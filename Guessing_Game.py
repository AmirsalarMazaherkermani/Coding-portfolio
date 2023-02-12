from art import logo
import random

def computer_number():
    print ("Welcom to Guessing Game.\nI am thinking of a number between 1 to 100")
    computer_guess = random.randint(0,100)
    return computer_guess


def user_number():
    print
    user_guess = int(input("Guess a number:\n"))
    return user_guess


def difficulty():
    if input("Choose a difficulty level. easy/hard:\n").lower() == 'easy':
        life = 10
        return life
    else:
        life = 5
        return life


def game():
    print (logo)
    game_over = False
    computer_guess = computer_number()
    # print (computer_guess)
    life = difficulty()
    while not game_over and life > 0:
        print (f"You have {life} guess remaining.")
        user_guess = user_number()
        if user_guess == computer_guess:
            game_over = True
            print ("Correct!")
        elif user_guess > computer_guess:
            print("Too high.")
            life -= 1
            continue
        elif user_guess < computer_guess:
            print("Too low.")
            life -= 1
            continue
    if life == 0:
        print ("You ran out of chances!")
        game_over = True

   
game()
