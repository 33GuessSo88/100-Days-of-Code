from art import logo, vs
from game_data import data
import random
import os

#TODO the second choice becomes first, pick a new second choice, compare
def compare_followers(players_guess, choiceA_num, choiceB_num):
    """returns False if player wins, True if player"""
    if players_guess == 'A' and choiceA_num > choiceB_num:
        return False
    if players_guess == 'B' and choiceB_num > choiceA_num:
        return False
    else:
        return True

def new_choices(x):
    """returns a list of the old B choice and a new A choice"""
    choiceA = x
    while choiceA == x:
            x = random.sample(data, 1)
            x = x[0]
    new_choices_list = [choiceA, x]
    return new_choices_list

#TODO pick 2 random instagram accounts
choices1 = random.sample(data, 2)
game_over = False
score = 0

while game_over == False:
    choiceA = choices1[0]
    choiceB = choices1[1]

    #TODO print the choices for the player
    print(logo)
    print(f"Compare A: {choiceA['name']}, a {choiceA['description']}, from {choiceA['country']}.")
    print(vs)
    print(f"Compare B: {choiceB['name']}, a {choiceB['description']}, from {choiceB['country']}.")
    players_guess = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    #print(f"players guess is {players_guess}")
    choiceA_num = choiceA['follower_count']
    choiceB_num = choiceB['follower_count']        
    #print(f"choice A is {choiceA_num} of followers")
    #print(f"choice B is {choiceB_num} of followers")

    #TODO compare players choice to other choice and find higher
    game_over = compare_followers(players_guess, choiceA_num, choiceB_num)
    if game_over == False:
        score += 1
        os.system('CLS')
        print(f"You're right! Your score is {score}.")
        choices1 = new_choices(choiceB)
        
    else:
        print(f"Sorry, that's wrong. Final score: {score}")


        