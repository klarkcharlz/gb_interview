"""
Написать программу,
которая будет содержать функцию для получения имени файла
из полного пути до него. При вызове функции
в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла,
а затем «выделение» из этого пути имени файла (без расширения).
"""
from os.path import splitext, basename


def get_file_name(full_path: str) -> str:
    return splitext(basename(full_path))[0]


if __name__ == "__main__":
    path = '/Users/nikolajpetrov/Documents/gb_interview/gb_interview/1.py'
    print(get_file_name(path))
