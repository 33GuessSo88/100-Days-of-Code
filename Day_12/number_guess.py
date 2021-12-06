import random

#Set a global variable so it's easy to change these values in the future.
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Instead of setting difficulty in play_game(), better to create function
#The key here is to RETURN the number of guesses and then call it later
def set_difficulty():
    """returns the number of guesses based on difficulty chosen"""
    level = input("Would you like to play easy or hard? ")
    if level == "hard":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS

def play_again():
    """Checks to see if you would like to play again, if not thanks you for playing and ends game"""
    another_game = input("Would you like to play again? ")
    if another_game == 'y':
        play_game()
    else:
        print("Thank you for playing")
        
def play_game():
    game_over = False
    num_guesses = set_difficulty() #This is critical learning, call the funtion to set the variable
    number = random.randint(1, 100)
    guess = 0

    while game_over == False:
        if num_guesses <1:
            print("You have no guesses left. GAME OVER.")
            play_again()
            game_over = True #I could use a return here and just jump out of the while loop
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

print("Welcome to the Number Guessing Game!")
play_game()

