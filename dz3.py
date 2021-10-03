#3
numb = 1
while numb < 101:
    if numb % 10 == 0 or numb % 10 in range(5, 10) or 10 < numb < 15:
        print(numb, 'процентов')
    elif numb % 10 == 1:
        print(numb, 'процент')
    else:
        print(numb, 'процента')
    numb += 1
