"""
File: boggle.py
Name: PEI-WEN(Lisa) WANG
----------------------------------------
This program recursively finds all the word(s)
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'  # The file name of the dictionary txt file
LEN = 4                  # The side length

# Global Variables
dictionary = set()       # All words in the dictionary
sub_dict = set()         # Snippets of all words in the dictionary
spot_dict = {}           # Spots' neighbors


def main():
	"""
	This program recursively finds all the word(s)
	"""
	# Load data
	read_dictionary()

	# Remember one's neighbors' spots
	for r in range(LEN):
		for c in range(LEN):
			spot = r * LEN + c
			spot_set = set()
			for i in range(-1, 2):      # Control the change of neighbors' x coordinate
				for j in range(-1, 2):  # Control the change of neighbors' y coordinate
					if (0 <= r + i < LEN) and (0 <= c + j < LEN) and (r + i) * LEN + c + j != spot:
						spot_set.add((r + i) * LEN + c + j)
			spot_dict[spot] = spot_set

	# Input
	all_lst = []
	for i in range(1, LEN+1):
		row = input(str(i) + ' row of letters: ')
		row_lst = [letter.lower() for letter in row.split()]
		if illegal_input(row_lst):
			print('Illegal input')
			break
		for letter in row_lst:
			all_lst.append(letter)

	# Letters' spots in all_lst
	spot_lst = []
	for i in range(len(all_lst)):
		spot_lst.append(i)

	# Algorithm
	start = time.time()
	find_words(all_lst, spot_lst)
	end = time.time()
	print('It took ', end - start, ' seconds.')


def find_words(all_lst, spot_lst):
	"""
	:param all_lst: lst, all letters that user inputted
	:param spot_lst: lst, all spots of letters
	"""
	count_lst = [0]
	helper('', all_lst, spot_lst, count_lst, [])
	print('There are ' + str(count_lst[0]) + ' words in total.')


def helper(current_s, all_lst, spot_lst, count_lst, current_spot):
	"""
	:param current_s: str, current string
	:param all_lst: lst, all letters that user inputted
	:param spot_lst: lst, all spots of letters
	:param count_lst: lst, how many words
	:param current_spot: lst, spots of all letters that are in the current string
	"""
	if current_s in dictionary:
		print('Found \"' + current_s + '\"')
		count_lst[0] += 1
		dictionary.remove(current_s)  # Avoid repeated printing
	for spot in spot_lst:
		if len(current_s) > 0 and spot not in spot_dict[current_spot[-1]]:
			pass
		elif len(current_s) > 0 and current_s not in sub_dict:
			pass
		else:
			# Choose
			current_s += all_lst[spot]
			current_spot.append(spot)
			spot_lst.remove(spot)
			# Explore
			helper(current_s, all_lst, spot_lst, count_lst, current_spot)
			# Un-choose
			current_s = current_s[:-1]
			current_spot.pop()
			spot_lst.append(spot)
			spot_lst.sort()


def illegal_input(row_lst):
	"""
	:param row_lst: lst, row that user inputted
	:return: bool, make sure whether the input is illegal
	"""
	if len(row_lst) != LEN:
		return True
	for letter in row_lst:
		if len(letter) > 1 or letter.isalpha() is False:
			return True
	return False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python set
	"""
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			if LEN * LEN >= len(line) >= 4:
				dictionary.add(line)
				for i in range(1, len(line) + 1):
					if line[:i] not in sub_dict:
						sub_dict.add(line[:i])


if __name__ == '__main__':
	main()
