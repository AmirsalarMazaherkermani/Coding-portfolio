MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def checking_resources(name):
    """ to check if it is possible to make the requested drink with the resources"""
    drink = MENU[name]
    req_water = drink["ingredients"]["water"]
    req_milk = drink["ingredients"]["milk"]
    req_coffee = drink["ingredients"]["coffee"]
    if resources["water"] < req_water:
        print("Not enough water!")
        return False
    elif resources["milk"] < req_milk:
        print("Not enough milk!")
        return False
    elif resources["coffee"] < req_coffee:
        print("Not enough coffee!")
        return False
    else:
        return True


def money_check():
    """ adding the coins value to a total"""
    print("Please insert coins:")
    quarters = int(input("How many quarters?:\n"))
    dimes = int(input("How many dimes?:\n"))
    nickles = int(input("How many nickles?:\n"))
    pennies = int(input("How many pennies?:\n"))
    tot_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(f"You have inserted ${tot_money}")
    return tot_money


profit = 0
is_over = False
while not is_over:
    rem_water = resources["water"]
    rem_milk = resources["milk"]
    rem_coffee = resources["coffee"]
    demand = input("Please choose your drink (Cappuccino/Latte/Espresso):\n").lower()
    if demand == "off":
        is_over = True
    elif demand == "report":
        print(resources)
    else:
        if not checking_resources(demand):
            is_over = True
        else:
            print(f"price: ${MENU[demand]['cost']}")
            ins_coins = money_check()
            if ins_coins >= float(MENU[demand]["cost"]):
                change = round((ins_coins - float(MENU[demand]["cost"])), 2)
                profit += ins_coins - change
                if ins_coins > float(MENU[demand]["cost"]):
                    print(f"Your change is: {change}\nDon't forget to take your change!")
                rem_water = resources["water"] - MENU[demand]["ingredients"]["water"]
                rem_milk = resources["milk"] - MENU[demand]["ingredients"]["milk"]
                rem_coffee = resources["coffee"] - MENU[demand]["ingredients"]["coffee"]
                resources["water"] = rem_water
                resources["milk"] = rem_milk
                resources["coffee"] = rem_coffee
                print(f"Here is your {demand}, please enjoy your drink and thank you for using our services!")
            else:
                print("Not enough. Please take your coins.")
               
