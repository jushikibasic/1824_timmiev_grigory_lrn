src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_numbs = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique_numbs.add(el)
    else:
        unique_numbs.discard(el)
    tmp.add(el)
unique_numbs_ord = [el for el in src if el in unique_numbs]
print(unique_numbs_ord)
