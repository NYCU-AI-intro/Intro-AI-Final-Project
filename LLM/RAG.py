import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
#from langchain_openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA
import openai
from time import time
import logging


class Agent:
    def __init__(self):
        
        print('init start')
        print('load doc')
        start = time()
        load_dotenv() # load OPENAI_API_KEY
        loader = DirectoryLoader('./exdatabase', glob='*.txt') # load all the .txt in 
        documents = loader.load() # type: list{Document}
        end = time()
        print('time: ', end - start)

        print('split text')
        start = time()
        # text_splitter to split the document to adjust to the input limit of LLM
        text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
        splited_docs = text_splitter.split_documents(documents) # type: list{Document}, which means split n document, n = all tokens/100
        end = time()
        print('time: ', end - start)

        print('build db')
        # embedding text to vector for model
        start = time()
        embeddings = OpenAIEmbeddings()
        # store vector in Chroma vector database
        self.db = Chroma.from_documents(splited_docs, embeddings) # type: db
        print('build agent')
        self.qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model_name='gpt-3.5-turbo'), chain_type="map_reduce", retriever=self.db.as_retriever(), return_source_documents=True)
        end = time()
        print('time: ', end - start)
        print('init end')

    def ask_without_db(self, prompt: str, model="gpt-3.5-turbo"):
        print('ask_without_db start')
        start = time()
        response = openai.OpenAI().chat.completions.create(
            model=model,
            messages=[
                #{"role": "system", "content": "You are a prefessional assistant help people to find paper."},
                {"role": "user", "content": prompt},
            ]
        )
        end = time()
        print('time: ', end - start)
        print('ask_without_db end')
        return response.choices[0].message.content
        

# RetrievalQA: an QA system which can retrieval information from database
    def ask_question(self, prompt):
        
        print('ask_question start')
        '''''''''''''''''''''''
        'Question optimization'
        '''''''''''''''''''''''
        print('question optimization')
        start = time()
        question_template = ''
        with open('./prompt_engineering/question_template.txt', 'r', encoding='utf-8') as f:
            question_template = f.read()
        format_question = question_template + prompt + '\n'
        end = time()
        print('time: ', end - start)
        '''''''''''''''''''''''
        'Question optimization'
        '''''''''''''''''''''''

        '''''''''''''''''
        'Few-shot prompt'
        '''''''''''''''''
        print('Few-shot prompt')
        start = time()
        example_output = ''
        with open('./prompt_engineering/few_shot_prompting.txt', 'r', encoding='utf-8') as f:
            example_output = f.read()
        few_shot_prompt = 'This is an example output. **Output refer to the example.**\n' + \
                            'example output: \n' + \
                            f'{example_output}\n' 
        end = time()
        print('time: ', end - start)                 
        '''''''''''''''''
        'Few-shot prompt'
        '''''''''''''''''
        
        query = few_shot_prompt + format_question

        print('query with db')
        start = time()
        result = self.qa({"query": query})
        end = time()
        print('time: ', end - start)

        print('judge')
        if "I don't" in result['result'] or "I do not" in result['result']:
            result = self.ask_without_db(query)
        else: 
            result = result['result']

        print('translate...')
        start = time()
        chinese_example_output = ''
        with open('./prompt_engineering/few_shot_prompting_chinese.txt', 'r', encoding='utf-8') as f:
            chinese_example_output = f.read()
        chinese_few_shot_prompt = '這裡有一份範例輸出，**請根據範例進行翻譯**\n' + \
                            '範例輸出: \n' + \
                            f'{chinese_example_output}\n'   
        result_chinese = self.ask_without_db(chinese_few_shot_prompt + result + '\n請將這些翻譯成繁體中文')
        end = time()
        print('time: ', end - start)
        print('ask_question end')
        return result, result_chinese
    
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.ERROR)
    agent = Agent()
    while(1):
        question = input('輸入問題: ')
        result, result_chinese = agent.ask_question(question)
        print(result)
        print('////////////////////')
        print(result_chinese)
