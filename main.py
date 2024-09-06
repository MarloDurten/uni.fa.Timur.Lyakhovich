import random 

# Функция создаёт массив из 9 случайных чисел от 1 до 9 
# далле они будут использованы для генерации игрового поля
def gameplay_numbers():   
    numbers=[]
    for i in range (9):
        numbers.append(random.randint(1,9))
    return numbers


# 1 | 1 | 1
# 1 | 1 | 1
# 1 | 1 | 1
def gamefield_generator(numbers):
    print('''\f | \f | \f
\f | \f | \f
\f | \f | \f ''')
        
gamefield_generator(gameplay_numbers())
    