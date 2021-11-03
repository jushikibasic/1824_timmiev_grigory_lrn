def ad_sale(argv):
    program, *arg = argv
    with open('bakery.csv', 'a', encoding='utf-8') as fw:
        for i in range(len(arg)):
            fw.write(f'{arg[i]}\n')


if __name__ == '__main__':
    import sys
    exit(ad_sale(sys.argv))

