import unittest
from main import check_odd_or_even

def test_check_odd_or_even():
    assert check_odd_or_even(2) == "偶数"
    assert check_odd_or_even(0) == "偶数"
    assert check_odd_or_even(-4) == "偶数"
    assert check_odd_or_even(1) == "奇数"
    assert check_odd_or_even(-3) == "奇数"
    assert check_odd_or_even(7) == "奇数"

if __name__ == "__main__":
    test_check_odd_or_even()
    print("全てのテストが成功しました。")
