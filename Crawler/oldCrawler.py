from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
import time
import os
import wget
from PyPDF2 import PdfReader

PATH = "C:/Users/USER/Desktop/chromedriver-win32/chromedriver.exe"

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://arxiv.org/list/cs.AI/2401?skip=0&show=25")

path = os.path.join('january')
os.mkdir(path)
cnt=0
for j in range(1, 78):
    pdfs = driver.find_elements(by= By.LINK_TEXT, value= 'pdf')
    for pdf in pdfs:
        contains = []
        save_as = os.path.join(path, 'txt' + str(cnt) + '.pdf')
        #pdf = driver.find_element(by= By.XPATH, value='/html/body/div[2]/main/div/div/div/dl/dt['+str(1)+'/a[3]')
        #print(pdf.get_attribute('href'))

        try:
            wget.download(pdf.get_attribute('href'), save_as)
            cnt+=1
        except:
            cnt+=1
            continue
        try:
            
            reader = PdfReader(save_as,  strict=False)
            new_txt = os.path.join(path, 'txt' + str(cnt) + '.txt') 
            f = open(new_txt, "w", encoding='UTF-8')
            for page in reader.pages:
                contains.append(page.extract_text())
            f.write(' '.join(contains))
            f.close()
        except:
            print(cnt)
        os.remove(save_as)
    s = str(j)
    if(j>=5):
        s= str(5)
    nextPage = driver.find_element(by=By.XPATH, value='//*[@id="dlpage"]/div[1]/a['+s+']')
    driver.get(nextPage.get_attribute('href'))

driver.close()
#//*[@id="dlpage"]/div[1]/a[5]