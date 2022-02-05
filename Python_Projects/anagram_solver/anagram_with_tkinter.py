"""
File: anagram_with_tkinter.py
Name: PEI-WEN(Lisa) WANG
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 24

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time
import tkinter as tk

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
    matches the EXIT constant defined at line 24
    """
    # Create the window
    window = tk.Tk()
    window.title('anagram')
    window.geometry('800x900')
    window.configure(bg='skyblue')

    # Top labels
    header_label = tk.Label(window, text='Anagram', font=('Courier', 50), width=10, height=1, bg='skyblue')
    header_label.grid(row=0, column=1, sticky='nw')

    welcome_label = tk.Label(window, text='Welcome to \"Anagram Generator\" !', font=('Times', 15),
                             height=1, bg='skyblue')
    welcome_label.grid(row=1, column=1, sticky='nw')

    description_label = tk.Label(window,
                                 text='(If you want to enter more than one word, please separate it with space.) \n',
                                 font=('Times', 15), height=2, bg='skyblue')
    description_label.grid(row=2, column=1, sticky='nw')

    # Search bar
    label = tk.Label(window, text="Find anagrams for : ", font=('Times', 20), bg='skyblue')
    label.grid(row=3, column=0, sticky='nw')
    entry = tk.Entry(window, width=40, name='entry', borderwidth=2)
    entry.grid(row=3, column=1, sticky='w')
    entry.focus()

    # Result and Time
    result_label = tk.Label(window, text="Result & Time : ", font=('Times', 20), bg='skyblue')
    result_label.grid(row=4, column=0, sticky='nw')
    search_out = tk.Text(window, height=40, width=75, borderwidth=2, font=('Times', 15),
                         bg='seashell')
    search_out.grid(row=4, column=1, sticky='w')

    # When <return> key is hit in a text field .. connect to the and handle_search() functions to do the work.
    entry.bind("<Return>", lambda event: handle_search(entry, search_out))

    # This line starts the graphical loop that is responsible for processing user interactions and showing results
    window.mainloop()


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
                for i in range(1, len(line)+1):
                    if line[:i] not in sub_dict:
                        sub_dict.add(line[:i])
                dictionary.add(line)


def handle_search(entry, search_out):
    """
    :param entry: the words which are inputted by user
    :param search_out: the Text on the window
    """
    search_out.delete('1.0', tk.END)
    text = entry.get()
    lookups = [word.lower() for word in text.split()]  # Handles casing

    # Start to Search
    for i in range(len(lookups)):

        # Load data
        read_dictionary(len(lookups[i]))

        spot_lst = []  # The place where the letters are
        for j in range(len(lookups[i])):
            spot_lst.append(j)

        # Algorithm
        start = time.time()
        count, all_lst = find_anagrams(lookups[i], spot_lst, search_out)
        end = time.time()

        # Showing results on the window
        result = (count + ' anagrams: ')
        for word in all_lst:
            result += word
            if all_lst.index(word) != len(all_lst) - 1:
                result += ', '
            else:
                result += '\n'
        search_out.insert(tk.INSERT, '\n' + lookups[i] + '\n')
        search_out.insert(tk.INSERT, result)

        time_result = 'It took  ' + str(end - start) + '  seconds. \n'
        search_out.insert(tk.INSERT, time_result)

        separator = '_________________________________________________________________________' + '\n' + '\n'
        search_out.insert(tk.INSERT, separator)


def find_anagrams(s, spot_lst, search_out):
    """
    :param s: str, the word which is inputted by user
    :param spot_lst: lst, the place where the letters are
    :param search_out: the Text on the window
    :returns: str, how many results
              lst, all results that user wants
    """
    all_lst = []     # All results that user wants
    count_lst = [0]  # Remember how many results
    search_out.insert(tk.INSERT, 'Searching...' + '\n')
    helper(s, '', all_lst, count_lst, spot_lst, search_out)
    return str(count_lst[0]), all_lst


def helper(s, current_s, all_lst, count_lst, spot_lst, search_out):
    """
    :param s: str, the word which is inputted by user
    :param current_s: str, current string
    :param all_lst: lst, all results that user wants
    :param count_lst: lst, remember how many results
    :param spot_lst: lst, the place where the letters are
    :param search_out: the Text on the window
    """
    if current_s in dictionary:
        # Showing result
        search_out.insert(tk.INSERT, 'Found: ' + current_s + '\n')
        search_out.insert(tk.INSERT, 'Searching...' + '\n')
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
            helper(s, current_s, all_lst, count_lst, spot_lst, search_out)
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
