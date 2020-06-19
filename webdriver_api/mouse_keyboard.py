'''
鼠标和键盘操作
'''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains #鼠标操作方法封装在ActionChains类中
from selenium.webdriver.common.keys import Keys #键盘操作方法封装在Keys类中

dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.maximize_window() #设置窗口最大化

time.sleep(2)
'''
#火狐浏览器
dr01 = webdriver.Firefox()
dr01.get("https://www.baidu.com")

#Edge浏览器，注意：新版本的edge浏览器驱动默认名称为msedgedriver.exe,
#需要更名为MicrosoftWebDriver.exe,并将路径添加到系统环境变量path
dr02 = webdriver.Edge()
dr02.get("https://huke88.com")
'''
elem = dr.find_element_by_css_selector("div#u1>span")
ActionChains(dr).move_to_element(elem).perform() #鼠标悬停

elem_01 = dr.find_element_by_css_selector("input#kw")
elem_01.send_keys("seleniumm")
time.sleep(2)
elem_01.send_keys(Keys.BACK_SPACE) #退格键
time.sleep(2)
elem_01.send_keys(Keys.SPACE) #增加空格
time.sleep(2)
elem_01.send_keys("教程")
time.sleep(2)
elem_01.send_keys(Keys.CONTROL,'a') #ctrl+a全选
time.sleep(2)
elem_01.send_keys(Keys.CONTROL,'x') #ctrl+x剪切
time.sleep(2)
elem_01.send_keys(Keys.CONTROL,'v') #ctrl+v粘贴
time.sleep(2)
elem_01.send_keys(Keys.ENTER) #回车
#dr.find_element_by_css_selector("input#su").send_keys(Keys.ENTER) 虫师教材写法，效果同上