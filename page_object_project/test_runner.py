import time
import unittest
from HTMLTestRunner import HTMLTestRunner


if __name__ == "__main__":
    
    suit = unittest.defaultTestLoader.discover(
        start_dir = './test_case',
        pattern = 'demo*.py'
    )

    current_time = time.strftime('%y_%m_%d_%H_%M_%S')
    with open('./test_reports/'+current_time+' report.html', 'wb') as f:
        runner = HTMLTestRunner(f)
        runner.run(suit)