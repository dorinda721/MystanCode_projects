"""
File: hailstone.py
Name:Dorinda
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    If odd number, n*3+1
    If even number, n/2
    """
    print("This program computes Hailstone sequences.")
    n = int(input("Enter a number:"))
    count = 0

    while n != 1:
        count += 1  # 計算次數
        if n % 2 == 0:  # 判斷為偶數
            even_num = n
            n = int(n / 2)
            print(str(even_num) + " is even, so I take half: " + str(n))
        else:
            odd_num = n
            n = int(n*3+1)
            print(str(odd_num) + " is odd, so I take half: " + str(n))
    print("It took " + str(count) + " step to reach 1.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
