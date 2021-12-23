from test.myunittest.calculator import Count
import unittest


class TestAdd(unittest.TestCase):
    def setUp(self):
        print('----------test start----------')

    def test_add(self):
        obj = Count(2, 3)
        self.assertEqual(obj.add(), 5, '计算错误！')

    def tearDown(self):
        print('----------test end----------')


if __name__ == 'main':
    # 构造测试用例
    suite = unittest.TestSuite()
    suite.addTest(TestAdd('test_add'))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)