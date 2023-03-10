""" importing game data"""
from game_data import data
import art
import random


def info(x):
    """ shows the information of each member """
    return (f"{x['name']}, a {x['description']} from {x['country']}")

def random_choice():
    """ creates a random number in the range of the list indices """
    a = random.randint(0, len(data)-1)
    return a
    

def game():
    """ the main function of the game"""
    print (art.logo)
    game_is_over = False
    score = 0
    data1 = data[random_choice()]
    while not game_is_over:
        data2 = data[random_choice()]
        def compare():
            """ compares the followers of the selected members """
            n1 = data1['follower_count']
            n2 = data2['follower_count']
            if n1 > n2:
                return "a"
            else:
                return "b"        
        print (f"Your score is: {score}")
        print (f"Compare A: {info(data1)}")
        print (art.vs)
        print (f"Against B: {info(data2)}")
        answer = input("Type A or B: ").lower()
        if compare() == answer:
            print ("Correct!")
            # print (data1['follower_count'])
            # print (data2['follower_count'])
            score += 1
            data1 = data2
        else:
            print ("Wrong!")
            print (f"Your score is: {score}")
            # print (data1['follower_count'])
            # print (data2['follower_count'])
            game_is_over = True

            
game()
