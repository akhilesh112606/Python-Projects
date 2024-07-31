import random

# DECLARING THE GLOBAL VARIABLES
number_to_guess = random.randint(1,100)
number_of_attempts = 0

print("Welcome to the number guessing game!\nI'm thinking of a number between 1 to 100.")
choice = (input("Choose a difficulty. Type 'EASY' or 'HARD' : ")).upper()

if choice == 'EASY':
    number_of_attempts = 10

elif choice == 'HARD':
    number_of_attempts = 5

else:
    print("Invalid CHOICE!")
    exit(0)

while(number_of_attempts>0):
    print(f"You have {number_of_attempts} attmpets to guess the number.")
    user_guess = int(input("Enter your Guess : "))
    number_of_attempts-=1

    if user_guess == number_to_guess:
        print(f"YOU GUESSED THE NUMBER!")
        exit(0)
    
    elif user_guess > number_to_guess:
        print("Too HIGH, Guess again.")

    elif user_guess < number_to_guess:
        print("Too LOW, Guess again.")
    
    print('\n')

print("YOU LOST!, Unable to Guess")

