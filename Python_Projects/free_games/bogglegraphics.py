import tkinter as tk

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'  # The file name of the dictionary txt file
LEN = 4                  # The side length

# Global Variables
dictionary = set()       # All words in the dictionary
sub_dict = set()         # Prefix of all words in the dictionary
spot_dict = {}           # Spots' neighbors

all_ans_set = set()      # Answers of the game
guess_set = set()        # User's answers
count_lst = [0]          # Number of the answers
correct_lst = [0]        # Number of user answered correctly


class BoggleGraphics:

    def __init__(self):

        # Create the window
        window = tk.Tk()
        window.wm_attributes('-topmost', 1)  # Let it on the main window
        window.title('Boggle')
        window.geometry('1099x731')
        window.configure(bg='SaddleBrown')

        # Top labels
        header_label = tk.Label(window, text='Boggle', font=('Courier', 40), width=8, height=1,
                                bg='SaddleBrown', fg='white')
        header_label.grid(row=0, column=0, columnspan=2, sticky='nw')

        enter_lst = [None, None, None, None,
                     None, None, None, None,
                     None, None, None, None,
                     None, None, None, None]

        # Row 1
        entry_00 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_00.grid(row=2, column=0, sticky='w', padx=10, pady=10, ipady=20)
        entry_00.focus()
        enter_lst[0] = entry_00

        entry_01 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_01.grid(row=2, column=1, sticky='w', padx=10, pady=10, ipady=20)
        entry_01.focus()
        enter_lst[1] = entry_01

        entry_02 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_02.grid(row=2, column=2, sticky='w', padx=10, pady=10, ipady=20)
        entry_02.focus()
        enter_lst[2] = entry_02

        entry_03 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_03.grid(row=2, column=3, sticky='w', padx=10, pady=10, ipady=20)
        entry_03.focus()
        enter_lst[3] = entry_03

        # Row 2
        entry_10 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_10.grid(row=3, column=0, sticky='w', padx=10, pady=10, ipady=20)
        entry_10.focus()
        enter_lst[4] = entry_10

        entry_11 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_11.grid(row=3, column=1, sticky='w', padx=10, pady=10, ipady=20)
        entry_11.focus()
        enter_lst[5] = entry_11

        entry_12 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_12.grid(row=3, column=2, sticky='w', padx=10, pady=10, ipady=20)
        entry_12.focus()
        enter_lst[6] = entry_12

        entry_13 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_13.grid(row=3, column=3, sticky='w', padx=10, pady=10, ipady=20)
        entry_13.focus()
        enter_lst[7] = entry_13

        # Row 3
        entry_20 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_20.grid(row=4, column=0, sticky='w', padx=10, pady=10, ipady=20)
        entry_20.focus()
        enter_lst[8] = entry_20

        entry_21 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_21.grid(row=4, column=1, sticky='w', padx=10, pady=10, ipady=20)
        entry_21.focus()
        enter_lst[9] = entry_21

        entry_22 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_22.grid(row=4, column=2, sticky='w', padx=10, pady=10, ipady=20)
        entry_22.focus()
        enter_lst[10] = entry_22

        entry_23 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_23.grid(row=4, column=3, sticky='w', padx=10, pady=10, ipady=20)
        entry_23.focus()
        enter_lst[11] = entry_23

        # Row 4
        entry_30 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_30.grid(row=5, column=0, sticky='w', padx=10, pady=10, ipady=20)
        entry_30.focus()
        enter_lst[12] = entry_30

        entry_31 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_31.grid(row=5, column=1, sticky='w', padx=10, pady=10, ipady=20)
        entry_31.focus()
        enter_lst[13] = entry_31

        entry_32 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_32.grid(row=5, column=2, sticky='w', padx=10, pady=10, ipady=20)
        entry_32.focus()
        enter_lst[14] = entry_32

        entry_33 = tk.Entry(window, width=3, borderwidth=2, font=('Courier', 40))
        entry_33.grid(row=5, column=3, sticky='w', padx=10, pady=10, ipady=20)
        entry_33.focus()
        enter_lst[15] = entry_33

        # Description
        description_label = tk.Label(window,
                                     text='1. Please key in letters on your left side.' + '\n' +
                                          '2. Press \'Enter\'. (Cursor must be in any box on the left side.)' + '\n' +
                                          '3. Start to find words!' + '\n' +
                                          '4. Press the bottom button to see all the answers.' + '\n',
                                     font=('Times', 20), height=5, bg='SaddleBrown')
        description_label.grid(row=6, column=0, rowspan=6, columnspan=6, sticky='W')

        # User input
        user_label = tk.Label(window, text="Found : ", font=('Times', 20), bg='SaddleBrown', fg='white')
        user_label.grid(row=1, column=5, sticky='ne')
        user_entry = tk.Entry(window, width=62, name='entry', borderwidth=2)
        user_entry.grid(row=1, column=6, sticky='w')
        user_entry.focus()

        # Result
        result_label = tk.Label(window, text="Result : ", font=('Times', 20), bg='SaddleBrown', fg='white')
        result_label.grid(row=2, column=5, sticky='ne')
        search_out = tk.Text(window, height=26, width=60, borderwidth=2, font=('Times', 18),
                             bg='seashell')
        search_out.grid(row=2, column=6, rowspan=6, padx=10, pady=10, ipady=20, sticky='nw')
        search_out.insert(tk.INSERT, '1. Please type letters on your left side.' + '\n')
        search_out.insert(tk.INSERT, '2. Press \' Enter \'.  (The cursor should be in any box on the left side.)' + '\n')

        # Show answers
        btn = tk.Button(window, text='Show Answers', state=tk.NORMAL, command=lambda: self.show_ans(search_out))
        btn.grid(row=8, column=6)

        # When <return> key is hit in a text field .. connect to the and handle_search() functions to do the work.
        entry_00.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_01.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_02.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_03.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_10.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_11.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_12.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_13.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_20.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_21.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_22.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_23.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_30.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_31.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_32.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))
        entry_33.bind("<Return>", lambda event: self.handle_enter(enter_lst, search_out))

        # When <return> key is hit in a text field .. connect to the and handle_guess() functions to do the work.
        user_entry.bind("<Return>", lambda event: self.handle_guess(user_entry, search_out))

        # This line starts the graphical loop that is responsible for processing user interactions and showing results
        window.mainloop()

    @staticmethod
    def handle_guess(user_entry, search_out):
        guess_set.clear()
        ans_set = all_ans_set.copy()

        search_out.delete('1.0', tk.END)
        text = user_entry.get()
        lookups = [word.lower() for word in text.split()]  # Handles casing

        # Start to Search
        for i in range(len(lookups)):
            if lookups[i] in ans_set:
                search_out.insert(tk.INSERT, lookups[i] + ' : Correct!' + '\n')
                ans_set.remove(lookups[i])
                guess_set.add(lookups[i])
            elif lookups[i] in guess_set:
                search_out.insert(tk.INSERT, lookups[i] + ' : You entered this word repeatedly.' + '\n')
            else:
                search_out.insert(tk.INSERT, lookups[i] + ' : Wrong!' + '\n')
        search_out.insert(tk.INSERT, '\n' + str(len(ans_set)) + ' Left.' + '\n')
        correct_lst[0] = len(guess_set)

    def handle_enter(self, enter_lst, search_out):
        all_ans_set.clear()
        count_lst[0] = 0
        correct_lst[0] = 0

        is_legal = True
        search_out.delete('1.0', tk.END)

        # Load data
        self.read_dictionary()

        # Data: Remember one's neighbors' spots
        for r in range(LEN):
            for c in range(LEN):
                spot = r * LEN + c
                spot_set = set()
                for i in range(-1, 2):  # Control the change of neighbors' x coordinate
                    for j in range(-1, 2):  # Control the change of neighbors' y coordinate
                        if (0 <= r + i < LEN) and (0 <= c + j < LEN) and (r + i) * LEN + c + j != spot:
                            spot_set.add((r + i) * LEN + c + j)
                spot_dict[spot] = spot_set

        # Input
        all_lst = []
        for enter in enter_lst:
            if enter is None:
                search_out.insert(tk.INSERT, 'Illegal input' + '\n')
                is_legal = False
                break
            else:
                text = enter.get()
                if len(text) != 1 or text.isalpha() is False:
                    search_out.insert(tk.INSERT, 'Illegal input' + '\n')
                    is_legal = False
                    break
                else:
                    all_lst.append(text)

        # Letters' spots in all_lst
        spot_lst = []
        for i in range(len(all_lst)):
            spot_lst.append(i)

        # Algorithm
        if is_legal:
            search_out.insert(tk.INSERT, 'Now you can find words and type them in the box above.' + '\n'
                              + '(If you want to type more than one word, please separate it with space.)' + '\n'
                              + '\n' + 'You can also press the bottom button to see all the answers.' + '\n')
            self.find_words(all_lst, spot_lst, search_out)

    def find_words(self, all_lst, spot_lst, search_out):
        self.helper('', all_lst, spot_lst, [], search_out)

    def helper(self, current_s, all_lst, spot_lst, current_spot, search_out):
        if current_s in dictionary:
            all_ans_set.add(current_s)
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
                self.helper(current_s, all_lst, spot_lst, current_spot, search_out)
                # Un-choose
                current_s = current_s[:-1]
                current_spot.pop()
                spot_lst.append(spot)
                spot_lst.sort()

    @staticmethod
    def illegal_input(row_lst):
        if len(row_lst) != LEN:
            return True
        for letter in row_lst:
            if len(letter) > 1 or letter.isalpha() is False:
                return True
        return False

    @ staticmethod
    def read_dictionary():
        """
        This function reads file "dictionary.txt" stored in FILE
        and appends words in each line into a Python list
        """
        with open(FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if 17 > len(line) >= 4:
                    dictionary.add(line)
                    for i in range(1, len(line) + 1):
                        if line[:i] not in sub_dict:
                            sub_dict.add(line[:i])

    @staticmethod
    def show_ans(search_out):
        search_out.insert(tk.INSERT, '\n')
        search_out.insert(tk.INSERT, '__________________________________________')
        search_out.insert(tk.INSERT, '\n' + 'Answers:' + '\n')
        if count_lst[0] == 0:
            search_out.insert(tk.INSERT, 'There are ' + str(count_lst[0]) + ' words in total.' + '\n')
        else:
            for word in all_ans_set:
                search_out.insert(tk.INSERT, '  Found \"' + word + '\"' + '\n')
            search_out.insert(tk.INSERT, '\n')
            search_out.insert(tk.INSERT, 'There are ' + str(count_lst[0]) + ' words in total.' + '\n')
            search_out.insert(tk.INSERT, 'You found ' + str(int(correct_lst[0]/count_lst[0] * 100)) + '% words.' + '\n')
