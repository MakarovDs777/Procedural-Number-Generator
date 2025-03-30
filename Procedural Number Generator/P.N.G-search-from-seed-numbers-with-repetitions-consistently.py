from itertools import permutations, product, islice

# Функция для генерации всех массивов с повторениями
def generate_combinations_with_repeats(numbers, repeat_length):
    return list(product(numbers, repeat=repeat_length))

# Функция для поиска заданного массива среди всех перестановок и сочетаний
def find_array_from_seed(seed_index, target_array, numbers, repeat_length):
    index = seed_index  # Начинаем с указанного индекса
    all_combinations = generate_combinations_with_repeats(numbers, repeat_length)
    all_combinations_length = len(all_combinations)

    while True:  # Бесконечный цикл
        if index >= all_combinations_length:  # Если индекс выходит за пределы
            print("Все возможные комбинации проверены.")
            break

        repeated_array = all_combinations[index]  # Получаем повторяющуюся последовательность чисел по индексу
        print(f"сид {index + 1}: {list(repeated_array)}")  # Выводим текущую повторяющуюся последовательность чисел

        # Проверяем, не содержит ли полученная повторяющаяся последовательность соответствующих чисел
        if len(set(repeated_array))!= len(repeated_array):
            if list(repeated_array) == target_array:
                print(f"Найдена повторяющаяся последовательность с сидом {index + 1}: {list(repeated_array)}")  # Нашли соответствие
                return index + 1  # Возвращаем 1-индексируемый номер последовательности

        index += 1  # Увеличиваем индекс для следующей итерации

# Основная часть программы
starting_seed = 0  # Начальный индекс
target_array = [6, 6]  # Замените на целевой массив
repeat_length = len(target_array)
numbers = list(range(10))  # Числа от 0 до 9
find_array_from_seed(starting_seed, target_array, numbers, repeat_length)
