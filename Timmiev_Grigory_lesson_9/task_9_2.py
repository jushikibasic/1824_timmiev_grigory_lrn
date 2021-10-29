class Road:
    def __init__(self, length: int, width: int):
        """
        при инициализации указывается
        :param length: длинна в метрах
        :param width: ширина в метрах
        """
        self._length = length
        self._width = width

    def mass_of_materials(self, high: int, mass_m_2: int) -> int:
        """
        считает масу массу асфальта, необходимого для покрытия всей дороги в тоннах
        :param high: высота дорожного полотна в сантиметрах
        :param mass_m_2: масса в кг квадратного метра дороги высотой 1 см
        :return: mass
        """
        mass = int((self._width * self._length * mass_m_2 * high) / 1000)
        return mass


krd_msk = Road(1400, 20)
print(f'{krd_msk.mass_of_materials(5, 25)} т.')
