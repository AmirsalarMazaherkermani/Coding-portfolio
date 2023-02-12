import random
#from art import logo
#print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """ to deal random cards """
    return random.choice(cards)

    
def score_cal(cards):
    """ returning the sum of cards and cheching for BlackJack """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """ Comapring different conditions for wining """
    if user_score == 0:
        return "BlackJack! you win"
    elif computer_score == 0:
        return "computer has got a BlackJack and you lose"
    elif user_score > 21:
        return "you went higher than 21!"
    elif computer_score > 21:
        return "computer went higher than 21"
    elif user_score == computer_score :
        return "it's a tie!"
    elif computer_score > user_score:
        return "you lose"
    else:
        return "you win"


def game():    
    is_gamemeover = False
    user_cards = []
    computer_cards = []
    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    if input("Do you want to play BlackJack? 'y'/'n'\n") == "n":
        is_gamemeover = True
    else:
        is_gamemeover = False
    while not is_gamemeover:
        user_score = score_cal(user_cards)
        computer_score = score_cal(computer_cards)    
        print (f"    Your cards: {user_cards}, score: {user_score}\n    Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_gamemeover = True
        else:
            next_round = input("type 'y' for another card and 'n' for pass: ")
            if next_round == 'y':
                user_cards.append(deal_card())
            else:
                is_gamemeover = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = score_cal(computer_cards)
    
    print(compare(user_score, computer_score))
    print(computer_cards, user_cards)


while input("Do you want to play? yes/no ").lower() == 'yes':
    from replit import clear
    clear()
    game()
   
