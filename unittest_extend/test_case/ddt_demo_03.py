import unittest
import time
from ddt import ddt, file_data
from selenium import webdriver
from public import baidu_search
import os

# 获取json文件路径
path_01 = os.path.dirname(os.path.abspath(__file__))
path_02 = os.path.dirname(path_01)
file_path = os.path.join(path_02, "test_data", "ddt_data.json")
print(file_path)


@ddt
class TestDdt_03(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
         cls.dr.close()

    # 读取外部json文件
    @file_data(file_path)
    def test_ddt_example(self,search_word,result_title): # 函数接收的参数名必须与json文件中的key相同
        self.dr.get(self.base_url)
        baidu_search(self.dr, search_word)
        time.sleep(2)
        self.assertEquals(self.dr.title,result_title)

if __name__ == "__main__":
    unittest.main()