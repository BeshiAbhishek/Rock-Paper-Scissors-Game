# Hello and welcome to Rock-Paper-Scissors Game 

import random

your_Choice = input('Select one from Rock, Paper, Scissor: ')
print(f"Your choice is {your_Choice}")
options = ['rock','paper','scissor']
comp_select = random.choice(options)
print(f"The System choice is: {comp_select}")
count_user = 0
count_system = 0

if your_Choice == 'Rock':
    if comp_select == 'rock':
        print('Tie')
    elif comp_select == 'paper':
        count_system += 1
    else:
        count_user += 1
elif your_Choice == 'Paper':
    if comp_select == 'rock':
        count_user+=1
    elif comp_select == 'paper':
        print('Tie')
    else:
        count_system += 1
elif your_Choice == 'Scissor':
    if comp_select == 'rock':
        count_system+=1
    elif comp_select == 'Scissor':
        print('Tie')
    else:
        count_user += 1
    
print(f'System Score is {count_system}')
print(f'User Score is {count_user}')

if count_user>count_system:
    print('Hey! You won... Keep Playing')
else:
    print("System won.... Why don't you try again")




