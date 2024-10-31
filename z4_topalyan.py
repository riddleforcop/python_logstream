# Задание 1 
# пункт 1
# squar = [x**2 for x in range(1, 11)]
# print(squar)

# # пункт 2
# days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# days_dict = {day: i + 1 for i, day in enumerate(days)}
# print(days_dict)

# # пункт 3
# libr = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
# libr_set = {lib.lower() for lib in libr}
# print(libr_set)

# Задание 2
# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
# n = 10
# fib_seq = list(fibonacci(n))
# print(fib_seq)

# Задание 3
# def write_and_print(text, filename):
#     with open(filename, mode="a+", encoding="utf-8") as f:
#         f.write(text + "\n")
#         f.seek(0)
#         lines = f.readlines()
#     for index, line in enumerate(lines):
#         if index % 2 == 1:
#             print(line.strip())

# write_and_print("Для записи и создания файла нужно использовать mode = ”a+”. Для получения всех строк файла можно использовать f.readlines(). Чтение данных из файла реализовать с помощью контекстного", "qwerty.txt")

# Задание 4
# def debug_info(func):
#     def wrap(*args, **kwargs):
#         print(f"Вызов функции {func.__name__} с позиционными аргументами {args} и именованными аргументами {kwargs}")
#         return func(*args, **kwargs)
#     return wrap

# @debug_info
# def fibonacci(n):
#     a, b = 1, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# n = 10
# fib_sequence = list(fibonacci(n))
# print(fib_sequence)

# Задание 5*
# class Cards:
#     def __init__(self):
#         self.suits = ["Пики", "Черви", "Буби", "Крести"]
#         self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]
#         self.cards = [f"{value} {suit}" for suit in self.suits for value in self.values]
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index < len(self.cards):
#             card = self.cards[self.index]
#             self.index += 1
#             return card
#         else:
#             raise StopIteration

# deck = Cards()
# for card in deck:
#     print(card)
