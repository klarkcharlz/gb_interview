"""
Дополнить следующую функцию недостающим кодом:
"""
from os import listdir
from os.path import isdir


def print_directory_contents(sPath: str) -> None:
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    files = listdir(sPath)
    for file in files:
        new_path = f"{sPath}/{file}"
        if isdir(new_path):
            print_directory_contents(new_path)
        else:
            print(new_path)


if __name__ == "__main__":
    print_directory_contents("..")
