"""
File: extension1_factioral.py
Name: Dorinda
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	階乘公式，從1一路乘到輸入的數字
	"""
	print("Welcome to stanCode factorial master!")
	while True:
		n = int(input("Give me a number, and I will list the answer of factorial: "))
		if n == EXIT:
			print("------ See ya! ------")
			break
		else:
			ans = 1
			for i in range(1, n+1):  # n+1包含n
				ans *= i
			print("Answer: " + str(ans))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()
