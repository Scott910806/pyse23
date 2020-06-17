from selenium import webdriver
from time import sleep
from public import baidu_search

# 读取txt文件，建议使用'with open'方法
with open('./data/search_data.txt','r') as f:
    keywords_list = f.readlines()
print(keywords_list)

# 处理每一行末尾的回车符
keywords = []
for keyword in keywords_list:
    keywords.append(keyword.strip())
print(keywords)

dr = webdriver.Chrome()

for word in keywords:
    dr.get("https://www.baidu.com")
    baidu_search(dr, word)
    sleep(3)
    print(dr.title)    
    