# -*- coding: utf-8 -*-

# Сам массив явно задан
base_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def generate_array_from_base(seed, length, shift_by_seed=False):
    """
    Возвращает массив длины `length`, взятый из base_array.
    Если shift_by_seed=True, массив циклически сдвигается вправо на seed % length.
    """
    arr = base_array[:length]  # используем явный массив
    if shift_by_seed:
        shift = seed % length
        if shift:
            arr = arr[-shift:] + arr[:-shift]
    return arr

def display_generated_array(seed, length, shift_by_seed=False):
    generated_array = generate_array_from_base(seed, length, shift_by_seed)
    print(f"сид {seed}: {generated_array}")

def search_from_seed(start_seed, rainbowRow, LenNumber, shift_by_seed=False):
    for seed in range(start_seed, start_seed + rainbowRow):
        display_generated_array(seed, LenNumber, shift_by_seed)

# Пример использования
rainbowRow = 12    # Поиск последовательных сидов
LenNumber = 10    # Длина массива
starting_seed = 9 # Замените на нужный сид

# Без сдвига:
# search_from_seed(starting_seed, rainbowRow, LenNumber, shift_by_seed=False)

# С сдвигом по сиду (пример вывода для starting_seed=9):
search_from_seed(starting_seed, rainbowRow, LenNumber, shift_by_seed=True)
