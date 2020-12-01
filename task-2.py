"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def parameters_func(name, lastname, year_of_birth, city, email, phone):
    """output user data in a single line"""
    print(f'имя: {name}, фамилия: {lastname}, год рождения: {year_of_birth}, город проживания: {city}, email: {email},'
          f' телефон: {phone}')

parameters_func(name='John', lastname='Smith', year_of_birth='1990', city='New York', email='JonSmith@exemple.com',
                phone='+01234567899')
