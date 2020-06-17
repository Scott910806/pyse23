'''python跨目录导包：将要引用的包所在路径，添加到系统环境变量'''
import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_path = os.path.join(base_path, 'page_modul')
sys.path.append(target_path)

import seldom
from page_object import BaiduHomePage
from seldom import Seldom
from seldom import data
from seldom import excel_to_list

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excel_file_path = os.path.join(base_path, 'test_data', 'data_info.xlsx')

class MyTest2(seldom.TestCase):

    @data(excel_to_list(excel_file_path, sheet='search', line=2))
    def test_case1(self, search_word, result_title):
        self.open("https://www.baidu.com")
        page = BaiduHomePage(Seldom.driver)
        page.search_input.send_keys(search_word)
        page.search_button.click()
        self.assertTitle(result_title)

if __name__ == '__main__':
    seldom.main(debug=True)