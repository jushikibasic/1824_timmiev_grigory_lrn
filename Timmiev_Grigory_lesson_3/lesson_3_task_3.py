def thesaurus(*args: str) -> dict:
    """Принимает на вход имена и создает из них словарь с ключем по первой букве имен"""
    names_dictionary = {}
    for name in args:
        if name[0] in names_dictionary:
            old_name = names_dictionary[name[0]]
            names_dictionary[name[0]] = [*old_name, name]
        else:
            names_dictionary.setdefault(name[0], [name])
    return names_dictionary


name_list = ("Иван", "Мария", "Петр", "Илья", "Маша", "Потап")
for key, value in thesaurus(*name_list).items():
    print(f'"{key}": {value}')
