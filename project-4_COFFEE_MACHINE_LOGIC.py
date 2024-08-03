MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0
}

while 1:
    choice = input("What would you like to have? (espresso, latte, cappuccino)").lower()
    if choice == 'report':
        for key in resources:
            print(f"{key} : {resources[key]}")
        continue

    elif choice == 'no':
        break

    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        count = 1
        for materials in MENU[choice]["ingredients"]:
            if MENU[choice]["ingredients"][materials] >= resources[materials]:
                print(f"Sorry there is not enough {materials}")
                count = 0
                break

        if count == 0:
            continue

        # MONEY RELATED MATTER CODE IS BELOW
        print("Insert the coins.")
        quarters = float(0.25*int(input("How many quarters : ")))
        dimes = float(0.10 * int(input("How many dimes : ")))
        nickles = float(0.05 * int(input("How many nickles : ")))
        pennies = float(0.01 * int(input("How many pennies : ")))

        user_total_amount = float(quarters + dimes + nickles + pennies)

        if user_total_amount < MENU[choice]['cost']:
            print('Insufficient Amount!')
            print(f"Refund : {user_total_amount}")

        elif user_total_amount >= MENU[choice]['cost']:
            change = user_total_amount - MENU[choice]['cost']
            print(f"Here is {change}$ in change!")
            user_total_amount -= change
            resources['money'] += user_total_amount

            for materials in MENU[choice]['ingredients']:
                resources[materials] -= MENU[choice]['ingredients'][materials]

            print(f"Here is your {choice}, ENJOY!")
            continue

    else:
        print("Invalid Option, choose AGAIN!")
        continue

print('Thanks for Using our Coffee Machine.')
