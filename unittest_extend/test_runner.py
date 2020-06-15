import time
import unittest
from HTMLTestRunner import HTMLTestRunner

suit = unittest.defaultTestLoader.discover(
    start_dir = './test_case',
    pattern = 'ddt*.py'
)

# runner = unittest.TextTestRunner()
# runner.run(suit)

# 用时间戳区分测试报告
current_time = time.strftime("%Y_%m_%d_%H_%M_%S")
with open('./test_reports/'+current_time+' result.html','wb') as f:
    runner = HTMLTestRunner(stream=f, title='parameterized', description='automation test project')
    runner.run(suit, rerun=1, save_last_run=False)