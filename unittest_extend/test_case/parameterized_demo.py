'''
parameterized 扩展的使用
本例用参数化实现百度搜索测试用例
'''

import unittest
import time
from parameterized import parameterized
from selenium import webdriver

class TestParameterized(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
         cls.dr.close()

    # 列表内的每个tupe为一组测试用例的数据
    @parameterized.expand([("testcase1","selenium","selenium_百度搜索"),
        ("testcase2","unittest","unittest_百度搜索"),
        ("testcase3","python","python_百度搜索")]
    )
    def test_baidu_search(self,test_name,search_word,result_title):
        
        # 打印一些信息
        print("test_name-->",test_name)
        print("search_word-->",search_word)
        print("result_title-->",result_title)

        self.dr.get(self.base_url)
        self.dr.find_element_by_css_selector("input#kw").send_keys(search_word)
        self.dr.find_element_by_css_selector("input#su").click()
        time.sleep(2)
        self.assertEquals(self.dr.title,result_title)


if __name__ == "__main__":
    unittest.main()