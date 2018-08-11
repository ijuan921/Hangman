from random import randint,choice
import json

def pick_word():
    with open("words.json") as file:
        words = json.load(file)
    return choice(words).upper()

def hangman(index):
    hangman_art = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''    
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+  
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    return hangman_art[index]

def save_letter(lst, letter):
    for count, value in enumerate(lst[0]):
        if value == letter:
            lst[1][count] = letter

def check_letter():
    wrong = 0
    word = pick_word()
    board_shape = "_"
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    guessed_letters = set()
    game_list = [[m.strip(' ') for m in word], [board_shape for _ in word]]

    while wrong < 7:
        print(hangman(wrong))
        print(" ".join(game_list[1]))
        letter = str(input("Guess a letter: ")).capitalize()

        if letter in letters:
            if letter in guessed_letters:
                print("\nAlready guessed that letter!")
            elif letter in set(game_list[0]):
                save_letter(game_list, letter)
            else:
                wrong += 1
            guessed_letters.add(letter)

        if '_' not in game_list[1]:
            print(hangman(wrong))
            print("\nYou guessed the word %s correctly!" % word)
            break
        elif wrong == 6:
            print(hangman(wrong))
            print("\nYou've lost! The word was %s." % word)
            break

if __name__ == '__main__':
    print("Welcome to Hangman!")
    check_letter()

    while True:
        user_choice = input("Do you wish to play again?\n>>>").capitalize()

        if user_choice == "Yes":
            check_letter()
        elif user_choice == "No":
            break