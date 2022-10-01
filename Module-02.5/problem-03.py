""" rock paper scissor """
player1 = input('Player1: ')
player2 = input('Player2: ')

if player1 == 'rock':
    if player2 == 'paper':
        print('Player 2 is winner')
    elif player2 == 'scissor':
        print('Player 1 is winner')
elif player1 == 'paper':
    if player2 == 'rock':
        print('Player 1 is winner')
    elif player2 == 'scissor':
        print('Player 2 is winner')

elif player1 == 'scissor':
    if player2 == 'rock':
        print('Player 2 is winner')
    elif player2 == 'paper':
        print('Player 1 is winner')