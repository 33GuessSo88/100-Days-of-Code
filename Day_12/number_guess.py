import random


def play_again():
    """Checks to see if you would like to play again, if not thanks you for playing and ends game"""
    another_game = input("Would you like to play again? ")
    if another_game == 'y':
        play_game()
    else:
        print("Thank you for playing")
        
def play_game():
    game_over = False
    num_guesses = 0
    level = input("Would you like to play easy or hard? ")
    if level == "hard":
        num_guesses = 5
    else:
        num_guesses = 10

    number = random.choice(range(1, 100))
    guess = 0

    while game_over == False:
        if num_guesses <1:
            print("You have no guesses left. ")
            play_again()
            game_over = True
        else:
            print(f"You have {num_guesses} guesses left. ")
            guess = int(input("Please guess a number between 1 and 100. "))
            if guess == number:
                print("You WIN!")
                play_again()
                game_over = True
            elif guess > number:
                print("Too high, please guess again.")
            else:
                print("Too low, please guess agian. ")
            num_guesses -= 1

play_game()





#TODO find ascii art

