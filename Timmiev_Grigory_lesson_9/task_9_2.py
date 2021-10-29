class Road:
    def __init__(self, length: int, width: int):
        """
        при инициализации указывается
        :param length: длинна в метрах
        :param width: ширина в метрах
        """
        self._length = length
        self._width = width

    def mass_of_materials(self, high: int) -> str:
        """
        считает масу массу асфальта, необходимого для покрытия всей дороги в тоннах
        :param high: высота дорожного полотна в сантиметрах
        :return: <mass> т.: str
        """
        mass = f'{int((self._width * self._length * 25 * high) / 1000)} т.'
        return mass


krd_msk = Road(8000, 20)
print(krd_msk.mass_of_materials(5))
