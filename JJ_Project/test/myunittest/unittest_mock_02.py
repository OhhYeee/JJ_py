from unittest import mock
import unittest
import test.myunittest.mock_temple as mock_temple


class Test_Zhifu_Status(unittest.TestCase):
    @mock.patch("test.myunittest.mock_temple.zhifu")
    def test_01(self, mock_zhifu):
        # 方法一：Mock方法
        # mock_temple.zhifu = mock.Mock(return_value={"result": "success", "reason": "null"})

        # 方法二：mock.patch装饰器模拟返回结果
        mock_zhifu.result_valule = {"result": "success", "reason": "null"}
        status = mock_temple.zhifu_statues()
        print(status)
        self.assertEqual(status, '支付成功')

    @mock.patch("test.myunittest.mock_temple.zhifu")
    def test_02(self, mock_zhifu):
        # 方法一：Mock方法
        # mock_temple.zhifu = mock.Mock(return_value={"result": "fail", "reason": "余额不足"})

        # 方法二：mock.patch装饰器模拟返回结果
        mock_zhifu.result_valule = {"result": "fail", "reason": "余额不足"}
        status = mock_temple.zhifu_statues()
        print(status)
        self.assertEqual(status, '支付失败')

    @mock.patch("test.myunittest.mock_temple.zhifu")
    def test_03(self, mock_zhifu):
        # 方法一：Mock方法
        # mock_temple.zhifu = mock.Mock(return_value={"result": "fai", "reason": "余额不足"})

        # 方法二：mock.patch装饰器模拟返回结果
        mock_zhifu.result_valule = {"result": "fai", "reason": "余额不足"}
        status = mock_temple.zhifu_statues()
        print(status)
        self.assertEqual(status, '未知错误异常')

    @mock.patch("test.myunittest.mock_temple.zhifu")
    def test_04(self, mock_zhifu):
        # 方法一：Mock方法
        # mock_temple.zhifu = mock.Mock(return_value={})

        # 方法二：mock.patch装饰器模拟返回结果
        mock_zhifu.result_valule = {}
        status = mock_temple.zhifu_statues()
        print(status)
        self.assertEqual(status, '未知错误异常')


if __name__ == 'main':
    unittest.main()
