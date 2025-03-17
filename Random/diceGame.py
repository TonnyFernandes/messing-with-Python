from random import randint as rd

def tossDie():
    return rd(1, 6)

player1score = 0
player2score = 0

t = int(input('Type how many rounds you want to play: '))

for x in range(t):
    print('Round {}:'.format(x+1))
    die = tossDie()
    player1score += die
    print('\tPlayer 1 die: {}'.format(die))
    print('\t\tTotal score: {}'.format(player1score))

    die = tossDie()
    player2score += die
    print('\tPlayer 2 die: {}'.format(die))
    print('\t\tTotal score: {}'.format(player2score))

    print('')

if player1score == player2score:
    print('We have a tie, both players scored {}'.format(player1score))
elif player1score > player2score:
    print('Player 1 wins with {} points!'.format(player1score))
    print('Player 2 lost with {}'.format(player2score))
else:
    print('Player 2 wins with {} points!'.format(player2score))
    print('Player 1 lost with {}'.format(player1score))
