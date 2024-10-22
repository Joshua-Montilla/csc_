from pathlib import Path
import random
import pygame
# By Jadrian M & Joshua M
# Initialize pygame and the mixer
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)

filename = "/Users/joshuamontilla/Downloads/MusicBox.mp3"
pygame.mixer.music.load(filename)
pygame.mixer.music.play(-1)

def get_word():
    with open("Code Jam/words.txt", 'r') as file:
        wordlist = file.read().splitlines("\n")
    word = random.choice(wordlist).lower()
    return word

def get_letters(word):
    letters = []
    temp = '_' * len(word)
    if word == " ":
        word.replace(" ", "")
    
    for char in list(word):
        if char not in letters:
            letters.append(char)
    character = " "

    for num, char in enumerate(list(word)):
        if char == character:
            templist = list(temp)
            templist[num] = char
            temp = ''.join(templist)
    return temp

def draw_man(chances):
    stages = [
        "\n  __\n /  |\n|   |\n|\n|\n|\n_ _ _ _ _",    # 6 chances left
        "  __\n /  |\n|   |\n|   o\n|\n|\n_ _ _ _ _",  # 5 chances left
        "  __\n /  |\n|   |\n|   o\n|   |\n|\n_ _ _ _ _",  # 4 chances left
        "  __\n /  |\n|   |\n|  \\o\n|   |\n|\n_ _ _ _ _",  # 3 chances left
        "  __\n /  |\n|   |\n|  \\o/\n|   |\n|\n_ _ _ _ _",  # 2 chances left
        "  __\n /  |\n|   |\n|  \\o/\n|   |\n|  |\n_ _ _ _ _",  # 1 chance left
        "  __\n /  |\n|   |\n|  \\o/\n|   |\n|  | |\n_ _ _ _ _",  # 0 chances left
    ]
    print(stages[6 - chances])

def start_game():
    word = get_word()
    temp = get_letters(word)
    chances = 6
    found = False
    draw_man(chances)
    active = True
    while active:
        if chances == 0:
            print("Game over\nWord: "+(word.title()))
            break

        print("\n=== Guess the word ===")
        print(temp, end='')
        print("\nLength = " + str(len(temp)))
        print("\nGuesses: "+ str(chances))
        guessed = []
        character = input("Enter letter (or type 'quit' to exit): ").lower()
        if character == "quit":
            print("Goodbye.")
            break

        if len(character) != 1 or not character.isalpha():
            print("Only one letter at a time.")
            continue

        if character in guessed:
            print("You already entered: " + character)
            continue
        
        
        if character in word:
            for num, char in enumerate(list(word)):
                if char == character:
                    templist = list(temp)
                    templist[num] = char
                    temp = ''.join(templist)
                    found = True
                    guessed.append(character)
        elif found == True:
            found = False
        else:
            chances -= 1
        
        if '_' not in temp:
            print("\nWinner! \nWord is: " + word.title())
            print(f"Tries: {6 - chances}")
            break
        
        draw_man(chances)

while True:
    entry = input("Welcome user, would you like to play Hangman? (Y)es/(N)o: ").strip().lower()
    if entry == "y":
        start_game()
    elif entry == "n":
        print("Goodbye.")
        break
    else:
        print("Invalid entry.")
    print("\n")
