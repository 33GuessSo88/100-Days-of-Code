############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
# If dealer has < 17 they must take a card

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = random.choices(cards, k = 2)
print(player_cards)
player_total = sum(player_cards)

computer_cards = random.choices(cards, k = 2)
print(computer_cards)
computer_total = sum(computer_cards)

print(f"Your cards: {player_cards} ---- current total: {player_total}")
print(f"Computer's first card: {player_cards[0]}\n")

def check_for_winner():
    if computer_total > 21:
        print("Computer BUSTS!\n YOU WIN!!")
    elif player_total > 21:
        print("YOU BUSTED!\n YOU LOSE!!")
    elif computer_total > player_total:
        print(f"Your cards: {player_cards} ---- current total: {player_total}")
        print(f"Computer's cards: {computer_cards} ---- current total: {computer_total}")
        print("YOU LOSE")
    elif computer_total == player_total:
        print(f"You have {player_total} and computer has {computer_total}.")
        print("It's a DRAW.")
    else:
        print("YOU WIN!")
        print(f"You have {player_cards} and computer has {computer_cards}")
        print(f"{player_total} vs {computer_total}")

another_card = input("Would you like another card? y or n ")

while another_card == 'y':
    player_cards.append(random.choice(cards))
    player_total = sum(player_cards)
    if player_total > 21:
        if 11 in player_cards:
            index = player_cards.index(11)
            player_cards[index] = 1
        else:
            check_for_winner()
            another_card = 'n'
    else:
        print(f"You have {player_cards} for a total of {player_total}.\n")
        another_card = input("Would you like another card? y or n ")

while computer_total < 17:
    print(f"Computer has {computer_cards} for {computer_total} and takes another card.\n ")
    computer_cards.append(random.choice(cards))
    computer_total = sum(computer_cards)

    
print("Thank you for playing Blackjack")

