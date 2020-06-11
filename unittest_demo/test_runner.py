import unittest
'''跨文件批量执行测试用例'''

# 查询用例并组装成suit
suit = unittest.defaultTestLoader.discover(     
    start_dir = './test_case', # 指定文件所在路径
    pattern = 'demo*.py' # 指定文件名匹配规则
)

# 执行suit
runner = unittest.TextTestRunner()
runner.run(suit)

'''
 关于'start_dir'的说明：
 对于多层级目录，如用例文件存放在test_case/file_01,file_02两个文件夹中
 则需要分别在file_01,file_02文件夹下新建'__init__.py'空文件 （'__init__.py'文件的作用是，
 标识该文件目录是一个标准的包含了python模块的目录）
''' 