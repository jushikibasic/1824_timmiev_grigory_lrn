class Stationery:

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('"Запуск отрисовки"')


class Pen(Stationery):

    def draw(self):
        print(f'{self.title}: "Запуск письма"')


class Pencil(Stationery):

    def draw(self):
        print(f'{self.title}: "Запуск черчения"')


class Handle(Stationery):

    def draw(self):
        print(f'{self.title}: "Запуск маркировки"')


thing = Stationery('Канцелярка')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
thing.draw()
pen.draw()
pencil.draw()
handle.draw()
