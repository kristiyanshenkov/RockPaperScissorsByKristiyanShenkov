import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
players_move = input('Choose [r]ock, [p]aper or [s]cissors: ')

if players_move == 'r':
    players_move = rock
elif players_move == 'p':
    players_move = paper
elif players_move == 's':
    players_move = scissors
else:
    raise SystemExit('Invalid input. Try again...')

computer_random_move = random.randint(1, 3)
computer_move = ''

if computer_random_move == 1:
    computer_move = rock
elif computer_random_move == 2:
    computer_move = paper
else:
    computer_move = scissors
print(f'The computer chose: {computer_move}')
if (players_move == rock and computer_move == scissors) or \
        (players_move == scissors and computer_move == paper) or \
        (players_move == paper and computer_move == rock):
    print('You win!')
elif players_move == computer_move:
    print('Draw!')
else:
    print('You lose!')

