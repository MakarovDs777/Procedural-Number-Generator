from itertools import permutations, product, islice

# Функция для генерации всех перестановок чисел без повторений
def generate_permutations(numbers):
    return list(permutations(numbers))

# Функция для генерации всех массивов с повторениями
def generate_combinations_with_repeats(numbers, repeat_length):
    return list(product(numbers, repeat=repeat_length))

# Функция для поиска заданного массива среди всех перестановок и сочетаний
def find_target_array(start_seed, target_array, permutations_array):
    length = len(target_array)
    numbers = list(range(10))  # Числа от 0 до 9

    index = start_seed - 1
    while True:
        for permuted_array in permutations_array:
            index += 1
            print(f"сид {index + 1}: {list(permuted_array)}")
            if list(permuted_array) == target_array:
                print(f"Найдена перестановка без повторений с сидом {index + 1}: {list(permuted_array)}")
                return index + 1  # Возвращаем 1-индексируемый номер

        # Теперь переходим к перестановкам с повторениями
        print("Переход к перестановкам с повторениями...")
        for repeated_array in generate_combinations_with_repeats(numbers, length):
            index += 1
            print(f"сид {index + 1}: {list(repeated_array)}")  # Выводим текущую перестановку
            if list(repeated_array) == target_array:
                print(f"Найдена перестановка с повторениями с сидом {index + 1}: {list(repeated_array)}")
                return index + 1  # Возвращаем общий индекс

    print("Все возможные комбинации проверены.")
    return None  # Если ничего не найдено

# Основная часть программы
target_array = [2, 6, 3, 4, 8, 7, 9, 5, 0, 1]  # Замените на целевой массив

numbers = list(range(10))  

start_seed_array = [3, 8, 6, 7, 5, 2, 1, 4, 9, 0] 
index = list(permutations(numbers)).index(tuple(start_seed_array)) + 1

permutations_array = list(islice(permutations(numbers), index-1, None))

find_target_array(index, target_array, permutations_array)