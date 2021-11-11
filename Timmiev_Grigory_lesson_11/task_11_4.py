class Tech:
    def __init__(self, name: str):
        self.name = name


class Printer(Tech):
    def __init__(self, name: str, print_sp: int, is_color: bool):
        super(Printer, self).__init__(name)
        self.print_sp = print_sp
        self.is_color = is_color

    def __str__(self):
        return f'Принтер:({self.name})'


class Scanner(Tech):
    def __init__(self, name: str, scan_res: int):
        super(Scanner, self).__init__(name)
        self.scan_resolution = scan_res

    def __str__(self):
        return f'Сканер:({self.name})'


class MFU(Tech):
    def __init__(self, name: str, pr_sp: int):
        super(MFU, self).__init__(name)
        self.is_color = False
        self.pr_sp = pr_sp

    def __str__(self):
        return f'Копир:({self.name})'


class TechWarehouse:
    def __init__(self, name):
        self.title = name
        self.p_list: set = set()
        self.s_list: set = set()
        self.x_list: set = set()

    def __str__(self):
        return f'{self.title}'

    def accept_to_ware(self, *args):
        for tech in args:
            if not isinstance(tech, Tech):
                print(f'На складе может храниться только оргтехника')
                continue
            if isinstance(tech, Printer):
                self.p_list.add(tech)
            if isinstance(tech, Scanner):
                self.s_list.add(tech)
            if isinstance(tech, MFU):
                self.x_list.add(tech)

    def move_technics(self, type_of: str, count: int, place_out):
        if not type(count) == int:
            raise ValueError('Not int')
        if type_of.capitalize() == 'Printer':
            if len(place_out.p_list) < count:
                print(f' на {place_out} не достаточно техники этого типа')
            else:
                num = count
                while num != 0:
                    swap = place_out.p_list.pop()
                    self.p_list.add(swap)
                    num -= 1
                print(f'{count} объектов было перемещено из {place_out} на {self}')
        if type_of.capitalize() == 'Scanner':
            if len(place_out.s_list) < count:
                print(f' на {place_out} не достаточно техники этого типа')
            else:
                num = count
                while num != 0:
                    swap = place_out.s_list.pop()
                    self.s_list.add(swap)
                    num -= 1
                print(f'{count} объектов было перемещено из {place_out} на {self}')
        if type_of.capitalize() == 'Xerox':
            if len(place_out.x_list) < count:
                print(f' на {place_out} не достаточно техники этого типа')
            else:
                num = count
                while num != 0:
                    swap = place_out.x_list.pop()
                    self.x_list.add(swap)
                    num -= 1
                print(f'{count} объектов было перемещено из {place_out} на {self}')
        else:
            print(f' допускаются только типы: "printer", "scanner", "xerox"')

    def move_to(self, name, place_out):
        if isinstance(name, Printer):
            if name in place_out.p_list:
                place_out.p_list.discard(name)
                self.p_list.add(name)
                print(f'{name} был перемещен из {place_out} на {self}')
            else:
                print(f'{name} отсутствует на {place_out}')
        if isinstance(name, Scanner):
            if name in place_out.s_list:
                place_out.s_list.discard(name)
                self.s_list.add(name)
                print(f'{name} был перемещен из {place_out} на {self}')
            else:
                print(f'{name} отсутствует на {place_out}')
        if isinstance(name, MFU):
            if name in place_out.x_list:
                place_out.x_list.discard(name)
                self.x_list.add(name)
                print(f'{name} был перемещен из {place_out} на {self}')
            else:
                print(f'{name} отсутствует на {place_out}')

    def show_tech(self):
        print(f'В отделении "{self.title}"'
              f' находится {len(self.s_list) + len(self.p_list) + len(self.x_list)} объект(а/ов):')
        for item in self.p_list:
            print(f'{item}')
        for item in self.s_list:
            print(f'{item}')
        for item in self.x_list:
            print(f'{item}')


class Division(TechWarehouse):
    pass


typography = Division('Типография')
wh = TechWarehouse('Склад')
printer1 = Printer('Canon', 12, True)
printer2 = Printer('Canon', 12, True)
scanner1 = Scanner('No name', 1200)
scanner2 = Scanner('No name', 1200)
xerox1 = MFU('Xerox', 120)
xerox2 = MFU('Xerox', 120)
xerox3 = MFU('Xerox', 120)
wh.accept_to_ware(printer1, printer2, scanner1, scanner2, xerox1, xerox2, xerox3)
typography.move_to(xerox1, wh)
typography.show_tech()
wh.show_tech()
wh.move_to(xerox1, typography)
wh.show_tech()
wh.move_to(xerox1, typography)
typography.move_technics('xerox', 2, wh)
typography.show_tech()
