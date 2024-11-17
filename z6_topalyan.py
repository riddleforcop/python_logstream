# Задание 1
# def average_num(list_num: list) -> float:
#     for ind, el in enumerate(list_num):
#         if not isinstance(el, int | float):
#             try:
#                 list_num[ind] = int(el)
#             except:
#                 return "Bad request"
#     if len(list_num) == 0:
#         return "Bad request"
#     return round(sum(list_num) / len(list_num), 2)

# def tests():
#     print("Начало проверки...")
#     # на корректный список чисел
#     assert average_num([1, 2, 3, 4, 5]) == 3.0, "Ошибка: [1, 2, 3, 4, 5] должно быть 3.0"
    
#     # на список с числами с плавающей точкой
#     assert average_num([1.5, 2.5, 3.5]) == 2.5, "Ошибка: [1.5, 2.5, 3.5] должно быть 2.5"
    
#     # на список со строковыми числами, которые можно преобразовать в int
#     assert average_num(["1", "2", "3"]) == 2.0, "Ошибка: ['1', '2', '3'] должно быть 2.0"
    
#     # на список с нечислом, которое невозможно преобразовать в int
#     assert average_num(["1", "a", "3"]) == "Bad request", "Ошибка: ['1', 'a', '3'] должно вернуть 'Bad request'"
    
#     # на пустой список
#     assert average_num([]) == "Bad request", "Ошибка: пустой список должен вернуть 'Bad request'"
    
#     # на список с одним числом
#     assert average_num([42]) == 42.0, "Ошибка: [42] должно быть 42.0"
    
#     # на список с отрицательными числами
#     assert average_num([-3, -7, -10]) == -6.67, "Ошибка: [-3, -7, -10] должно быть -6.67"
    
#     # на смешанный список с int и float
#     assert average_num([1, 2.5, 3.5, 4]) == 2.75, "Ошибка: [1, 2.5, 3.5, 4] должно быть 2.75"
    
#     # на список с большим количеством чисел
#     assert average_num(list(range(1, 101))) == 50.5, "Ошибка: диапазон [1..100] должно быть 50.5"
    
#     # на список с None
#     assert average_num([1, None, 3]) == "Bad request", "Ошибка: [1, None, 3] должно вернуть 'Bad request'"
#     print("Все хорошо")

# if __name__ == "__main__":
#     tests()

#---------------------------------------------------------------------------------------------------------------------

# Задание 2
# import pytest

# def merge_and_write(file1_path, file2_path, output_file_path):
#     try:
#         with open(file1_path, 'r') as file1:
#             data1 = file1.read().strip()

#         with open(file2_path, 'r') as file2:
#             data2 = file2.read().strip()

#         merged_data = data1 + ' ' + data2

#         with open(output_file_path, 'w') as output_file:
#             output_file.write(merged_data)

#         with open(output_file_path, 'r') as output_file:
#             data = output_file.read()
#         return data
#     except FileNotFoundError:
#         return "Один из файлов не найден"

# @pytest.fixture
# def temp_files(tmp_path):
#     file1 = tmp_path / "file1.txt"
#     file2 = tmp_path / "file2.txt"
#     output_file = tmp_path / "output.txt"
#     return file1, file2, output_file

# def test_1(temp_files):
#     file1, file2, output_file = temp_files
#     file1.write_txt("Hello")
#     file2.write_txt("World")

#     result = merge_and_write(file1, file2, output_file)
#     assert result == "Hello World", "Результат слияния должен быть 'Hello World'"
#     assert output_file.read_txt() == "Hello World", "Выходной файл должен содержать 'Hello World'"

# def test_2(temp_files):
#     file1, file2, output_file = temp_files
#     file1.write_txt("Hello")

#     result = merge_and_write(file1, file2, output_file)
#     assert result == "Один из файлов не найден", "Должно вернуться сообщение об отсутствии файла"

# def test_3(temp_files):
#     file1, file2, output_file = temp_files
#     file1.write_txt("")
#     file2.write_txt("")

#     result = merge_and_write(file1, file2, output_file)
#     assert result == " ", "Результат слияния пустых файлов должен быть один пробел"
#     assert output_file.read_txt() == " ", "Выходной файл должен содержать один пробел"

#---------------------------------------------------------------------------------------------------------------------

# Задание 3
# import unittest
# import sys
# import time

# def factorial(n: int):
#     if n < 0:
#         raise ValueError("Факториал отрицательного числа не определен")
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#         if result > sys.maxsize:
#             raise ValueError(f"Факториал для {n} не поддерживается типом int")
#     return result

# class Tests(unittest.TestCase):
#     def test_1(self):
#         # факториал 0 должен быть равен 1
#         self.assertEqual(factorial(0), 1)

#     def test_2(self):
#         # факториал положительных чисел
#         self.assertEqual(factorial(5), 120)
#         self.assertEqual(factorial(3), 6)

#     def test_3(self):
#         # факториал большого числа
#         with self.assertRaises(ValueError):
#             factorial(100000)

#     def test_4(self):
#         # факториал отрицательного числа
#         with self.assertRaises(ValueError):
#             factorial(-1)

#     def test_5(self):
#         # факториал числа, близкого к пределу
#         self.assertEqual(factorial(20), 2432902008176640000)

#     def test_6(self):
#         # факториал нецелых чисел
#         with self.assertRaises(TypeError):
#             factorial(3.5)

# if __name__ == "__main__":
#     start_time = time.time()
#     unittest.main(exit=False)
#     end_time = time.time()
#     print(f"\nВремя выполнения тестов: {end_time - start_time:.4f} секунд")

