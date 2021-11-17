"""
Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка:
с текстовой и числовой информацией.
Для создания списков использовать генераторы.
Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан
и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла
и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
"""
from os.path import exists
import random


def read(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        for line in f.readlines():
            print(line)


def write(file_path):
    if not exists(file_path):
        print("По данному пути такого файла не существует.")
    with open(file_path, "w", encoding='utf-8') as f:
        line_cnt = random.randint(1, 100)
        random_words = [[chr(random.randint(97, 122)) for _ in range(random.randint(3, 20))] for _ in range(line_cnt)]
        random_words = ["".join(word).capitalize() for word in random_words]
        random_numbers = [random.randint(1, 1_000_000_000_000) for _ in range(line_cnt)]
        f.write("\n".join([f"{word} {number}" for word, number in zip(random_words, random_numbers)]))
    read(file_path)


if __name__ == "__main__":
    file = '/Users/nikolajpetrov/Documents/gb_interview/gb_interview/test.txt'
    write(file)
