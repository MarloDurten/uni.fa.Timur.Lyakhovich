import random
from random import randint

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
def FirstPlayerMove():
    chosenDot = []
    
    print('First Player Move: ', end='')
    chosenDot = str(input()).split()
        
    if convertDotCoordsToInt(chosenDot) == 0:
        print('Incorrect dot coordinats input')
        main()
    else: 
        print(f'First Player Move is: {chosenDot}', end='')   


# func to make Player 2 move
def SecondPlayerMove():
    chosenDot = []
    
    print('Second Player Move: ', end='')
    chosenDot = str(input()).split()
        
    if convertDotCoordsToInt(chosenDot) == 0:
        print('Incorrect dot coordinats input')
        main()
    else: 
        print(f'Second Player Move is: {chosenDot}', end='')   



def main():
    # creating array that will be the field
    GameNums_2D = [ [randint(1, 9) for j in [[]] * 3 ] for i in [[]] * 3 ]
    first_dude_score = 0
    second_dude_score = 0
    turn_counter = 1

    gamefield_gen_2D(GameNums_2D)
    
    if turn_counter % 2 != 0:
        FirstPlayerMove()
        turn_counter+=1;
    else:
        SecondPlayerMove()
        turn_counter+=1;


if __name__ == '__main__':
    main()