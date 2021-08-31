import math


class Auto:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, dist, my_angle):
        self.x = round(dist * math.cos(my_angle * math.pi / 180), 1)
        self.y = round(dist * math.sin(my_angle * math.pi / 180), 1)
        self.angle = my_angle

    def auto_info(self):
        return 'В данный момент автомобиль находится на точке [{:.1f};{:.1f}]'.format(
            self.x, self.y
        )


class Bus(Auto):
    def __init__(self, x, y, angle, passengers=0, money=0):
        super().__init__(x, y, angle)
        self.passengers = passengers
        self.money = money

    def move(self, dist, my_angle):
        self.x += round(dist * math.cos(my_angle * math.pi / 180), 1)
        self.y += round(dist * math.sin(my_angle * math.pi / 180), 1)
        self.angle = my_angle
        for i_km in range(dist):
            self.money += round(self.passengers * 4.5, 2)

    def enter(self, pass_amount):
        self.passengers += pass_amount

    def exit(self, pass_amount):
        try:
            self.passengers -= pass_amount
            if self.passengers < 0:
                raise ValueError(
                    '\nЧисло пассажиров не может быть отрицатльным!'
                )
        except ValueError as ve:
            print(ve)

    def bus_info(self):
        return '\nВ данный момент автобус находится на точке [{:.1f};{:.1f}]\n' \
               'Заработано денег: {:.2f} рублей\n' \
               'Текущее число пассажиров в автобусе: {}'.format(
                self.x, self.y, self.money, self.passengers
                )


bus = Bus(x=0, y=0, angle=0)
print(bus.bus_info())
bus.move(10, 30)
print(bus.bus_info())
bus.enter(5)
print(bus.bus_info())
bus.move(10, 60)
print(bus.bus_info())
bus.move(30, 110)
print(bus.bus_info())
bus.exit(2)
bus.move(30, 110)
print(bus.bus_info())
bus.exit(4)

