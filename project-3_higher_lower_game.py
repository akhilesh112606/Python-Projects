import resources # WHICH STORES INFORMATION OF LIST AND DESIGNS
import random # FOR RANDOM PICKING 
import os # FOR SCREEN CLEARING

# GLOBAL VARIABLES
score = 0
high = ''
user_choice = ''

choice_A = random.choice(resources.data)

while(user_choice == high):
    print(resources.logo) #PRINTED THE DESIGN
    print(f"Your Score : {score}")
    print(f"Compare A : {choice_A['name']}, {choice_A['description']}, {choice_A['country']}")
    print(resources.vs)

    choice_B = random.choice(resources.data)
    print(f"Against B : {choice_B['name']}, {choice_B['description']}, {choice_B['country']}")
    followers_A = int(choice_A['follower_count'])
    followers_B = int(choice_B['follower_count'])

    if(followers_A >= followers_B):
        high = 'A'
    else:
        high = 'B'
    
    user_choice = input("Who has more followers? Type 'A' or 'B' : ")

    if(user_choice == high):
        score+=1
        choice_A = choice_B
        os.system('cls')
    else:
        print(f"YOU LOST!\nYour Final Score : {score}")
        break