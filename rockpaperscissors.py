import numpy as np
import matplotlib as plt
import scipy.special as sp

"""
Practice python code by making a rock paper scissors game
2 Players each choose either rock paper or scissors. 
"""

print('Play rock, paper, scissors, best 2 out of 3 games!\n')#introduce game

p2w = 'Player 2 wins!\n'
p1w = 'Player 1 wins!\n' #results
t = 'It\'s a tie, try again\n'
games = 1   #set game at 0
p1p = 0 #player 1 has 0 points
p2p = 0 #player 2 has 0 points

while games <= 3: #plays 3 games

    print('Game number ' + str(games) + ": ") #game #
    print('Player 1: '+ str(p1p) + '   Player 2: ' + str(p2p))#anounces score
    
    p1 = input('Player 1, choose rock, paper, or scissors: ') #get choices from players
    p2 = input('Player 2, choose rock, paper, or scissors: ')
    
    if p1 == 'rock':   #if player 1 chooses rock 
        if p2 == 'paper':
            print(p2w)
            games = games+1 #adds 1 to games only if someone wins
            p2p = p2p+1 #give player 2 a point
        elif p2 == 'rock':
            print(t) #doesn't add to games if tie
        elif p2 == 'scissors' :
            print(p1w)
            p1p = p1p+1 #give player 1 a point
            games = games+1
        else:
            print('Someone didn\'t answer correctly.\n')
            break #ends game if answer isn't an option
    elif p1 == 'paper':  #if player 1 chooses paper 
        if p2 == 'paper':
            print(t)
        elif p2 == 'rock':
            print(p1w)
            games = games+1
            p1p += 1
        elif p2 == 'scissors' :
            print(p2w)
            games = games+1
            p2p+=1
        else:
            print('Someone didn\'t answer correctly.\n')
            break
    elif p1 == 'scissors':  #if player 1 chooses sissors
        if p2 == 'paper':
            print(p1w)
            games = games+1
            p1p+=1
        elif p2 == 'rock':
            print(p2w)
            games = games+1
            p2p+=1
        elif p2 == 'scissors' :
            print(t)
        else:
            print('Someone didn\'t answer correctly.\n')
    else:
        print('Someone didn\'t answer correctly.\n')
        break
    
print('Game over')#end game

if p1p>p2p:                 #announces winner
    print('Player 1 is the winner!!!\n')
else:
    print('Player 2 is the winner!!!\n')
    

    