# Rock Paper Scissors3

import random, time

choiceQ = '''\nRock Paper or Scissors
Type 1 for rock
Type 2 for paper
Type 3 for scissors
'''
options = ['rock', 'paper', 'scissors']

intChoice = 12

def countdown(seconds):
    for i in range(3):
        print(options[i])
        time.sleep(seconds)

playAgain = 'play'

while playAgain == 'play':
    choice = int(input(choiceQ))
    print(choice)
    computerChoice = random.randint(1,3)

    while not choice in range(1, 4):
        print('You may have not picked a number, pick again.\n')
        choice = int(input(choiceQ))

    while choice == computerChoice:
        print('You picked the same as CPU, pick again')
        computerChoice = random.randint(1,3)
        choice = int(input(choiceQ)) 

    countdown(1)

    if choice == computerChoice - 1 or int(choice) == 3 and int(computerChoice) == 1:
        print('\nCPU picked', options[computerChoice - 1], 'you lose')
    elif choice == computerChoice + 1 or choice == 1 and computerChoice == 3:
        print('\nCPU picked', options[computerChoice - 1], 'you win')

    time.sleep(2)

    playAgain = str.lower(input('\nDo you want to play again?\n'
                                'type \'play\' to play again, press any other key to quit.\n'))
    
    
    
    
