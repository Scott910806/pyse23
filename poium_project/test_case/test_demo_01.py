import unittest
import time
'''python跨目录导包：将要引用的包所在路径，添加到系统环境变量'''
import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_path = os.path.join(base_path, 'page_modul')
sys.path.append(target_path)

from page_object import BaiduHomePage
from selenium import webdriver


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
        cls.dr.close()

    def test_case1(self):
        self.dr.get(self.base_url)
        page = BaiduHomePage(self.dr)
        page.search_input.send_keys("unittest")
        page.search_button.click()
        self.assertEquals(self.dr.title, "unittest_百度搜索")

if __name__ == '__main__':
        unittest.main()