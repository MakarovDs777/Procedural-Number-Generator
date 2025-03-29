from itertools import permutations, product, islice

# Функция для генерации всех массивов с повторениями
def generate_combinations_with_repeats(numbers, repeat_length):
    return list(product(numbers, repeat=repeat_length))

# Функция для поиска заданного массива среди всех перестановок и сочетаний
def find_target_array(start_seed, target_array, repeat_length, numbers):
    index = start_seed - 1
    while True:
        for repeated_array in generate_combinations_with_repeats(numbers, repeat_length):
            index += 1
            print(f"сид {index + 1}: {list(repeated_array)}")
            # Проверяем, не содержит ли полученная перестановка повторяющиеся числа
            if len(set(repeated_array))!= len(repeated_array):
                if list(repeated_array) == target_array:
                    print(f"Найдена перестановка с повторениями с сидом {index + 1}: {list(repeated_array)}")
                    return index + 1  # Возвращаем 1-индексируемый номер
        else:
            # Если все перестановки с повторениями проверены и ничего не найдено
            print("Все возможные комбинации проверены.")
            return None  # Если ничего не найдено

# Основная часть программы
target_array = [2, 6, 3, 4, 8, 7, 9, 5, 0, 1, 1]  # Замените на целевой массив
repeat_length = len(target_array)
numbers = list(range(10))  # Числа от 0 до 9

start_seed_array = [3, 8, 6, 7, 5, 2, 1, 4, 9, 0, 1] 
comma_start = 0
for repeated_array in generate_combinations_with_repeats(numbers, repeat_length):
    comma_start += 1
    if list(repeated_array) == start_seed_array:
        break
find_target_array(comma_start, target_array, repeat_length, numbers)
