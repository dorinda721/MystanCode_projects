"""
File: extension3_triangular_checker.py
Name: Dorinda
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    判別是否為等邊三角形
    """
    print("Welcome to the triangular number checker!")
    while True:
        num = int(input("n: "))
        if num == EXIT:
            print("Have a good one!")
            break
        else:
            for i in range(1, num):
                if num == i*(i+1)/2:  # 數字要相等於右邊的公式
                    print(str(num)+" is a triangular number")
                    break
            else:
                print(str(num) + " is not a triangular number")


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
