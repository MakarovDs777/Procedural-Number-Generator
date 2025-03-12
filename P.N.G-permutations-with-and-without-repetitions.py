from itertools import permutations, product

# Функция для генерации всех перестановок чисел без повторений
def generate_permutations(numbers):
    return list(permutations(numbers))

# Функция для генерации всех массивов с повторениями
def generate_combinations_with_repeats(numbers, repeat_length):
    return list(product(numbers, repeat=repeat_length))

# Функция для поиска заданного массива среди всех перестановок и сочетаний
def find_target_array(start_seed, target_array):
    length = len(target_array)
    numbers = list(range(10))  # Числа от 0 до 9

    # Генерация всех перестановок без повторений
    permuted_arrays = generate_permutations(numbers)

    # Проверка всех перестановок
    index = start_seed
    while index < len(permuted_arrays):
        generated_array = permuted_arrays[index]  # Получаем перестановку
        print(f"сид {index + 1}: {list(generated_array)}")
        
        if list(generated_array) == target_array:
            print(f"Найдена перестановка без повторений с сидом {index + 1}: {list(generated_array)}")
            return index + 1  # Возвращаем 1-индексируемый номер
        
        index += 1

    # Теперь переходим к перестановкам с повторениями
    print("Переход к перестановкам с повторениями...")
    repeated_arrays = generate_combinations_with_repeats(numbers, length)
    
    # Проверка всех массивов с повторениями
    for index, generated_array in enumerate(repeated_arrays):
        print(f"сид {len(permuted_arrays) + index + 1}: {list(generated_array)}")  # Выводим текущую перестановку
        
        if list(generated_array) == target_array:
            print(f"Найдена перестановка с повторениями с сидом {len(permuted_arrays) + index + 1}: {list(generated_array)}")
            return len(permuted_arrays) + index + 1  # Возвращаем общий индекс

    print("Все возможные комбинации проверены.")
    return None  # Если ничего не найдено

# Основная часть программы
starting_seed = 0  # Начальный индекс
target_array = [2, 6, 3, 4, 8, 7, 9, 5, 0, 1]  # Замените на целевой массив
find_target_array(starting_seed, target_array)
