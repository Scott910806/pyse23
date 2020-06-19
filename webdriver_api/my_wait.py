'''
封装自己的等待方法
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
# from selenium.common.exceptions import TimeoutException

def wait_element(dr,by,value,timeout=10):
    for i in range(timeout):
        try:
            elem = dr.find_element(by,value)
        except NoSuchElementException:
            sleep(1)
        else:
            break
    else:
        raise TimeoutException("通过{by} = {value}找不到元素".format(by=by,value=value))
    return elem


dr = webdriver.Chrome()
dr.get("https://www.baidu.com")

wait_element(dr,By.CSS_SELECTOR,"#kw",3).send_keys("selenium")
wait_element(dr,By.CSS_SELECTOR,"#su00",3).click()
dr.quit()