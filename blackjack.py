import art
import random

def choose_card():
 chosen_card=random.randint(0,12)
 return chosen_card

def calculate_value(chosen_card):

    if chosen_card==0:
        value=11

    elif chosen_card==1:
        value=2

    elif chosen_card==2:
        value=3

    elif chosen_card==3:
        value=4

    elif chosen_card==4:
        value=5

    elif chosen_card==5:
        value=6

    elif chosen_card==6:
        value=7

    elif chosen_card==7:
        value=8

    elif chosen_card==8:
        value=9

    elif chosen_card==9:
        value=10

    elif chosen_card==10:
        value=10

    elif chosen_card==11:
        value=10

    elif chosen_card==12:
        value=10

    return value

def dealer_cards():
    print("\n The dealer's cards are: ")
    dealer_card1=choose_card()
    dealer_card2=choose_card()
    print(art.cards[dealer_card1])
    dealer_val=calculate_value(dealer_card1)+calculate_value(dealer_card2)
    # print(dealer_val)
    return dealer_val

def player_cards():
    print("\nYour cards are: ")
    player_card1=choose_card()
    player_card2=choose_card()
    print(art.cards[player_card1],art.cards[player_card2])
    player_val=calculate_value(player_card1)+calculate_value(player_card2)
    # print(player_val)
    return player_val