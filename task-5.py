"""Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу."""


def sum_func(source_list, my_sum):
    """Sum of list values"""
    sum_number = 0
    for item in source_list:
        sum_number += int(item)
    my_sum += sum_number
    return my_sum


result = 0
while True:
    string = input("Введите строку чисел нажатии Enter(если вы закончили нажмите '~'): ")
    my_list = string.split()
    if my_list[0] == '~':
        break
    elif my_list[-1] == '~':
        my_list = my_list[:-1]
        result = sum_func(my_list, result)
        break
    else:
        result = sum_func(my_list, result)

print(result)
