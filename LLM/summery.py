import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu') # cuda:0 -> first GPU
# {tensor}.to(device): put tensor to choosed deviced

model = AutoModelForCausalLM.from_pretrained("gpt2", n_head = 24)
model.to(device)

tokenizer = AutoTokenizer.from_pretrained("gpt2")

prompt = ''
with open('exampleText.txt', 'r', encoding='utf-8') as f:
    prompt = f.read()

'''''''''''''''''
'Few-shot prompt'
'''''''''''''''''
example_text = ''
with open('exampleText.txt', 'r', encoding='utf-8') as f:
    example_text = f.read()

example_output = ''
with open('exampleOutput.txt', 'r', encoding='utf-8') as f:
    example_text = f.read()

few_shot_prompt = f'This is an example text and example output. Please output according to the example.\n \
                    example text: \n \
                    {example_text}\n \
                    example output: \n \
                    {example_output}\n'                  
'''''''''''''''''
'Few-shot prompt'
'''''''''''''''''

question = '\nsummery the following paper text, and output appropriate Name, summery, domain tag, link: '
# preprocessed_prompt = few_shot_prompt + question + prompt
preprocessed_prompt = 'Are you a good model?'     


tokened_prompt = tokenizer(preprocessed_prompt, return_tensors="pt",) # return_tensor: which data type to return
tokened_prompt.to(device)

input_ids = tokened_prompt.input_ids

gen_tokens = model.generate(
    input_ids,
    do_sample=True, # GPT will choose word by probability, rather than directly choose the highest probility
    temperature=0.9, # higher -> output more ranodmly
    max_length = 1024, # default=20
)

gen_text = tokenizer.batch_decode(gen_tokens)[0]


print('---')
print(gen_text)
print('---')