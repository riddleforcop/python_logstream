# Задание 1
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Деление на ноль запрещено.")
#     return a / b

# def power(a, b):
#     return a ** b

# def validate_input(value):
#     try:
#         return float(value)
#     except ValueError:
#         raise ValueError("Неверный ввод: не число.")

# def calculator():
#     while True:
#         print("\nВыберите операцию:")
#         print("1. Сложение")
#         print("2. Вычитание")
#         print("3. Умножение")
#         print("4. Деление")
#         print("5. Возведение в степень")
#         print("6. Выход")
#         choice = input("Введите номер операции (1/2/3/4/5/6): ")
#         if choice == '6':
#             print("Выход из программы.")
#             break
#         if choice not in ('1', '2', '3', '4', '5', '6'):
#             print("Неверный выбор, пожалуйста, выберите корректную операцию.")
#             continue
#         try:
#             num1 = validate_input(input("Введите первое число: "))
#             num2 = validate_input(input("Введите второе число: "))
#             if choice == '1':
#                 print(f"{num1} + {num2} = {add(num1, num2)}")
#             elif choice == '2':
#                 print(f"{num1} - {num2} = {subtract(num1, num2)}")
#             elif choice == '3':
#                 print(f"{num1} * {num2} = {multiply(num1, num2)}")
#             elif choice == '4':
#                 print(f"{num1} / {num2} = {divide(num1, num2)}")
#             elif choice == '5':
#                 print(f"{num1} ^ {num2} = {power(num1, num2)}")
#         except ValueError as ve:
#             print(ve)
#         except ZeroDivisionError as zde:
#             print(zde)

# if __name__ == "__main__":
#     calculator()


# Задание 2
# def mul_list(els, mul=2):
#     return [el * mul for el in els]
# mul_lambda = lambda els, mul=2: [el * mul for el in els]

# print(mul_list([1, 2, 3]))
# print(mul_list([1, 2, 3], 5))
# print(mul_lambda([1, 2, 3]))
# print(mul_lambda([1, 2, 3], 5))

# Задание 3
# def function_name(search: str, status: bool, *args: tuple, **kwargs: dict) -> list | str:
#     result = []
#     result_2 = ""
#     if search == "args":
#         if status:
#             for i in args:
#                 if isinstance(i, int):
#                     result.append(i)
#             return result
#         else:
#             for i in args:
#                 result_2 += f" {i}"
#             return result_2
#     elif search == "kwargs":
#         for k, v in kwargs.items():
#             result_2 += f" Key: {k}, Value: {v}; "
#         return result_2
    
#     else:
#         raise ValueError("Error for search")
# print(function_name("args", True, 1, 2, "three", 4))
# print(function_name("args", False, 1, 2, "three", 4))
# print(function_name("kwargs", True, a=1, b=2, c="three"))

# Задание 4
# class Wallet:
#     def __init__(self, name: str, curr: str):
#         self.name = name
#         if curr not in ("USD", "EUR", "RUB"):
#             raise ValueError("Неверная валюта. Допустимые валюты: USD, EUR, RUB.")
#         self.curr = curr
#         self._balance = 0

#     def deposit(self, summa: float) -> None:
#         if summa <= 0:
#             raise ValueError("Сумма пополнения должна быть больше 0.")
#         self._balance += summa
#         print(f"Баланс пополнен на {summa} {self.curr}.")

#     def pay(self, summa: float) -> None:
#         if summa <= 0:
#             raise ValueError("Сумма оплаты должна быть больше 0.")
#         if self._balance >= summa:
#             self._balance -= summa
#             print(f"Оплата {summa} {self.curr} прошла успешно.")
#         else:
#             print("Недостаточно средств для выполнения операции.")

#     def show_balance(self) -> None:
#         print(f"Баланс: {self._balance} {self.curr}")

#     def delete_account(self) -> None:
#         self._balance = 0
#         print(f"Счет '{self.name}' удален. Баланс обнулен.")

# class CryptoWallet(Wallet):
#     def __init__(self, name: str, curr: str, coin: str):
#         super().__init__(name, curr)
#         if coin not in ("BTC", "ETH"):
#             raise ValueError("Неверная криптовалюта. Допустимые криптовалюты: BTC, ETH.")
#         self.coin = coin

#     def show_balance(self) -> None:
#         print(f"Баланс: {self._balance} {self.coin}")

#     def balance_in_dollars(self) -> None:
#         conv_rates = {
#             "BTC": 72000,
#             "ETH": 3500
#         }
#         if self.coin in conv_rates:
#             balance_in_usd = self._balance * conv_rates[self.coin]
#             print(f"Баланс в долларах: {balance_in_usd} USD")
#         else:
#             print("Невозможно перевести в доллары. Неподдерживаемая валюта.")

# wallet = Wallet("My Wallet", "USD")
# wallet.deposit(100)
# wallet.pay(130)
# wallet.show_balance()
# wallet.pay(30)
# wallet.show_balance()
# wallet.delete_account()
# wallet.show_balance()
# print()
# crypto_wallet = CryptoWallet("Crypto Wallet", "USD", "BTC")
# crypto_wallet.deposit(1.5)
# crypto_wallet.show_balance()
# crypto_wallet.balance_in_dollars()