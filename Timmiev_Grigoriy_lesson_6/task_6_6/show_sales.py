def show_sales(argv):
    program, *arg = argv
    with open('bakery.csv', 'r', encoding='utf-8') as fr:
        lines = sum(1 for _ in fr)
        fr.seek(0)
        count = 1
        result = {}
        for line in fr:
            string = line.strip()
            key = str(count)
            result.setdefault(key, string)
            count += 1
        if len(sys.argv) == 1:
            print(*result.values(), sep="\n")
        elif len(sys.argv) == 2:
            print(arg)
            for i in range(int(arg[0]), lines + 1):
                print(result[f'{i}'])
        elif len(sys.argv) == 3:
            if int(arg[1]) > lines:
                for i in range(int(arg[0]), lines + 1):
                    print(result[f'{i}'])
            else:
                for i in range(int(arg[0]), int(arg[1]) + 1):
                    print(result[f'{i}'])


if __name__ == '__main__':
    import sys
    exit(show_sales(sys.argv))
