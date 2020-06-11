'''unittest + selenium demo'''

import unittest
from time import sleep
from selenium import webdriver

# 模块化：将公用部分抽象为方法以供调用，可以保存在单独的文件中
def baidu_search(dr, keyword):
    dr.find_element_by_css_selector("input#kw").send_keys(keyword)
    dr.find_element_by_css_selector("input#su").click()

class BaiduTest(unittest.TestCase):
    
    # 所有用例执行前准备
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    # 所有用例执行后处置
    @classmethod
    def tearDownClass(cls):
        cls.dr.close()

    def test_case1(self):
        self.dr.get(self.base_url)
        baidu_search(self.dr, "unittest")
        sleep(2)
        self.assertEquals(self.dr.title, "unittest_百度搜索")

    def test_case2(self):
        self.dr.get(self.base_url)
        baidu_search(self.dr, "selenium")
        sleep(2)
        self.assertEquals(self.dr.title, "selenium_百度搜索")

if __name__ == "__main__":
    unittest.main()