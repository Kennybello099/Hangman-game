import sys
import random
import time

name = input("Enter your name: ")


def mainmenu():
    print('welcome ' + name)
    print("1. play game")
    print("2. instruction")
    print("3. exitprogram")
    time.sleep(1)

    def easy_game():
        states = ['Lagos', 'Oyo', 'Ogun',  'Kaduna',  'Plateau', 'Porthacourt', 'Nassarawa', 'Cross river', ]
        wordkey = random.choice(states)
        dash_char = len(wordkey)
        turns = 3


        while 1:
            print(dash_char * "_ ")

            guesses = input("Guess a state in Nigeria: ")

            if guesses == wordkey:
                print("You won")
                print("The word is:", wordkey)
                ans = input('Do you want to play again[yes/no]?')
                if ans.lower() == 'yes':
                    game_menu()
                else:
                    if ans.lower() == 'no':
                        exit()
            else:
                if guesses != wordkey:
                    turns -= 1
                    print("wrong")
                    print("You have", + turns, "more guesses")


                    if turns == 0:
                        print("You Loose")

    def difficult_game():
        country = ['Nigeria', 'Ghana', 'Gambia', 'Burkinafaso', 'Togo', 'Zimbabwe']
        wordkey = random.choice(country)
        dash_char = len(wordkey)

        turns = 3

        while turns > 0:
            print(dash_char * "_ ")


            guesses = input("Guess a Country in AFrica: ")

            if guesses == wordkey:
                print("You won")
                print("The word is:", wordkey)
                ans = input('Do you want to play again[yes/no]?')
                if ans.lower() == 'yes':
                    game_menu()
                else:
                    if ans.lower() == 'no':
                        exit()
            else:
                if guesses != wordkey:
                    turns -= 1
                    print("wrong")
                    print("You have", + turns, "more guesses")
                    if turns == 0:
                        print("You Loose")


    def instruction():
        noted = 'You must begin the first letter with a capital letter.\nFor easy level the words are within' \
                ' 3-11 letters\nwhile for difficult level,the words are within 4 - 11 letters'
        print(noted)
        time.sleep(1)
        return mainmenu()

    def continue_program():
        return mainmenu()

    def exit():
        ans = input('Quit the program[yes/no]? ')
        if ans.lower() == 'yes':
            sys.exit()
            exit()
        else:
            if ans.lower() == 'no':
                continue_program()

    def game_menu():
        if choice == 1:
            print("Game level")
            print("1. easy")
            print("2. difficult")

            level = int(input("Enter a level: "))

            if level == 1:
                print('Hello', name + ' time to play hangman!')
                print("The dashes represent the no of characters.")
                print("start guessing...")
                time.sleep(0.5)
                easy_game()

            elif level == 2:
                print('Hello', name + 'time to play hangman!')
                print("The dashes represent the no of characters.")
                print("start guessing...")
                time.sleep(0.5)
                difficult_game()
            else:
                print("out of range")

            ans = input('Do you want to play again[yes/no]?')
            if ans.lower() == 'yes':
                game_menu()
            else:
                if ans.lower() == 'no':
                    exit()

        elif choice == 2:
            instruction()

        elif choice == 3:
            exit()
        else:
            print("Out of range")

    choice = int(input("Enter number[1-3]: "))
    game_menu()


mainmenu()
