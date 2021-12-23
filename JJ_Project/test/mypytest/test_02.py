import pytest  # 引入pytest包


@pytest.mark.website
def test_a():  # test开头的测试函数
    print("------->test_a")
    assert 1  # 断言成功


def test_b():
    print("------->test_b")
    assert 1  # 断言失败


def test_c():
    print("------->test_c")
    assert 1  # 断言失败


def test_d():
    print("------->test_d")
    assert 1  # 断言失败


class Test_Class:
    def test_aa(self):
        print("------->test_aa")
        assert 1

    def test_bb(self):
        print("------->test_bb")
        assert 0
