from selenium import webdriver
from time import sleep
from public import Login

def test_case1():
    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.get("https://mail.126.com")
    lg = Login(dr) # 实例化类
    lg.login("admin","a123456")
    sleep(3)
    lg.close_browser()

def test_case2():
    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.get("https://mail.126.com")
    lg = Login(dr) # 实例化类
    lg.login("guest","b678901")
    sleep(3)
    lg.close_browser()

if __name__ == "__main__":
    test_case1()
    test_case2()