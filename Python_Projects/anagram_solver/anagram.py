"""
File: anagram.py
Name: PEI-WEN(Lisa) WANG
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 23

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variables
dictionary = set()            # All words in the dictionary
sub_dict = set()              # Snippets of all words in the dictionary
sub_all_lst = set()           # Snippets of all words that should be printed


def main():
    """
    This program recursively finds all the anagram(s) for the word input by user and terminates when the input string
    matches the EXIT constant defined at line 23
    """
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            # Load data
            s = s.lower()
            read_dictionary(len(s))

            spot_lst = []  # The place where the letters are
            for i in range(len(s)):
                spot_lst.append(i)

            # Algorithm
            start = time.time()
            find_anagrams(s, spot_lst)
            end = time.time()
            print('It took ', end - start, ' seconds.')


def read_dictionary(s_len):
    """
    This function will update the date of sub_dict and dictionary
    :param s_len: int, the length of the string that user inputted
    """
    sub_dict.clear()     # Remove all data
    dictionary.clear()   # Remove all data
    sub_all_lst.clear()  # Remove all data

    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()  # Remove '\n'
            if len(line) == s_len:
                for i in range(1, len(line) + 1):
                    if line[:i] not in sub_dict:
                        sub_dict.add(line[:i])
                dictionary.add(line)


def find_anagrams(s, spot_lst):
    """
    :param s: str, the word which is inputted by user
    :param spot_lst: lst, the place where the letters are
    """
    all_lst = []     # All results that user wants
    count_lst = [0]  # Remember how many results
    print('Searching...')
    helper(s, '', all_lst, count_lst, spot_lst)
    print(int(count_lst[0]), 'anagrams:', all_lst)


def helper(s, current_s, all_lst, count_lst, spot_lst):
    """
    :param s: str, the word which is inputted by user
    :param current_s: str, current string
    :param all_lst: lst, all results that user wants
    :param count_lst: lst, remember how many results
    :param spot_lst: lst, the place where the letters are
    """
    if current_s in dictionary:
        # Showing result
        print('Found: ', current_s)
        print('Searching...')
        count_lst[0] += 1
        all_lst.append(current_s)
        # Update data
        dictionary.remove(current_s)  # Avoid repeated printing
        add_sub_all_lst(current_s)    # It can reduce the loops of the same prefix
    elif (len(current_s) > 0 and current_s not in sub_dict) or current_s in sub_all_lst:
        pass
    else:
        for spot in spot_lst:
            # Choose
            current_s += s[spot]
            spot_lst.remove(spot)
            # Explore
            helper(s, current_s, all_lst, count_lst, spot_lst)
            # Un-choose
            current_s = current_s[:-1]
            spot_lst.append(spot)
            spot_lst.sort()


def add_sub_all_lst(current_s):
    """
    :param current_s: str, current string
    """
    for i in range(1, len(current_s) + 1):
        sub_all_lst.add(current_s[:i])


if __name__ == '__main__':
    main()
