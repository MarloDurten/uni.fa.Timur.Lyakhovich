import random
from random import randint
import os

GameNums_2D = [ [randint(1, 9) for j in [[]] * 3 ] for i in [[]] * 3 ] # creating 3x3 field with random nums in it
score = [0,0]   # [0] - first player score, [1] - second player score
turn_counter = 1    # turn counter
prev_move = [-1,-1]

# func to clear console
def clearConsole():
    # to-do :D
    pass

# func to display field in the console
def gamefield_gen_2D(GameNums_2D, turn_counter, score):
    print(f'\nTurn {turn_counter}. First Player Score: {score[0]}. Second Player Score: {score[1]}.\n')
    for i in GameNums_2D:
        for j in i:
            print(f'   {j}', end = '   ')
        print('\n')

# func to convert given array of strings to array of ints and to check if the given coords are proper (between 1 and 3)
def convertDotCoordsToInt(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
        if arr[i] < 1 or arr[i] > 3:
            return(0)
    return(arr)
    

# func to check if there is move left for the the First Player
def isTherePossibleMoveLeftFP(GameNums_2D, prev_move):
    for i in GameNums_2D[prev_move[1]-1]:
        if i != '': return True
    return False

# func to check if there is move left for the the Second Player
def isTherePossibleMoveLeftSP(GameNums_2D, prev_move):
    column = [row[prev_move[0]-1] for row in GameNums_2D]
    for i in column:
        if i != '': return True
    return False

# func to make Player 1 move
def FirstPlayerMove(turn_counter, score, prev_move):
    
    if isTherePossibleMoveLeftFP(GameNums_2D, prev_move) == False and (prev_move[0] == -1 and prev_move[1] == -1):
        print('There is no moves left for First Player, so Second Player keeps on cooking')
        turn_counter+=1
        clearConsole()
        SecondPlayerMove(turn_counter, score, prev_move)
        
    chosenDot = []

    print('First Player Move (column, row): ', end='')
    chosenDot = str(input()).split()
        
    if convertDotCoordsToInt(chosenDot) == 0:
        print('     !!! Incorrect dot coordinats input')
        clearConsole()
        FirstPlayerMove(turn_counter, score, prev_move)
        
    else:
        if prev_move[0] == -1 and prev_move[1] == -1:
            # the first move ever
            prev_move = chosenDot
            score[0] += GameNums_2D[chosenDot[1]-1][chosenDot[0]-1]
            GameNums_2D[chosenDot[1]-1][chosenDot[0]-1] = ''
            
        else:
            if chosenDot[1] == prev_move[1]:    # if the move is being made in the same row as the previous one
                if GameNums_2D[chosenDot[1]-1][chosenDot[0]-1] == '':    # if the move was already made before ('' means not avaliable)
                    print('     !!! You are trying to choose already made before move')
                    clearConsole()
                    FirstPlayerMove(turn_counter, score, prev_move)
                else:
                    prev_move = chosenDot
                    score[0] += GameNums_2D[chosenDot[1]-1][chosenDot[0]-1]
                    GameNums_2D[chosenDot[1]-1][chosenDot[0]-1] = ''
                
            else:
                print('     !!! Gotta make move in the same ROW as the first player')
                clearConsole()
                FirstPlayerMove(turn_counter, score, prev_move)
        
        print(f'\nFirst Player Move is: {chosenDot}({GameNums_2D[chosenDot[1]-1][chosenDot[0]-1]}). It makes their score: {score[0]}', end='')
        turn_counter+=1
        clearConsole()
        main(turn_counter, score, prev_move)


# func to make Player 2 move
def SecondPlayerMove(turn_counter, score, prev_move):
    
    if isTherePossibleMoveLeftSP(GameNums_2D, prev_move) == False:
        print('There is no moves left for Second Player, so First Player keeps on cooking')
        turn_counter+=1
        clearConsole()
        FirstPlayerMove(turn_counter, score, prev_move)
        
    chosenDot = []
    
    print('Second Player Move: ', end='')
    chosenDot = str(input()).split()
        
    if convertDotCoordsToInt(chosenDot) == 0:
        print('     !!! Incorrect dot coordinats input')
        clearConsole()
        SecondPlayerMove(turn_counter, score, prev_move)
        
    else:
        if chosenDot[0] == prev_move[0]:    # if the move is being made in the same column as the previous one
            if GameNums_2D[chosenDot[1]-1][chosenDot[0]-1] == '':    # if the move was already made before ('' means not avaliable)
                print('     !!! You are trying to choose already made before move')
                clearConsole()
                SecondPlayerMove(turn_counter, score, prev_move)
            else:
                prev_move = chosenDot
                score[1] += GameNums_2D[chosenDot[1]-1][chosenDot[0]-1]
                GameNums_2D[chosenDot[1]-1][chosenDot[0]-1] = ''
                
        else:
            print('     !!! Gotta make move in the same COLUMN as the first player')
            clearConsole()
            SecondPlayerMove(turn_counter, score, prev_move)
        
        print(f'\nSecond Player Move is: {chosenDot}({GameNums_2D[chosenDot[1]-1][chosenDot[0]-1]}). It makes their score: {score[1]}', end='')
        turn_counter+=1
        clearConsole()
        main(turn_counter, score, prev_move)


def main(turn_counter, score, prev_move):
    

    print('\n'*2)
    gamefield_gen_2D(GameNums_2D, turn_counter, score)
    
    if turn_counter % 2 != 0:
        FirstPlayerMove(turn_counter, score, prev_move)
    else:
        SecondPlayerMove(turn_counter, score, prev_move)


if __name__ == '__main__':
    main(turn_counter, score, prev_move)