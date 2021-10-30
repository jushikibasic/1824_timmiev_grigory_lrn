class Car:

    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self.actual_speed = 0

    def go(self):
        self.actual_speed = self.speed
        return print(f'Машина {self.name}, поехала')

    def stop(self):
        self.actual_speed -= self.speed
        return print(f'Машина {self.name}, остановилась')

    def turn_left(self):
        if self.actual_speed > 0:
            return print(f'Машина {self.name}, повернула на лево')
        else:
            return print(f'Машина {self.name}: стоит, начните движение')

    def turn_right(self):
        if self.actual_speed > 0:
            return print(f'Машина {self.name}, повернула на право')
        else:
            return print(f'Машина {self.name}: стоит, начните движение')

    def show_speed(self):
        if self.actual_speed > 0:
            return print(f'Машина {self.name}, едет со скоростью:{self.actual_speed} км/час')
        if self.actual_speed == 0:
            return print(f'Машина {self.name}, стоит, скорость: 0 км/час')

    def police_or_not(self):
        if self.is_police:
            return print(f'Машина {self.name}, является служебной')
        else:
            return print(f'Машина {self.name}, не является служебной')


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super(TownCar, self).__init__(speed, color, name)

    def show_speed(self):
        if 0 < self.actual_speed <= 60:
            return print(f'Машина {self.name}, едет со скоростью:{self.actual_speed} км/час')
        if self.actual_speed > 60:
            return print(f'Превышение скорости {self.name}!\n'
                         f'Разрешенная скорость для класса {self.__class__.__name__}: 60 км/час\n'
                         f'Актуальная скорость: {self.actual_speed} км/час')
        if self.actual_speed == 0:
            return print(f'Машина {self.name}, стоит, скорость: 0 км/час')


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super(SportCar, self).__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super(WorkCar, self).__init__(speed, color, name)

    def show_speed(self):
        if 0 < self.actual_speed <= 40:
            return print(f'Машина {self.name}, едет со скоростью:{self.actual_speed} км/час')
        if self.actual_speed > 40:
            return print(f'Превышение скорости {self.name}!\n'
                         f'Разрешенная скорость для класса {self.__class__.__name__}: 40 км/час\n'
                         f'Актуальная скорость: {self.actual_speed} км/час')
        if self.actual_speed == 0:
            return print(f'Машина {self.name}, стоит, скорость: 0 км/час')


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super(PoliceCar, self).__init__(speed, color, name)
        self.is_police = True


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
sport_car.turn_left()
sport_car.turn_right()
town_car.police_or_not()
sport_car.police_or_not()
work_car.police_or_not()
police_car.police_or_not()
