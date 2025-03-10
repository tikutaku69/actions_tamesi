import unittest
import sys
import os
from unittest.mock import patch
from io import StringIO

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from judge import check_odd_or_even, order

def test_check_odd_or_even():
    print("test_check_odd_or_evenを実行してる")
    assert check_odd_or_even(2) == "偶数"
    assert check_odd_or_even(0) == "偶数"
    assert check_odd_or_even(-4) == "偶数"
    assert check_odd_or_even(1) == "奇数"
    assert check_odd_or_even(-3) == "奇数"
    assert check_odd_or_even(7) == "奇数"

def test_order():
    print("test_orderを実行してる")
    
    # テストケース1: 正常入力（偶数）
    with patch.object(sys, 'argv', ['judge.py', '4']), patch('sys.stdout', new=StringIO()) as mock_stdout:
        result = order()
        assert result == "偶数"
        assert "4は偶数です。" in mock_stdout.getvalue()
    
    # テストケース2: 正常入力（奇数）
    with patch.object(sys, 'argv', ['judge.py', '5']), patch('sys.stdout', new=StringIO()) as mock_stdout:
        result = order()
        assert result == "奇数"
        assert "5は奇数です。" in mock_stdout.getvalue()
    
    # テストケース3: 引数なし
    with patch.object(sys, 'argv', ['judge.py']), patch('sys.stdout', new=StringIO()) as mock_stdout:
        result = order()
        assert result is None
        assert "使用方法: python judge.py <整数>" in mock_stdout.getvalue()
    
    # テストケース4: 不正な入力（文字列）
    with patch.object(sys, 'argv', ['judge.py', 'abc']), patch('sys.stdout', new=StringIO()) as mock_stdout:
        result = order()
        assert result is None
        assert "整数を入力してください。" in mock_stdout.getvalue()


def test_even_number():
    """偶数を入力した場合のテスト"""
    print("test_even_numberを実行してる")
    with patch('sys.argv', ['judge.py', '2']):
        with patch('builtins.print') as mocked_print:
            result = order()
            mocked_print.assert_called_with("2は偶数です。")
            assert result == "偶数"


if __name__ == "__main__":
    test_check_odd_or_even()
    test_order()
    test_even_number()
    print("全てのテストが成功しました。")
