import tkinter as tk
from itertools import permutations, product, islice
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.starting_seed = 0
        self.target_array = [6, 6]
        self.repeat_length = len(self.target_array)
        self.numbers_range = 10
        self.numbers = list(range(self.numbers_range))
        self.update_interval = 1000
        self.current_seed = None

        self.create_widgets()

        self.start_generation()

    def create_widgets(self):
        self.seed_label = tk.Label(self, text="Сид:")
        self.seed_label.pack()

        self.seed_value = tk.Entry(self, width=10)
        self.seed_value.insert(0, str(self.starting_seed))
        self.seed_value.pack()

        self.target_array_label = tk.Label(self, text="Целевой массив:")
        self.target_array_label.pack()

        self.target_array_value = tk.Entry(self, width=20)
        self.target_array_value.insert(0, str(self.target_array))
        self.target_array_value.pack()

        self.numbers_range_label = tk.Label(self, text="Количество чисел:")
        self.numbers_range_label.pack()

        self.numbers_range_value = tk.Entry(self, width=10)
        self.numbers_range_value.insert(0, str(self.numbers_range))
        self.numbers_range_value.pack()

        self.speed_label = tk.Label(self, text="Скорость:")
        self.speed_label.pack()

        self.speed_slider = tk.Scale(self, from_=100, to=10000, orient=tk.HORIZONTAL, command=self.update_speed_method)
        self.speed_slider.set(self.update_interval)
        self.speed_slider.pack()

        self.log_text = tk.Text(self, width=50, height=10)
        self.log_text.pack()

        self.update_button = tk.Button(self, text="Обновить", command=self.update_seed_value_and_arrays)
        self.update_button.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def start_generation(self):
        self.current_seed = self.find_array_from_seed(self.starting_seed, self.target_array, self.numbers, self.repeat_length)
        self.update_seed()

    def find_array_from_seed(self, seed_index, target_array, numbers, repeat_length):
        index = seed_index
        all_combinations = list(product(numbers, repeat=repeat_length))
        all_combinations_length = len(all_combinations)

        while True:
            if index >= all_combinations_length:
                self.log_text.insert(tk.END, "Все возможные комбинации проверены.\n")
                self.log_text.see(tk.END)
                return None

            repeated_array = all_combinations[index]
            self.log_text.insert(tk.END, f"Сид {index + 1}: {list(repeated_array)}\n")
            self.log_text.see(tk.END)

            if list(repeated_array) == target_array:
                self.log_text.insert(tk.END, f"Найдена повторяющаяся последовательность с сидом {index + 1}: {list(repeated_array)}\n")
                self.log_text.see(tk.END)
                return index + 1

            index += 1

    def update_seed(self):
        if self.current_seed is not None:
            self.log_text.insert(tk.END, f"Текущий сид: {self.current_seed}\n")
            self.log_text.see(tk.END)
            self.current_seed = self.find_array_from_seed(self.current_seed, self.target_array, self.numbers, self.repeat_length)
            self.after(self.update_interval, self.update_seed)

    def update_speed_method(self, value):
        self.update_interval = int(value)

    def update_seed_value_and_arrays(self):
        self.current_seed = int(self.seed_value.get())
        self.target_array = list(map(int, self.target_array_value.get().strip('[]').split(',')))
        self.numbers_range = int(self.numbers_range_value.get())
        self.numbers = list(range(self.numbers_range))
        self.repeat_length = len(self.target_array)
        self.log_text.delete(1.0, tk.END)  # CLEAR LOG TEXT BOX

root = tk.Tk()
root.title("Procedural Number Generator")
root.geometry("470x400")
app = Application(master=root)
app.mainloop()
