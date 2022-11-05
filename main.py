import random
from game_data import data
from art import logo, vs
from replit import clear

#get details of the list
def get_details(which_list):
    '''Pull the name, description and country from the list'''
    name = which_list.get('name')
    description = which_list.get('description')
    country = which_list.get('country')
    return(f"{name}, {description}, {country}")

def higher_lower():   
    playing = True
    current_score = 1
    a = []
    b = []
    
    while playing:
        #select two random items to compare from the data list
        a_b_choices = random.sample(data, 2)
        if len(a) == 0:
            a = a_b_choices[0]
        b = a_b_choices[1]
        #if you already have an a list available from playing, use that value
        #print out the A list for comparison
        print(logo)
        print(f"Compare A: {get_details(a)}")
        print(vs)
        print(f"Against B: {get_details(b)}")
    
        #decide which is higher
        selection = input("Who has more followers?  Type 'A' or 'B': ")
        clear()
        #create empty lists to shift A and B
        if selection == 'A':
            if a.get('follower_count') > b.get('follower_count'):
                current_score += 1
                print(f"You're right!, your current score is {current_score}")
            if a.get('follower_count') < b.get('follower_count'):
                current_score -=1
                print(f"Sorry, that's wrong.  Final score: {current_score}")
                playing = False
        if selection == 'B':
            if b.get('follower_count') > a.get('follower_count'):
                current_score += 1
                print(f"You're right!, your current score is {current_score}")
            if b.get('follower_count') < a.get('follower_count'):
                current_score -=1
                print(f"Sorry, that's wrong.  Final score: {current_score}")
                playing = False
    
higher_lower()