import numpy as np
from itertools import permutations

# Функция для генерации всех перестановок чисел от 0 до 9
def generate_permutations(numbers):
    return list(permutations(numbers))

# Функция для отображения перестановок
def display_permutations(permutations):
    for index, perm in enumerate(permutations):
        print(f"сид {index + 1}: {list(perm)}")

# Основная часть программы
numbers = list(range(10))  # Числа от 0 до 9
permuted_arrays = generate_permutations(numbers)

# Вывод всех перестановок
display_permutations(permuted_arrays)
