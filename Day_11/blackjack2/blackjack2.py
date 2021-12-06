from art import logo
import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(some_cards):
    if sum(some_cards) == 21 and len(some_cards) == 2:
        return 0
    if 11 in some_cards and sum(some_cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(some_cards)

def compare_scores(playersscore, computerscore):
    if playersscore == computerscore:
        return "DRAW!"
    elif computerscore == 0:
        return "Lose, computer has Blackjack"
    elif playersscore == 0:
        return "You win with Blackjack!"
    elif playersscore > 21:
        return "You busted, you lose."
    elif computerscore > 21:
        return "Computer busted, you WIN!"
    elif playersscore > computerscore:
        return "You win!"
    else:
        return "You lose"


    return sum(some_cards)

players_cards = []
computers_cards = []
is_game_over = False

for i in range(2):
    players_cards.append(deal_card())
    computers_cards.append(deal_card())

def play_game():
    is_game_over = False
    while not is_game_over:
        player_score = calculate_score(players_cards)
        computer_score = calculate_score(computers_cards)

        print(f"Your cards are {players_cards} totalling {player_score}")
        print(f"Computer is showing {computers_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            another_player_card = input("Would you like another card? y or n.")
            if another_player_card == 'y':
                players_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal_card())
        computer_score = calculate_score(computers_cards)

    print(f"  Your cards are {players_cards} totalling {player_score}")
    print(f"   Computers cards are {computers_cards} toalling {computer_score}")
    print(compare_scores(player_score, computer_score))
    
while input("Do you want to play Blackjack? y or n") == 'y':
    play_game()

    
