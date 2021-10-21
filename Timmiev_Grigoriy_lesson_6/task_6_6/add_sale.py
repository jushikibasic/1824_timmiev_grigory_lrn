def ad_sale(argv):
    program, arg = argv
    with open('sales.txt', 'a', encoding='utf-8') as fw:
        fw.write(f'{arg}\n')


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        sys.exit(3)
    exit(ad_sale(sys.argv))
