'''
python导包，demo_02.py中引用的test_base.py文件，与demo_02.py的上一级目录平级，需将
test_base.py所在的路径添加到系统环境变量，才可被正常引用
'''
import sys
import os
file_path =os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(file_path)

import unittest
from test_base import add
'''测试套件的使用'''

class MyTest2(unittest.TestCase):

    # 用例执行前置
    def setUp(self):
        print("start test")
    
    # 用例执行后置
    def tearDown(self):
        print("end test")

    def test_case1(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_case2(self):
        result = add(2, 3)
        self.assertEqual(result, 4)

    def test_case3(self):
        result = add(2.1, 3.2)
        self.assertEqual(result, 4)

if __name__ == "__main__":
    
    # 创建test suit
    suit = unittest.TestSuite()
    suit.addTest(MyTest2("test_case1"))
    suit.addTest(MyTest2("test_case2"))
    
    # 创建test runner，执行suit 
    runner = unittest.TextTestRunner()
    runner.run(suit)