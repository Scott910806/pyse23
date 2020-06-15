'''
ddt的使用
'''
import unittest
from ddt import ddt, data, file_data

@ddt
class TestDdt_01(unittest.TestCase):

    # 数据为单个值
    @unittest.skip("跳过测试")
    @data(3, 4, 5, 6)
    def test_ddt_example_01(self, value):
        print("value-->",value)

if __name__ == "__main__":
    unittest.main()