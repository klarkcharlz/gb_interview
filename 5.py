"""
Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений заменить
на значения типа example345 (строка+число).
Далее — усовершенствовать вторую функцию
из предыдущего примера (функцию извлечения данных).
Дополнительно реализовать поиск определенных подстрок
в файле по следующим условиям: вывод первого вхождения,
вывод всех вхождений.
Реализовать замену всех найденных подстрок на новое значение
и вывод всех подстрок, состоящих из букв и цифр
и имеющих пробелы только в начале и конце — например, example345.
"""
from os.path import exists
import random
from re import findall


def find_text(file, template, multi=False):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        res = findall(template, text)
        if multi:
            return res
        return res[0]


def replace(file, old, new):
    with open(file, "r", encoding='utf-8') as f:
        old_text = f.read()
    with open(file, "w", encoding='utf-8') as f:
        f.write(old_text.replace(old, new))


def read(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        for line in f.readlines():
            print(line)


def find_example345(file):
    with open(file, "r", encoding='utf-8') as f:
        text = f.read()
        return findall(r'[a-zA-Z]+\d+', text)


def write(file_path):
    if not exists(file_path):
        print("По данному пути такого файла не существует.")
    with open(file_path, "w", encoding='utf-8') as f:
        line_cnt = random.randint(1, 100)
        random_words = [[chr(random.randint(97, 122)) for _ in range(random.randint(3, 20))] for _ in range(line_cnt)]
        random_words = ["".join(word).capitalize() for word in random_words]
        random_numbers = [random.randint(1, 1_000_000_000_000) for _ in range(line_cnt)]
        f.write("\n".join([f"{word}{random.choice([' ', ''])}{number}" for word, number in zip(random_words, random_numbers)]))
    read(file_path)


if __name__ == "__main__":
    file = '/Users/nikolajpetrov/Documents/gb_interview/gb_interview/test.txt'
    # write(file)
    # print(find_text(file, "Wmkcdppul"))
    # replace(file, "Wmkcdppul", "TEST")
    print(find_example345(file))