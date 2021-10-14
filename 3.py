"""
Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить).
Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""
from time import time


def randint(min_num: int, max_num: int) -> int:
    """
    Генератор случайного целого положительного числа
    :param min_num: минимальное число диапазона генерации случайного числа
    :param max_num: максимальное число диапазона генерации случайного числа
    :return: случайное целое положительное число от min_num до max_num включительно
    """
    try:
        assert min_num > 0 and max_num > 0, "Число должно быть положительным"
        assert min_num != max_num, "Числа не должны быть равны"
        assert min_num < max_num, "Минимальное число не может быть больше максимального"
    except AssertionError as err:
        raise ValueError(err)
    else:
        root = int(str(time()).split(".")[1]) * int(str(time()).split(".")[0])  # длинное случайное число
        rand_int = root % (max_num - min_num + 1) + min_num
        return rand_int


def create_rand_dict(rand_l: list) -> dict:
    """
    Генерация словаря на основе списка с случайными числами
    :param rand_l: список наполненный случайными числами
    :return: словарь на основе списка с случайными числами
    """
    return {f"elem_{num}" for num in rand_l}


def create_rand_list(min_num: int, max_num: int, n: int) -> list:
    """
    Генерация списка наполненного случайными числами
    :param min_num: минимальное число диапазона генерации случайного числа
    :param max_num: максимальное число диапазона генерации случайного числа
    :param n: количество необходимых случайных цифр
    :return: список наполненный случайными числами
    """
    return [randint(min_num, max_num) for _ in range(n)]


if __name__ == "__main__":
    try:
        min_, max_, n = map(int, (input("Пожалуйста введите через запятую минимальную границу генерации, максимальную "
                                        "и необходимое количество случайных чисел:\n ").split(",")))
    except ValueError:
        print("Ну что ты вводишь!")
    else:
        rand_list = create_rand_list(min_, max_, n)
        rand_dict = create_rand_dict(rand_list)
        print(f"{rand_list}\n{rand_dict}")  # словарь может быть короче списка, так как возможны дубликаты чисел
