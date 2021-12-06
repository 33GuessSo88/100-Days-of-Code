import random

print("Welcome to Chris Birchard\'s ROCK PAPER SCISSORS game")

player_choice = input("Pick rock, paper or scissors\n")

computer_list = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer_list)

print(f"player choice is {player_choice}")

print(f"Computer choice is {computer_choice}")

if player_choice == computer_choice:
    print("You TIED!")
elif player_choice == "rock" and computer_choice == "paper":
    print("You WIN!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You LOSE!")
elif player_choice == "paper" and computer_choice == "rock":
    print("You WIN!")
elif player_choice == "paper" and computer_choice == "scissors":
    print("You LOSE!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You WIN!")
elif player_choice == "scissors" and computer_choice == "rock":
    print("You LOSE!")
else:
    print("you typed something wrong")


