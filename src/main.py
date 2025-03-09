def check_odd_or_even(number):
    """
    入力された整数が奇数か偶数かを判断して返す関数
    
    Args:
        number (int): 判断したい整数
        
    Returns:
        str: "偶数" または "奇数" の文字列
    """
    if number % 2 == 0:
        return "偶数"
    else:
        return "奇数"


# # 使用例
# if __name__ == "__main__":
#     try:
#         num = int(input("整数を入力してください: "))
#         result = check_odd_or_even(num)
#         print(f"{num}は{result}です。")
#     except ValueError:
#         print("整数を入力してください。")