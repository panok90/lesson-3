"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(*my_dict):
    """sum of the largest two arguments"""
    my_list = sorted(my_dict)
    sum_number = my_list[1] + my_list[2]
    return sum_number


val1 = int(input("Введите значение перврго аргумента: "))
val2 = int(input("Введите значение второго аргумента: "))
val3 = int(input("Введите значение третьего аргумента: "))
result = my_func(val1, val2, val3)
print(result)
