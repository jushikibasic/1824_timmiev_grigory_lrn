thesaurus_adv = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

names_dictionary = {}
for name in thesaurus_adv:
    if (name.split()[-1])[0] in names_dictionary:
        if name[0] in names_dictionary[(name.split()[-1])[0]]:

            old_name = names_dictionary[(name.split()[-1])[0]]
        old_name = names_dictionary[(name.split()[-1])[0]]
        names_dictionary[(name.split()[-1])[0]] = [*old_name, name]

    else:
        names_dictionary.setdefault((name.split()[-1])[0], {name[0]: name})
#    if name[0] in names_dictionary:
#        old_name = names_dictionary[name[0]]
#        names_dictionary[name[0]] = [*old_name, name]
#    else:
#        names_dictionary.setdefault(name[0], [name])
print(names_dictionary)