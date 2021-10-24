import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(BASE_DIR, 'trash_fold')


def size_of_files(path: str) -> list:
    """
    создает список элементов типа [<размер>, <расширение>]
    для всех файлов находящихвсе в 'path'
    :param path: имя проверяемой папки
    :return: list
    """
    return_data = []
    for data in os.walk(path):
        for file in data[2]:
            _, ex = file.split(".")
            return_data.append([os.stat('/'.join([data[0], file])).st_size, ex])
    return return_data


def counter(path: str) -> dict:
    """
    считает количество файлов в 'path' по размеру в байтах кратному 10
    :param path: имя проверяемой папки
    :return: dict
    """
    dictionary = {}
    for item in size_of_files(path):
        count = 10
        while True:
            if item[0] < count:
                if count in dictionary:
                    dictionary[count] += 1
                else:
                    dictionary[count] = 1
                break
            count *= 10
    return dictionary


print(counter(folder))
