"""
File: weather_master.py
Name:Dorinda
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	compute the average, highest, lowest, cold days among the inputs.
	"""
	print('stanCode "Weather Master 4.0!"')
	weather = int(input("Next Temperature: (or " + str(EXIT) + " to quit)?"))
	if weather == EXIT:
		print("No temperature were entered.")
	else:
		highest = weather
		lowest = weather
		sum_tep = weather
		day = 0
		sum_n = 1
		if weather < 16:  # 因有第一輸入的值，所以也必須納入是否低於16度
			day += 1
		while True:
			weather = int(input("Next Temperature: (or " + str(EXIT) + " to quit)?"))
			if weather == EXIT:
				break
			sum_n += 1
			sum_tep += weather
			if weather < 16:  # 低於16度的天數
				day += 1
			if weather > highest:
				highest = weather
			if weather < lowest:
				lowest = weather
		avg = float(sum_tep/sum_n)  # 平均溫度
		print("Highest temperature= " + str(highest))
		print("Lowest temperature= " + str(lowest))
		print("Average= "+str(avg))
		print(str(day) + " cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
