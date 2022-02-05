"""
File: weather_master.py
Name: PEI-WEN(Lisa) WANG
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
"""
EXIT = -1


def main():
	"""
	First of all, users have to choose which scale they want to use. Then, users need to enter temperature(s)
	which is/are integer(s) or decimal number(s) in degrees Celsius or Fahrenheit until they enter the EXIT number,
	and they will get the highest temperature, the lowest temperature, the average in both degrees Celsius
	and Fahrenheit. Besides, users will also get the number of cold day(s) that is/are below sixteen degrees Celsius.
	"""
	print('\"Weather Master 4.0\"!')
	print('Which scale do you want to use? 1.Celsius 2.Fahrenheit')
	scale = float(input('Please enter the number (1 or 2): '))  # The scale that the users chose
	while True:
		if scale == 1 or scale == 2:
			break
		else:
			scale = float(input('Please enter the number (1 or 2): '))

	temperature = float(input("First Temperature: (or " + str(EXIT) + " to quit)? "))
	if temperature == EXIT:
		print('No temperatures were entered.')
	else:
		if scale == 2:  # users chose Fahrenheit
			temperature = fahrenheit_to_celsius(temperature)
		maximum = temperature
		minimum = temperature
		total_temperature = temperature  # Calculating the total temperatures users entered
		number = 1  # Counting how many temperatures users entered
		cold_day = 0  # Counting how many day(s) that is/are below sixteen degrees Celsius
		if temperature < 16:
			cold_day += 1  # The first temperature is a cold day

		while True:
			temperature = float(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
			if temperature == EXIT:
				break
			if scale == 2:  # users chose Fahrenheit
				temperature = fahrenheit_to_celsius(temperature)
			if temperature > maximum:
				maximum = temperature
			if temperature < minimum:
				minimum = temperature
			if temperature < 16:
				cold_day += 1
			total_temperature += temperature
			number += 1
		average = total_temperature / number
		print('Highest temperature = ' + str(maximum) + '°C (' + str(celsius_to_fahrenheit(maximum)) + '°F)')
		print('Lowest temperature = ' + str(minimum) + '°C (' + str(celsius_to_fahrenheit(minimum)) + '°F)')
		print('Average = ' + str(average) + '°C (' + str(celsius_to_fahrenheit(average)) + '°F)')
		print(str(cold_day) + ' cold day(s)')


def celsius_to_fahrenheit(celsius):
	"""
	:param celsius: float, converting Celsius to Fahrenheit
	:return: float, temperature in degrees Fahrenheit
	"""
	fahrenheit = 9/5 * celsius + 32
	return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
	"""
	:param fahrenheit: float, converting Fahrenheit to Celsius
	:return: float, temperature in degrees Celsius
	"""
	celsius = (fahrenheit - 32) * 5/9
	return celsius


if __name__ == "__main__":
	main()
