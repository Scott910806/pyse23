## 基本概念
* test fixtrue :  setUp/tearDown，用例执行前和执行后的处理
* test case : 测试用例
* test suit : 要执行用例的一个集合
* test runner: 运行测试套件里面的用例


## unittest使用规则
* 必须创建测试类，继承unittest.TestCase类
* 创建的测试方法名字必须以“test”开头

## 用例执行结果中 fail、error的区别
* fail表示断言失败
* error表示代码有错误

## 用例的查询和执行方式
* unittest.main()，只适用于执行当前文件中的用例
* test suit + unittest.TextTestRunner，执行大量用例时，比较繁琐
* discover + unittest.TextTestRunner，适合批量执行用例

## 用例的执行顺序
* a ~z , A ~ Z   
目录、文件、类、方法   
aa_test/aa_test.py.AATest.test_aa_case

* 只有 TestSuite 可以控制用例的执行顺序，discover() 和 main() 都是按照ASCII码的顺序执行用例