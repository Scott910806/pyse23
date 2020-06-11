''' test fixture 层次'''

import unittest

# 模块级别
def setUpModule():
    print("test module start>>>>>>>>>>>>>>>>")

def tearDownModule():
    print("test module end>>>>>>>>>>>>>>>>>")

class MyTest4(unittest.TestCase):

    # 类级别
    @classmethod
    def setUpClass(cls):
        print("test class start-------------")

    @classmethod
    def tearDownClass(cls):
        print("test class end--------------")

    # 用例级别
    def setUp(self):
        print("test case start")
    
    def tearDown(self):
        print("test case end")

    def test_case1(self):
        print("test case 1")

    def test_case2(self):
        print("test case 2")
    
if __name__ == "__main__":
    unittest.main()