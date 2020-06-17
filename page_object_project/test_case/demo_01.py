import unittest
import time
from selenium import webdriver
from ddt import ddt, file_data
from page_model import BaiduHomePage
from config import baidu_search_data_path

@ddt
class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    @file_data(baidu_search_data_path)
    def test_case_01(self, search_word, result_title):
        self.driver.get(self.base_url)
        page = BaiduHomePage(self.driver)
        page.search_input.send_keys(search_word)
        page.search_button.click()
        time.sleep(2)
        self.assertEquals(self.driver.title, result_title)  