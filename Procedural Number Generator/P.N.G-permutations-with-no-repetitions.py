import numpy as np
from itertools import permutations

# Функция для генерации всех перестановок чисел от 0 до 9
def generate_permutations(numbers):
    return list(permutations(numbers))

# Функция для поиска массивов с заданным сидом и целевым массивом
def find_array_from_seed(start_seed, target_array):
    length = len(target_array)
    numbers = list(range(10))
    permuted_arrays = generate_permutations(numbers)  # Генерация всех перестановок

    index = start_seed  # Начинаем с указанного индекса
    
    while True:  # Бесконечный цикл
        if index >= len(permuted_arrays):  # Если индекс выходит за пределы
            print("Все перестановки уже проверены.")
            break
        
        generated_array = permuted_arrays[index]  # Получаем перестановку по индексу
        print(f"сид {index + 1}: {list(generated_array)}")  # Выводим текущую перестановку
        
        if list(generated_array) == target_array:
            print(f"Найдена перестановка с сидом {index + 1}: {list(generated_array)}")  # Нашли соответствие
            return index + 1  # Возвращаем 1-индексируемый номер перестановки
        
        index += 1  # Увеличиваем индекс для следующей итерации

# Основная часть программы
starting_seed = 1000000  # Начальный индекс
target_array = [2, 6, 3, 4, 8, 7, 9, 5, 0, 1]  # Замените на целевой массив
find_array_from_seed(starting_seed, target_array)