'''
窗口切换
'''
import time
from selenium import webdriver

dr = webdriver.Chrome()
dr.implicitly_wait(5)
dr.maximize_window()
dr.get("https://www.126.com")

login_handle = dr.current_window_handle #获取当前窗口句柄

dr.find_element_by_link_text("注册免费邮箱").click()

all_handles = dr.window_handles #获取所有窗口句柄

#通过for循环获取注册窗口句柄
register_handle = None
for handle in all_handles:
    if handle != login_handle:
        register_handle = handle

dr.switch_to.window(register_handle) #切换到注册窗口
dr.find_element_by_css_selector("input#username").send_keys("yxma2010")
dr.find_element_by_css_selector("input#password").send_keys("pihai123456")
