from itertools import permutations, product

# Функция для генерации всех перестановок чисел без повторений
def generate_permutations(numbers):
    return list(permutations(numbers))

# Функция для генерации всех массивов с повторениями
def generate_combinations_with_repeats(numbers, repeat_length):
    return list(product(numbers, repeat=repeat_length))

# Функция для поиска заданного массива среди всех перестановок и сочетаний
def find_target_array(target_array, array_length, start_seed=1):
    numbers = [0, 1]
    index = start_seed - 1  # Начинаем с переданного seed

    # Перестановки без повторений не применимы в данном случае, т.к. мы ищем массив длиной array_length из 0 и 1.

    # Сразу переходим к перестановкам с повторениями
    print("Переход к перестановкам с повторениями...")
    for repeated_array in generate_combinations_with_repeats(numbers, array_length):
        index += 1
        print(f"сид {index + 1}: {list(repeated_array)}")  # Выводим текущую перестановку
        if list(repeated_array) == target_array:
            print(f"Найдена перестановка с повторениями с сидом {index + 1}: {list(repeated_array)}")
            return index + 1  # Возвращаем общий индекс

    print("Все возможные комбинации проверены.")
    return None  # Если ничего не найдено

# Основная часть программы
target_array = [0, 1, 0, 1, 1, 0, 1, 0, 1, 0]  # Замените на нужный массив из 0 и 1
array_length = len(target_array) # Длина массива
start_seed = 1 # Начальный сид

result = find_target_array(target_array, array_length, start_seed)

if result:
    print(f"Целевой массив найден с сидом: {result}")
else:
    print("Целевой массив не найден.")
