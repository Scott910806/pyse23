import unittest
import time
from ddt import ddt, data, file_data, unpack
from selenium import webdriver
from public import baidu_search

@ddt
class TestDdt_02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
         cls.dr.close()

    # 数据为组合，list
    @data(["selenium","selenium_百度搜索"],
    ["unittest","unittest_百度搜索"],
    ["python","python_百度搜索"]
    )
    @unpack
    def test_ddt_example_02(self, search_word, result_title):
        print("search_word-->",search_word)
        print("result_title-->",result_title)

        self.dr.get(self.base_url)
        baidu_search(self.dr, search_word)
        time.sleep(2)
        self.assertEquals(self.dr.title,result_title)

    # 数据为组合，tupe
    @data(("selenium","selenium_百度搜索"),
    ("unittest","unittest_百度搜索"),
    ("python","python_百度搜索")
    )
    @unpack
    def test_ddt_example_03(self, search_word, result_title):
        self.dr.get(self.base_url)
        baidu_search(self.dr, search_word)
        time.sleep(2)
        self.assertEquals(self.dr.title,result_title)

     # 数据为组合，dict
    @data(
        {"search_word":"selenium","result_title":"selenium_百度搜索"},
        {"search_word":"unittest","result_title":"unittest_百度搜索"},
        {"search_word":"python","result_title":"python_百度搜索sss"}
        )
    @unpack
    def test_ddt_example_04(self, search_word, result_title): # 函数的参数名必须与dict中的key相同
        self.dr.get(self.base_url)
        baidu_search(self.dr, search_word)
        time.sleep(2)
        self.assertEquals(self.dr.title,result_title)

    
if __name__ == "__main__":
    unittest.main()