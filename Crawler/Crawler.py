from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import wget

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get('https://arxiv.org/list/cs.AI/2024-06?skip=0&show=25')
weblink = 'https://arxiv.org/list/cs.AI/2024-06?skip=0&show=25'
cnt = 12471
err = 0
page = 0
dataPath = "C:/Users/ASUS/Desktop/新增資料夾/data"
while 1:
    links = driver.find_elements(by= By.PARTIAL_LINK_TEXT, value='arXiv:2406.')
    links = [link.get_attribute("href") for link in links]
    for link in links:
        try:
            driver.get(link)
            cnt+=1
        except:
            err+=1
        try:
            title = driver.find_element(by= By.XPATH, value="//*[@id=\"abs\"]/h1")
        except:
            title = "None"
        try:
            content = driver.find_element(by = By.XPATH, value= "//*[@id=\"abs\"]/blockquote")
        except:
            content = "None"
        txt = "Name\n" + title.text + "\n\nAbstract\n" + content.text + "\n\nLink:\n" + link
        f = open(os.path.join(dataPath, str(cnt)+'.txt'), "w", encoding='UTF-8')
        f.write(txt)
        f.close()
    driver.get(weblink)
    if page < 5:
        page += 1
    nextPage = driver.find_element(by= By.XPATH, value = '//*[@id=\"dlpage\"]/div[2]/a[' + str(page) +']')
    weblink = nextPage.get_attribute("href")
    driver.get(weblink)
print(err)
'''    
//*[@id="dlpage"]/div[2]/a[1]
//*[@id="dlpage"]/div[2]/a[2]
//*[@id="dlpage"]/div[2]/a[5]
//*[@id="dlpage"]/div[2]/a[5]
//*[@id="dlpage"]/div[2]/a[5]
//*[@id="dlpage"]/div[2]/a[5]
//*[@id="abs"]/h1
//*[@id="abs"]/blockquote
'''




