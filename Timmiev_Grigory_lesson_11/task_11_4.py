class Tech:
    def __init__(self, name: str, warehouse: set):
        self.warehouse = warehouse
        self.warehouse.add(self)
        self.name = name


class Printer(Tech):
    def __init__(self, name: str, warehouse: set, print_sp: int, is_color: bool):
        super(Printer, self).__init__(name, warehouse)
        self.print_sp = print_sp
        self.is_color = is_color

    def __str__(self):
        return f'Принтер:({self.name})\n'


class Scanner(Tech):
    def __init__(self, name: str, warehouse: set, scan_res: int):
        super(Scanner, self).__init__(name, warehouse)
        self.scan_resolution = scan_res

    def __str__(self):
        return f'Сканер:({self.name})\n'


class MFU(Tech):
    def __init__(self, name: str, warehouse: set, pr_sp: int):
        super(MFU, self).__init__(name, warehouse)
        self.is_color = False
        self.pr_sp = pr_sp

    def __str__(self):
        return f'Копир:({self.name})\n'


class TechWarehouse:
    def __init__(self, name):
        self.title = name
        self.tech_list: set = set()

    def __str__(self):
        return f'{self.title}'

    def accept_to_ware(self, *args):
        for tech in args:
            if not isinstance(tech, Tech):
                print(f'На складе может храниться только оргтехника')
                continue
            self.tech_list.add(tech)

    def move_to(self, name, place_out):
        if name in place_out.tech_list:
            place_out.tech_list.discard(name)
            self.tech_list.add(name)
        else:
            print(f'{name} отсутствует на {place_out}')

    def show_tech(self):
        print(f'В отделении "{self.title}" находится {len(self.tech_list)} объект(а/ов):')
        for item in self.tech_list:
            print(f'{item}\n')


class Division(TechWarehouse):
    pass


income = set()
typography = Division('Типография')
wh = TechWarehouse('Склад')
printer = Printer('Canon', income, 12, True)
scanner = Scanner('No name', income, 1200)
xerox = MFU('Xerox', income, 120)
wh.accept_to_ware(*income)
typography.move_to(xerox, wh)
typography.show_tech()
wh.show_tech()
wh.move_to(xerox, typography)
wh.show_tech()
wh.move_to(xerox, typography)
