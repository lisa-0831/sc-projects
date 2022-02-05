"""
File: hangman.py
Name: PEI-WEN(Lisa) WANG
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The player has N_TURN chances to guess the word that is decided by a random function.
    If the player guesses the right one, then the dashed will show the right place where the alphabet is.
    If the player guesses a wrong one, then the player will lose a chance to guess.
    The player needs to re-enter again if he/she entered a number or alphabets.
    The player will see the hangman every step it takes. Before the last six chances, the rope will become longer
    when the player entered a wrong alphabet.
    """
    answer = random_word()
    dashed = produce_dashed(answer)
    chance = N_TURNS
    count = 0  # counting how many times the player guesses a wrong one
    while True:
        if still_alive(dashed, chance) is True:
            print('The word looks like: ' + dashed)
            print('You have ' + str(chance) + ' guesses left.')
            while True:
                guess = input('Your guess: ').upper()
                if guess.isalpha() is True and len(guess) == 1:
                    break
                else:
                    print('illegal format.')
            if answer.find(guess) != -1:  # guessed a right one
                print('You are correct!')
                dashed = update_dashed(answer, dashed, guess)
            else:  # guessed a wrong one
                print('There is no ' + guess + '\'s in the word.')
                chance -= 1

        elif chance == 0:  # the player loses
            print('You are completely hung.' + chr(128520))
            break

        else:  # the player wins
            print('You win!!' + chr(128519))
            break

        count = show_hangman(chance, count)  # show the hangman

    print('The word was: ' + answer)


def show_hangman(chance, count):
    """
    :param chance: int, to check the step of drawing the hangman
    :param count: int, to remember how many times the player guessed wrongly
    :return: count, updated how many times the player guessed wrongly
    """

    print('-------')
    if chance != N_TURNS and chance >= 7:
        for i in range(N_TURNS - chance):
            print('  | ')
        count += 1
    elif chance != N_TURNS and chance < 7:
        for i in range(count):
            print('  | ')

    if chance <= 7:
        step = 7 - chance
        for i in range(step):
            if i == 0:
                print('  | ')
            elif i == 1:  # head
                print('  ' + chr(128556) + ' ')
            elif i == 2 or i == 5:  # arm and leg
                print(' /', end='')
            elif i == 3:  # body
                print(chr(128087), end='')
            elif i == 4:  # arm
                print('\\')
            elif i == 6:  # leg
                print(' \\')
    print('')
    print('-------')
    print('')
    return count


def produce_dashed(answer):
    """
    :param answer: str, counting the length of the answer and producing dashed
    :return: str, the dashed
    """
    dashed = ''
    for i in range(len(answer)):
        dashed += '-'
    return dashed


def still_alive(dashed, chance):
    """
    :param dashed: str, to check if there is '-' in dashed
    :param chance: str, to check if the player still has chances
    :return: boolean, make sure the player can still guess the word
    """
    if dashed.find('-') != -1:  # still have alphabet to guess
        if chance > 0:  # still have chances to guess
            return True
    return False


def update_dashed(answer, dashed, guess):
    """
    :param answer: str, to check if the player guessed a right one
    :param dashed: str, to update and show the alphabet that was guessed by the player
    :param guess: str, to match if there is the same alphabet in the answer
    :return: str, the new dashed that be updated
    """
    new_dashed = ''
    for i in range(len(answer)):
        if guess == answer[i]:
            new_dashed += answer[i]
        else:
            new_dashed += dashed[i]
    return new_dashed


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
