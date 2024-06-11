# LLM輔助論文檢索與綜整

## Overview

使用selenium做爬蟲抓取arXiv的資料，接著使用langchain與OpenAI api建置以爬蟲資料為資料庫的RAG LLM與一般的LLM，並且使用discord bot做互動

可以對於discord bot發指令，讓bot從資料庫或是過去的訓練資料中，查找相關的論文。

## 環境

python version: 3.8.18
package version: in requirement.txt

## 使用方法

1. clone project

2. 在project folder中創建.env檔，在裡面加入discord bot的token，變數名為bot_token

3. 在LLM folder中創建.env檔，在裡面加入OpenAI的token，變數名為OPENAI_API_KEY

4. 因為database過大，因此project中未附上database，要運行Crawler資料夾底下的Crawler.py抓取資料(預估約為2小時左右)。創建一個database資料夾在LLM資料夾底下，並把資料的txt檔移動到database資料夾中

5. 在project folder中運行main.py，即可開啟discord bot，會自動進行LLM model與資料庫的建置，並且把discord bot部署(大概需要20分鐘)

6. 在伺服器中，對discord bot下"=search {input question}"，等待10~20秒鐘，就可以得到輸出的結果

## 實驗結果

我們的evalution方式主要有3個，格式正確率、內容正確率、內容相關率。格式正確率的定義為: 輸出的格式正確無誤，內容正確率的定義為: 輸出的內容正確無誤，內容相關率的定義為: 輸出的結果與問題相關。評估的方式是，對於model提問不同多元的問題，包括了中文或英文、不同領域知識、敘事型或關鍵字型。最後由我們人工判讀資料是否正確，並記錄結果分析。

對於我們的model，做了30次的測試之後，格式正確率為93.3%(28/30)，內容正確率為13.3%(4/30)，內容相關率為96.6%(29/30)，內容正確率的出錯，全部都是link與內容不合，但名稱、總結、tag的部分皆未觀察到出錯。