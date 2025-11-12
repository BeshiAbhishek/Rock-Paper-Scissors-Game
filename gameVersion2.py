# 🎮 Rock-Paper-Scissors — Version 2 (Best of 5 Rounds)
# In this version, the player and the system compete for 5 rounds.
# Whoever scores higher after 5 rounds wins!

import random

print('Welcome to Rock-Paper-Scissors 🎮 (Best of 5)')

options = ['rock', 'paper', 'scissor']
user_score = 0
system_score = 0
rounds = 0  # start from 0

while rounds < 5:
    your_choice = input('\nSelect one from Rock, Paper, Scissor: ').lower()
    system_choice = random.choice(options)
    rounds += 1

    match your_choice:
        case 'rock':
            if system_choice == 'rock':
                print('🤝 Tie')
            elif system_choice == 'paper':
                system_score += 1
                print('🖥️ System wins this round!')
            else:
                user_score += 1
                print('🙆🏼 You win this round!')

        case 'paper':
            if system_choice == 'rock':
                user_score += 1
                print('🙆🏼 You win this round!')
            elif system_choice == 'paper':
                print('🤝 Tie')
            else:
                system_score += 1
                print('🖥️ System wins this round!')

        case 'scissor':
            if system_choice == 'rock':
                system_score += 1
                print('🖥️ System wins this round!')
            elif system_choice == 'scissor':
                print('🤝 Tie')
            else:
                user_score += 1
                print('🙆🏼 You win this round!')

        case _:
            print('⚠️ Invalid choice! Please select Rock, Paper, or Scissor.')
            rounds -= 1  # don’t count invalid attempt
            continue

    print(f'🙆🏼 Your choice: {your_choice}')
    print(f'🖥️ System choice: {system_choice}')
    print(f'📊 Current Score → You: {user_score} | SyPapstem: {system_score}')

# 🏁 Final result
print('\nFinal Scores:')
print(f'🙆🏼 You: {user_score}')
print(f'🖥️ System: {system_score}')

if user_score > system_score:
    print("🏆 You’re the Champion! Well played!")
elif system_score > user_score:
    print("💻 System wins the game. Better luck next time!")
else:
    print("🤝 It’s a tie overall!")