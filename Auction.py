from art import logo
print (logo)
dic = {}
to_continue = True

def find_highest_bid (bidding_list):
    highest_bid = 0
    winner = ''
    for key in bidding_list:
        value = bidding_list[key]
        if value >= highest_bid:
            highest_bid = value
            winner = key
    print (f"The winner is {winner} with a bid of ${highest_bid}")


while to_continue is True:
    name = input("Type your name:\n")
    bid = int(input("What is your bid?\n"))
    dic[name] = bid
    c = input("Is there anyother bider? (yes, no)\n").lower()
    if c == 'yes':
        to_continue = True
    else:
        to_continue = False
print (logo)
#for n in range((len(dic.keys()))):
find_highest_bid(dic)
