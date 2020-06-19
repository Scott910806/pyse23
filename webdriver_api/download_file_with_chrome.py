'''
chrome浏览器下载文件
'''
import os
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_settings.popups': 0,
     'download.default_directory': os.getcwd()
}
options.add_experimental_option("prefs",prefs)

dr = webdriver.Chrome(chrome_options = options)
dr.get("https://pypi.org/project/selenium/#files")
dr.find_element_by_link_text("selenium-3.141.0.tar.gz").click()