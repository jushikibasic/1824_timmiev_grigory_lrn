class Car:
    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = False
        self.actual_speed = 0

    def go(self):
        self.actual_speed = self.speed
        print(f'Машина {self.name}, поехала')

    def stop(self):
        self.actual_speed -= self.speed
        print(f'Машина {self.name}, остановилась')

    def turn(self, direction: str):
        if self.actual_speed > 0:
            print(f'Машина {self.name}, повернула на {direction}')
        else:
            print(f'Машина {self.name}: стоит, начните движение')

    def show_speed(self):
        if self.actual_speed > 0:
            print(f'Машина {self.name}, едет со скоростью:{self.actual_speed} км/час')
        if self.actual_speed == 0:
            print(f'Машина {self.name}, стоит, скорость: 0 км/час')

    def police_or_not(self):
        if self._is_police:
            print(f'Машина {self.name}, является служебной')
        else:
            print(f'Машина {self.name}, не является служебной')


class TownCar(Car):
    def show_speed(self):
        if 0 < self.actual_speed <= 60:
            print(f'Машина {self.name}, едет со скоростью:{self.actual_speed} км/час')
        if self.actual_speed > 60:
            print(f'Превышение скорости {self.name}!\n'
                  f'Разрешенная скорость для класса {self.__class__.__name__}: 60 км/час\n'
                  f'Актуальная скорость: {self.actual_speed} км/час')
        if self.actual_speed == 0:
            print(f'Машина {self.name}, стоит, скорость: 0 км/час')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if 0 < self.actual_speed <= 40:
            print(f'Машина {self.name}, едет со скоростью:{self.actual_speed} км/час')
        if self.actual_speed > 40:
            print(f'Превышение скорости {self.name}!\n'
                  f'Разрешенная скорость для класса {self.__class__.__name__}: 40 км/час\n'
                  f'Актуальная скорость: {self.actual_speed} км/час')
        if self.actual_speed == 0:
            print(f'Машина {self.name}, стоит, скорость: 0 км/час')


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super(PoliceCar, self).__init__(speed, color, name)
        self._is_police = True


town_car = TownCar(61, "Red", 'WW_Golf')
work_car = WorkCar(41, 'Yellow', 'BobCat')
police_car = PoliceCar(120, "Blue", 'BMW')
sport_car = SportCar(300, 'White', 'Ferrari')
town_car.go()
sport_car.go()
police_car.go()
town_car.show_speed()
town_car.stop()
work_car.go()
work_car.show_speed()
town_car.show_speed()
sport_car.turn('left')
sport_car.turn('right')
town_car.police_or_not()
sport_car.police_or_not()
work_car.police_or_not()
police_car.police_or_not()
