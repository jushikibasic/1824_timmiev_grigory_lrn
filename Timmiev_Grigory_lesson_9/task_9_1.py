import time


class TrafficLight:
    __color: dict = {'красный': 7, 'желтый': 2, 'зеленый': 10}

    def running(self):
        for key in self.__color:
            color = key
            timing = self.__color[key]
            while timing:
                print(color, timing)
                time.sleep(1)
                timing -= 1


broad_street = TrafficLight()
broad_street.running()
