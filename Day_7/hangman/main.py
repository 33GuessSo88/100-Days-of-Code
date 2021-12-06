

import random
from os import system, name
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

def clear():
    if name == 'nt':
        _ = system('cls')

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")
#print(display)

end_of_game = False
lives = 6
all_guesses = []

while not end_of_game:   
    guess = input("Guess a letter\n").lower()
    all_guesses.append(guess)
    position = 0
    if guess in all_guesses:
        print("you've already guessed that letter.")
    for letter in chosen_word:
        if guess == letter:
            display[position] = letter
        position += 1

    if guess not in chosen_word:
        lives -= 1
        print(f"you have {lives} lives")
        print(stages[lives])
        
    print(' '.join([str(elem) for elem in display]))
    print(' '.join([str(elem) for elem in all_guesses]))

    if lives == 0:
        end_of_game = True
        print("you lose")
        print(f"the word was {chosen_word}.")

    if "_" not in display: 
        end_of_game = True
        print("you win!")
        print(display)
    

