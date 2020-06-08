from selenium import webdriver
from time import sleep
from public import Login

dr = webdriver.Chrome()
dr.maximize_window()

def test_case1():
    dr.get("https://mail.126.com")
    lg = Login(dr)
    lg.login("admin","a123456")
    sleep(3)
    lg.close_window()

def test_case2():
    dr.get("https://mail.126.com")
    lg = Login(dr)
    lg.login("guest","b678901")
    sleep(3)
    lg.close_window()

if __name__ == "__main__":
    # test_case1()
    # sleep(3)
    test_case2()