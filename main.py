import random 

# Функция создаёт массив из 9 случайных чисел от 1 до 9 
# далее они будут использованы для генерации игрового поля


#TODO
# 1. Функция для генерации игрового поля 
# 2. Создать словать из 9 элементов который будет генерить значения для каждого (от 1 до 9) 
# 3. Подружить словарь и поле для вывода поля с значениями
# 4. Придумать логику игры
#  

def gameplay_numbers():   
    numbers=[]
    for i in range (9):
        numbers.append(random.randint(1,9))
    return numbers



# 1 | 1 | 1
# 1 | 1 | 1
# 1 | 1 | 1
def gamefield_generator(numbers):
    print('''{\f} | {\f} | {\f}
{\f} | {\f} | {\f}
{\f} | {\f} | {\f} ''')
        
gamefield_generator(gameplay_numbers())