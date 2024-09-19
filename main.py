import random 

# Функция создаёт массив из 9 случайных чисел от 1 до 9 
# далее они будут использованы для генерации игрового поля


#TODO
# 1. Функция для генерации игрового поля 
# 2. Создать словать из 9 элементов который будет генерить значения для каждого (от 1 до 9) 
# 3. Подружить словарь и поле для вывода поля с значениями
# 4. Придумать логику игры
#  
GameNums={}


def gamelogic_NumsGeneration():

    for i in range(1,10):
        m= random.randint(1,9)
        GameNums.update({i:m})
    return GameNums

def gameplay_numbers():   
    numbers=[]
    for i in range (9):
        numbers.append(random.randint(1,9))
    return numbers


def gamefield_generator(numbers):
    print('''{} | {} | {}
{} | {} | {}
{} | {} | {} '''.format(GameNums.get(1),GameNums.get(2),GameNums.get(3),GameNums.get(4),GameNums.get(5),GameNums.get(6),GameNums.get(7),GameNums.get(8),GameNums.get(9)))
        




# test

gamelogic_NumsGeneration()
print(GameNums)
gamefield_generator(gameplay_numbers())