import random 

# Функция создаёт массив из 9 случайных чисел от 1 до 9 
# далее они будут использованы для генерации игрового поля

GameNums_2D=[]

def gamelogic_NumsGen_2D(GameNums_2D): #Работает
    for string in range(3):
        rN=[]
        for n in range(3):
            num=random.randint(1,9)
            rN.append(num)
        GameNums_2D.append(rN)



def gamefield_gen_2D(GameNums_2D): # Работает
   for arr in GameNums_2D:
       print('| {} | {} | {} |'.format(arr[0],arr[1],arr[2]))



# test

gamelogic_NumsGen_2D(GameNums_2D)
print(GameNums_2D)
gamefield_gen_2D(GameNums_2D)













