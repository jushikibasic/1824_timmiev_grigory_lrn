def thesaurus_adv(*args: str) -> dict:
    """
    Принимает на вход имена и фамилии и создает из них словарь с ключем по первой букве фамилии
    и вложенный словарь с ключем по первой букве имени
    """
    names_dictionary = {}
    for name in args:
        if (name.split()[-1])[0] in names_dictionary:
            if name[0] in names_dictionary[(name.split()[-1])[0]]:
                old_name = names_dictionary[(name.split()[-1])[0]][name[0]]
                names_dictionary[(name.split()[-1])[0]][name[0]] = [old_name, name]
            else:
                (names_dictionary[(name.split()[-1])[0]]).setdefault(name[0], [name])
        else:
            names_dictionary.setdefault((name.split()[-1])[0], {name[0]: name})
    return names_dictionary


from pprint import pprint
names_list = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
result_dict = thesaurus_adv(*names_list)
list_keys = list(result_dict.keys())
list_keys.sort()
for i in list_keys:
    print(f'"{i}": {result_dict[i]}')
pprint(result_dict)
