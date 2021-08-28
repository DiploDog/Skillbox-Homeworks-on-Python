import random


class Unit:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def kick(self):
        self.hp -= 20
        return self.hp

    def battle(self, unit):
        health = unit.kick()
        print(
            '{} нанес 20 урона {}. Текущее здоровье последнего: {}'.format(
                self.name, unit.name, health
            )
        )

    def is_dead(self):
        if self.hp == 0:
            print('{} погиб.'.format(self.name))
            return True
        return False


unit_1 = Unit('Воин 1')
unit_2 = Unit('Воин 2')

while True:
    if unit_2.is_dead():
        break
    elif unit_1.is_dead():
        break

    var = random.randint(0, 1)
    if var:
        unit_1.battle(unit_2)
    else:
        unit_2.battle(unit_1)
