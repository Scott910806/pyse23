import seldom

# import os
# import sys
# base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# target_path = os.path.join(base_path, 'page_modul', 'page_object.py')
# sys.path.append(target_path)

from page_object import BaiduHomePage

class YourTest(seldom.TestCase):

    def test_case(self):
        
        self.open("https://www.baidu.com")
        page = BaiduHomePage(seldom.driver)
        page.search_input.send_keys("selenium")
        page.search_button.click()
        self.assertTitle("selenium_百度搜索")


if __name__ == '__main__':
    seldom.main(debug=True)
