import numpy as np
 
 # Функция для генерации массива случайных чисел
def generate_random_array(seed, length):
    np.random.seed(seed)
    return np.random.randint(0, LenNumber, size=length).tolist()  # Генерация чисел от 0 до 9
 
 # Функция для отображения сгенерированного массива
def display_generated_array(seed):
    generated_array = generate_random_array(seed, LenNumber)  
    print(f"сид {seed}: {generated_array}")  # Выводим сид и массив
 
 # Основная часть программы
def search_from_seed(start_seed):
    for seed in range(start_seed, start_seed + rainbowRow):  
        display_generated_array(seed)
 
 # Пример использования
rainbowRow = 2 # Поиск 2 последовательных сидов
LenNumber = 10 # Длина массива = 10
starting_seed = 9 # Замените на нужный сид
search_from_seed(starting_seed)
