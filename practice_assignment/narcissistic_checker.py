"""
File: extension4_narcissistic_checker.py
Name:Dorinda
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    正整數的個別位數的數字，乘上總位數次方的和等於正整數
    例如：153==1**3+5**3+3**3
    """
    print("Welcome to the narcissistic number checker!")
    while True:
        num = int(input("n: "))
        if num == EXIT:
            print("Have a good one!")
            break
        else:
            n = num
            sum_n = 0
            i = len(str(num))  # 正整數的所有位數
            while True:
                # 個別算出每個位數的數字
                if n >= 1:
                    nn = n % 10
                    sum_n += nn ** i
                    n //= 10
                else:
                    break
            if num == sum_n:
                print(str(num)+" is a narcissistic number")
            else:
                print(str(num)+" is not a narcissistic number")


if __name__ == '__main__':
    main()
