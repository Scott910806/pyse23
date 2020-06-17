import seldom
import os
from seldom import data
from seldom import excel_to_list

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excel_file_path = os.path.join(base_path, 'test_data', 'data_info.xlsx')


class YourTest(seldom.TestCase):

    # 使用外部excel文件数据
    @data(excel_to_list(file=excel_file_path, sheet='search', line=2))
    def test_case(self, search_word, result_title):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(css="input#kw", text=search_word)
        self.click(css="input#su")
        self.assertTitle(result_title)


if __name__ == '__main__':
    seldom.main(debug=True)
