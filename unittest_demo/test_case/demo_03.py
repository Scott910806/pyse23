'''跳过测试用例和预期失败'''

import unittest

class MyTest3(unittest.TestCase):

    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test aaa")

    @unittest.skipIf(3>2,"当条件为True时跳过测试")
    def test_skip_if(self):
        print("test bbb")

    @unittest.skipUnless(3>2,"当条件为True时执行测试")
    def test_skip_unless(self):
        print("test ccc")
    
    @unittest.expectedFailure # 直接预期失败
    def test_expected_failure(self):
        self.assertEqual(2, 3)

if __name__ == "__main__":
    unittest.main()