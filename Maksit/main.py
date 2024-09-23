import random
from random import randint

# creating array that will be the field
GameNums_2D = [ [randint(1, 9) for j in [[]] * 3 ] for i in [[]] * 3 ]
            
# func to display field in the console
def gamefield_gen_2D(GameNums_2D): # Работает
    print('')
    for i in GameNums_2D:
        for j in i:
            print(f'   {j}', end = '   ')
        print('\n')
        

def gamefield_gen_2D_second(GameNums_2D): # Работает
    print('\n-------------------',end='')
    print(f'\n|  {GameNums_2D[0][0]}  |  {GameNums_2D[0][1]}  |  {GameNums_2D[0][2]}  |',end='')
    print('\n-------------------',end='')
    print(f'\n|  {GameNums_2D[1][0]}  |  {GameNums_2D[1][1]}  |  {GameNums_2D[1][2]}  |',end='')
    print('\n-------------------',end='')
    print(f'\n|  {GameNums_2D[2][0]}  |  {GameNums_2D[2][1]}  |  {GameNums_2D[2][2]}  |',end='')
    print('\n-------------------')
    

# test
        
gamefield_gen_2D(GameNums_2D)
gamefield_gen_2D_second(GameNums_2D)













