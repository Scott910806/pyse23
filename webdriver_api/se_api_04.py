'''
用126邮箱页面联系ifram表单切换
'''
from time import sleep
from selenium import webdriver

dr = webdriver.Chrome()
dr.get("https://www.126.com")
# sleep(2)
# dr.find_element_by_css_selector("#switchAccountLogin").click()
# sleep(2)

elem = dr.find_element_by_css_selector("div#loginDiv > iframe")
dr.switch_to.frame(elem) # 进入frame标签

dr.find_element_by_css_selector("[name = 'email']").send_keys("yxma2010")
dr.find_element_by_css_selector("[name = 'password']").send_keys("pihai123456")

dr.switch_to.parent_frame() #退出