import sys

def check_odd_or_even(number):
    """
    入力された整数が奇数か偶数かを判断して返す関数
    
    Args:
        number (int): 判断したい整数
        
    Returns:
        str: "偶数" または "奇数" の文字列
    """
    print("check_odd_or_even関数を実行してる")
    if number % 2 == 0:
        return "偶数"
    else:
        return "奇数"


def order():
    """
    システム引数から整数を読み込み、check_odd_or_even関数に渡す関数

    Returns:
        str: check_odd_or_even関数の結果
    """
    print("order関数を実行してる")

    if len(sys.argv) < 2:
        print("使用方法: python judge.py <整数>")
        return None

    try:
        number = int(sys.argv[1])
        result = check_odd_or_even(number)
        print(f"{number}は{result}です。")
        return result
    except ValueError:
        print("整数を入力してください。")
        return None

# 使用例
if __name__ == "__main__":
    order()