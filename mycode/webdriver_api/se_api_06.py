'''
警告框的处理
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

dr = webdriver.Chrome()
dr.get("https://www.baidu.com")

elem = dr.find_element_by_css_selector("div#u1 > span")
ActionChains(dr).move_to_element(elem).perform()

dr.find_element_by_link_text("搜索设置").click()
sleep(2)
dr.find_element_by_link_text("保存设置").click()
sleep(2)
alert = dr.switch_to.alert #获取警告框对象
print(alert.text)
sleep(2)
alert.accept()