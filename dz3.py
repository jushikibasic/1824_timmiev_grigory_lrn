#3
numb = 1
while numb < 101:
    if numb % 10 == 0 or numb % 10 == 5 or numb % 10 == 6 or numb % 10 == 7 or numb % 10 == 8 or numb % 10 == 9:
        print(numb, 'процентов')
    elif 10 < numb < 15:
        print(numb, 'процентов')
    elif numb % 10 == 1:
        print(numb, 'процент')
    else:
        print(numb, 'процента')
    numb += 1
