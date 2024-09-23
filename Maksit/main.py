import random
from random import randint
import os

GameNums_2D = [ [randint(1, 9) for j in [[]] * 3 ] for i in [[]] * 3 ] # creating 3x3 field with random nums in it
score = [0,0]   # [0] - first player score, [1] - second player score
turn_counter = 1    # turn counter

# func to clear console
def clearConsole():
    # to-do :D
    pass

# func to display field in the console
def gamefield_gen_2D(GameNums_2D):
    print('')
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
    

# func to make Player 1 move
def FirstPlayerMove(turn_counter, score):
    chosenDot = []
    
    print('First Player Move: ', end='')
    chosenDot = str(input()).split()
        
    if convertDotCoordsToInt(chosenDot) == 0:
        print('Incorrect dot coordinats input')
        clearConsole()
        main(turn_counter, score)
    else: 
        print(f'First Player Move is: {chosenDot}', end='')
        turn_counter+=1
        clearConsole()
        main(turn_counter, score)


# func to make Player 2 move
def SecondPlayerMove(turn_counter, score):
    chosenDot = []
    
    print('Second Player Move: ', end='')
    chosenDot = str(input()).split()
        
    if convertDotCoordsToInt(chosenDot) == 0:
        print('Incorrect dot coordinats input')
        clearConsole()
        main(turn_counter, score)
    else: 
        print(f'Second Player Move is: {chosenDot}', end='')
        turn_counter+=1
        clearConsole()
        main(turn_counter, score)



def main(turn_counter, score):
    
    gamefield_gen_2D(GameNums_2D)
    
    if turn_counter % 2 != 0:
        FirstPlayerMove(turn_counter, score)
        turn_counter+=1;
    else:
        SecondPlayerMove(turn_counter, score)
        turn_counter+=1;


if __name__ == '__main__':
    main(turn_counter, score)