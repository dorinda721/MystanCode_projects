"""
File: extension2_number_checker.py
Name:Dorinda
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    因數相加等於整數為完全數
    因數相加大於整數為盈數
    因數相加小於整數為虧數
    """
    print("Welcome to the number checker!")
    while True:
        num = int(input("n: "))
        if num == EXIT:
            print("Have a good one!")
            break
        else:
            ans = 0
            for i in range(1, num):
                if num % i == 0:  # 能被i整除餘數為0即為因數
                    ans += i
            if ans == num:  # ans為相加的因數和
                print(str(num) + " is a perfect number")
            elif ans > num:
                print(str(num) + " is an abundant number")
            else:
                print(str(num) + " is a deficient number")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
