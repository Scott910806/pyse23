'''
显示等待和隐式等待
'''
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
# dr.implicitly_wait(5) 隐式等待

print(time.ctime())
# 若元素不存在，则需要处理程序抛出的超时异常，才可继续执行
# 显示等待
try:
    search_elem = WebDriverWait(dr,5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"input#kw0001"))
        )
except TimeoutException:
    pass

print(time.ctime())