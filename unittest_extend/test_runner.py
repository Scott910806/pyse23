import unittest

suit = unittest.defaultTestLoader.discover(
    start_dir = './test_case',
    pattern = 'parameterized*.py'
)

runner = unittest.TextTestRunner()
runner.run(suit)