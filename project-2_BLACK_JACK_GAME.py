import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
computer_cards = []
dictionary = {'User' : user_cards, 'Computer' : computer_cards}

# TEMPORARY FUNCTIONS
def Eleven_To_One(temp_list):
    for temp_num in temp_list:
        if(temp_num == 11):
            index = temp_list.index(11)
            temp_list[index] = 1
            return True
            
        else:
            return False

def Random_Card_Selector():
    index = random.randint(0,12)
    return cards[index]
    
def Proper_Sum_Checker(temp_list):
    total = sum(temp_list)
    if total>21:
        return False
    else:
        return True

while True:
    temp = 0
    decision = input("Do you want to play the game of the BlackJack? Type 'y' or 'n'")
    if decision == 'n':
        break
    elif decision == 'y':
        card = Random_Card_Selector()
        dictionary['User'].append(card)
        card = Random_Card_Selector()
        dictionary['User'].append(card)
        card = Random_Card_Selector()
        dictionary['Computer'].append(card)
    
        print(f"Your Cards : {dictionary['User']}")
        print(f"Computer first Card : {card}")
        
        # Here the code is for the user Part
        while True:

            card_decision = input("Type y to pic and n to pass : ")
            if(card_decision == 'y'):
                card = Random_Card_Selector()
                dictionary['User'].append(card)
                if not(Proper_Sum_Checker(user_cards)):
                    if(Eleven_To_One(user_cards)):
                        print(f"Your Cards : {dictionary['User']}")
                    else:
                        temp = 1
                        break
                else:
                    print(f"Your Cards : {dictionary['User']}")
                        
            elif(card_decision == 'n'):
                break
                
                
        print(f"Your Final Hand : {dictionary['User']}")
        if temp == 1:
            card = Random_Card_Selector()
            dictionary['Computer'].append(card)
            print(f"Computer's Final Hand : {dictionary['Computer']}")
            print("Computer WIN!")
            
        else:
            while True:
                card = Random_Card_Selector()
                dictionary['Computer'].append(card)
                
                if(Proper_Sum_Checker(computer_cards)):
                    if(sum(computer_cards) > sum(user_cards)):
                        print(f"Computer's Final Hand : {dictionary['Computer']}")
                        print("Computer WIN!")
                        break
                        
                else:
                    if not(Eleven_To_One(computer_cards)):
                        print(f"Computer's Final Hand : {dictionary['Computer']}")
                        print("You WIN!")
                        break
        
        
print('Thanks for Coming!')