'''
python导包，demo_01.py中引用的test_base.py文件，与demo_o1.py的上一级目录平级需要将
test_base.py所在的路径添加到系统环境变量，才可被正常引用
'''
import sys
import os
file_path =os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(file_path)

import unittest
from test_base import add
'''
unittest测试框架使用规则：
1、必须创建测试类，继承unittest.TestCase类
2、测试方法必须以test开头
'''
# 创建测试类
class MyTest1(unittest.TestCase):

    # 创建测试方法
    def test_case1(self):
        result = add(1, 1)
        self.assertEqual(result, 2)
    
    def test_case2(self):
        result = add(1, 1)
        self.assertEqual(result, 3) # 程序会抛出fail，fail表示断言失败


    def test_case3(self):
        result = add(1,'1')  # 程序会抛出error，error表示代码有错误
        self.assertEqual(result, 2)


if __name__ == "__main__":
    
    # 执行测试用例
    unittest.main()