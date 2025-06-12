from itertools import product
import math

def generate_array_from_seed(seed, array_length):
    """Генерирует массив из 0 и 1 заданной длины на основе seed."""
    if seed <= 0:
        raise ValueError("Seed должен быть положительным целым числом.")

    # Общее количество возможных комбинаций
    total_combinations = 2**array_length

    if seed > total_combinations:
         raise ValueError(f"Seed слишком большой. Максимальный seed для длины {array_length}: {total_combinations}")

    # Преобразуем seed в индекс (начинаем с 0)
    index = seed - 1

    # Преобразуем индекс в двоичное представление фиксированной длины
    binary_representation = bin(index)[2:].zfill(array_length)

    # Преобразуем двоичную строку в массив целых чисел (0 и 1)
    array = [int(bit) for bit in binary_representation]
    return array

# Пример использования
if __name__ == "__main__":
    array_length = 10  # Длина массива
    seed = int(input("Введите номер сида: ")) # Получаем seed от пользователя

    try:
        generated_array = generate_array_from_seed(seed, array_length)
        print(f"Для сида {seed} сгенерирован массив: {generated_array}")
    except ValueError as e:
        print(f"Ошибка: {e}")
