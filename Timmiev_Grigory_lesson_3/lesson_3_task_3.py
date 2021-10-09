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


name_list = ("Иван", "Артём", "Мария", "Петр", "Илья", "Маша", "Потап", "Алексей")
result_dict = thesaurus(*name_list)
list_keys = list(result_dict.keys())
list_keys.sort()
for i in list_keys:
    print(f'"{i}": {result_dict[i]}')
