import sys
from itertools import zip_longest


def line_to_list(file):
    data = []
    for line in file:
        string = line.strip()
        data.append(string)
    return data


def user_hobby_fn(file_1, file_2, file_3):
    with open(file_1, 'r', encoding='utf-8') as fr:
        users = line_to_list(fr)
    with open(file_2, 'r', encoding='utf-8') as fr:
        hobby = line_to_list(fr)
    if len(users) < len(hobby):
        sys.exit(1)
    else:
        result = dict(zip_longest(users, hobby[:len(users)]))
        with open(file_3, 'w+', encoding='utf-8') as fw:
            for key, val in result.items():
                _ = f'{key}: {val}\n'
                fw.write(_)


users_file = 'Chache/users.csv'
hobby_file = 'Chache/hobby.csv'
user_hobby = 'Chache/users_hobby.txt'
user_hobby_fn(users_file, hobby_file, user_hobby)
