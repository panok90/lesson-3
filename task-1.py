"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division_of_numbers_func(numerator, denominator):
    """division"""
    try:
        number = numerator / denominator
    except ZeroDivisionError:
        return "Деление на 0"
    return number


val1 = int(input("Введите первое число: "))
val2 = int(input("Введите второе число: "))
result = division_of_numbers_func(val1, val2)
print(result)
