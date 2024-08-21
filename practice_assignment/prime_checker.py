"""
File: prime_checker.py
Name:Dorinda
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	判別是否為質數
	"""
	print("Welcome to the prime checker!")
	while True:
		num = int(input("n: "))
		if num == EXIT:
			print("Have a good one!")
			break
		else:
			for i in range(2, num+1):  # 從2開始因為所有數字都可被1整除
				if num % i == 0 and i != num:  # num為偶數且除數不等於被除數
					print(str(num) + " is not a prime number.")
					break
				else:
					if i == num:  # i等於num時亦為沒有其他數字可被整除
						print(str(num) + " is a prime number.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
