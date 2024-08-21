"""
File: quadratic_solver.py
Name:Dorinda
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	大於0,會有兩個值
	等於0,一個值
	小於零,沒有值
	"""
	print("stanCode Quadratic Solver!")
	a = int(input("Enter a:"))
	b = int(input("Enter b:"))
	c = int(input("Enter c:"))

	x = int(b*b-4*a*c)  # x為判別式變數
	if x > 0:  # 依據x的數字大小進行後續的方程式，並算出root的數值
		y = math.sqrt(x)
		root1 = (-b + y) / (2 * a)
		root2 = (-b - y) / (2 * a)
		print("Two root:"+str(root1)+","+str(root2))
	elif x == 0:
		y = math.sqrt(x)
		root = (-b + y) / (2 * a)
		print("One root:"+str(root))
	else:
		print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
