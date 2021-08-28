import math


class Circle:

    def __init__(self, name='окружность', x=0.0, y=0.0, r=1.0):
        self.name = name
        self.x, self.y, self.r = x, y, r
        self.s, self.p = round(math.pi * self.r ** 2, 2), round(2 * math.pi * self.r, 2)

    def square(self):
        self.s = round(math.pi * self.r ** 2, 2)
        return self.s

    def perimeter(self):
        self.p = round(2 * math.pi * self.r, 2)
        return self.p

    def increase(self, k):
        self.s *= k
        self.r = round(math.sqrt(self.s / math.pi), 2)
        self.p = self.perimeter()

    def intersection(self, circle):
        center_distance = math.sqrt((self.x - circle.x) ** 2 + (self.y - circle.y) ** 2)
        if abs(center_distance - self.r + circle.r) < 10e-10:
            print('{} пересекает {}'.format(self.name, circle.name))
        elif (center_distance < self.r + circle.r) and (center_distance > abs(self.r - circle.r)):
            print('{} пересекает {}'.format(self.name, circle.name))
        elif abs(center_distance - self.r - circle.r) < 10e-10:
            print('{} пересекает {}'.format(self.name, circle.name))
        else:
            print('Пересечений не обнаружено\n')

    def circle_info(self):
        print(
            '\n{}\n(X, Y) = ({}, {})\nR = {}\nS = {}\nP = {}\n'.format(
                self.name, self.x, self.y, self.r, self.s, self.p
            )
        )


circ_1 = Circle('Окружность А')
circ_1.circle_info()

print(circ_1.perimeter())
print(circ_1.square())
circ_2 = Circle('Окружность B', x=0.5)
circ_2.circle_info()
circ_3 = Circle('Окружность C', x=2, y=1, r=5)
circ_3.circle_info()

circ_2.intersection(circ_1)

circ_3.intersection(circ_1)

circ_1.increase(2)
circ_1.circle_info()
