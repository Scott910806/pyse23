'''
下载文件处理思路：配置浏览器，使点击下载时，不出现弹窗
Firefox浏览器文件下载
'''
import os
from selenium import webdriver

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.dir",os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","binary/octet-stream")

dr = webdriver.Firefox(firefox_profile=fp)
dr.get("https://pypi.org/project/selenium/#files")
dr.find_element_by_link_text("selenium-3.141.0.tar.gz").click()