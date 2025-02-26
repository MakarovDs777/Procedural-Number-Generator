import numpy as np

# Функция для генерации массива случайных чисел
def generate_random_array(seed, length):
    np.random.seed(seed)
    return np.random.randint(0, 10, size=length).tolist()  # Генерация чисел от 0 до 9

# Функция для поиска массива с заданным сидом и целевым массивом
def find_array_from_seed(start_seed, target_array):
    length = len(target_array)
    seed = start_seed  # Начинаем с указанного сида

    while True:  # Бесконечный цикл
        generated_array = generate_random_array(seed, length)
        if generated_array == target_array:
            print(f"Найден сид {seed}: {generated_array}")  # Нашли соответствие
            return seed
        else:
            print(f"сид {seed}: {generated_array}")  # Не соответствует
        seed += 1  # Увеличиваем сид на 1 для следующей итерации

# Пример использования
starting_seed = 2166528  # Замените на нужный сид
target_array = [9, 6, 9, 2, 6, 6, 5, 7, 5, 0]  # Замените на целевой массив
find_array_from_seed(starting_seed, target_array)
