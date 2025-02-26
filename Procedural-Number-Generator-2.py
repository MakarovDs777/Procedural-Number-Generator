import numpy as np
from itertools import permutations

# Функция для генерации массива случайных чисел
def generate_random_array(seed, length):
    np.random.seed(seed)
    return np.random.randint(0, 10, size=length).tolist()  # Генерация чисел от 0 до 9

# Функция для поиска сида по заданному массиву
def find_seed(target_array):
    length = len(target_array)
    for seed in range(2**32):  # Перебор всех возможных сидов
        generated_array = generate_random_array(seed, length)
        # Вывод информации о текущем сиде и результате сравнения
        if generated_array == target_array:
            print(f"{seed} 1 {generated_array}")  # Сид соответствует
            return seed
        else:
            print(f"{seed} 0 {generated_array}")  # Сид не соответствует
    return None  # Если сид не найден

# Функция для генерации и поиска по всем перестановкам
def search_seeds_in_permutations(numbers):
    for index, perm in enumerate(permutations(numbers)):
        print(f"Поиск для сид {index + 1}: {list(perm)}")
        found_seed = find_seed(list(perm))
        if found_seed is not None:
            print(f"Найден сид для {list(perm)}: {found_seed}")
        else:
            print(f"Сид не найден для {list(perm)}")

# Основная часть программы
numbers = list(range(10))  # Числа от 0 до 9
search_seeds_in_permutations(numbers)
