class Stationery:

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        return print('"Запуск отрисовки"')


class Pen(Stationery):

    def __init__(self, title: str):
        super(Pen, self).__init__(title)

    def draw(self):
        return print(f'{self.title}: "Запуск письма"')


class Pencil(Stationery):

    def __init__(self, title: str):
        super(Pencil, self).__init__(title)

    def draw(self):
        return print(f'{self.title}: "Запуск черчения"')


class Handle(Stationery):

    def __init__(self, title: str):
        super(Handle, self).__init__(title)

    def draw(self):
        return print(f'{self.title}: "Запуск маркировки"')


thing = Stationery('Канцелярка')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
thing.draw()
pen.draw()
pencil.draw()
handle.draw()
