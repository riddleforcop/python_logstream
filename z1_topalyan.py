# Номер 1

'''
while True:
    user_text = input("Введите число или exit для выхода: ")

    if user_text.lower() == "exit":
        print("Выход")
        break

    if user_text.isdigit() or (user_text.startswith('-') and user_text[1:].isdigit()):
        print(f"Длина введенного числа: {len(user_text)}")
    if user_text.startswith('-'):
        print(f"Длина введенного числа: {len(user_text) - 1}")
    else:
        print("Ошибка: введите корректное число.")
'''

# Номер 2
'''
user_text = int(input("Введите число: "))

print("Числа в интервале от", -user_text, "до", user_text + 1)
for i in range(-user_text, user_text + 1):
    print(i, end=" ")
print()

sum_negative = 0
sum_positive = 0
for i in range(-user_text, user_text + 1):
    if i < 0:
        sum_negative += i
    elif i > 0:
        sum_positive += i
print("Сумма отрицательных чисел:", sum_negative)
print("Сумма положительных чисел:", sum_positive)
'''

# Номер 3
'''
user_text = input("Введите трехзначное число с различными цифрами: ")
if not user_text.isdigit() or len(user_text) != 3:
    print("Ошибка: введите корректное трехзначное число.")
else:
    a, b, c = user_text[0], user_text[1], user_text[2]
    if a == b or a == c or b == c:
        print("Ошибка: цифры в числе не должны повторяться.")
    else:
        print("Перестановки цифр числа:")
        perm = [
            a + b + c,
            a + c + b,
            b + a + c,
            b + c + a,
            c + a + b,
            c + b + a
        ]
        for p in perm:
            print(p)
'''

# Номер 4

# Пункт 1
'''
ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
shot = input("Введите координаты выстрела: ")
ship = ship.lower()
shot = shot.lower()
if ship.find(shot) != -1:
    print("Попадание")
else:
    print("Мимо")
'''

# Пункт 2
'''
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")
output_format = "Ваше имя: {0}, Фамилия: {1}, Возраст: {2} лет.".format(name, surname, age)
print(output_format)
output_fstring = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет."
print(output_fstring)
'''
