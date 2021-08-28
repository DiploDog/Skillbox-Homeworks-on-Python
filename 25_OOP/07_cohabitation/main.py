import random


class Man:

    def __init__(self, name, satiety):
        self.name = name
        self.satiety = satiety

    def work(self):
        self.satiety -= 10
        House.nightstand_money += 5
        print(
            '{} поработал и получил 25 кредитов. Остаток: {} кредитов'.format(
                self.name, House.nightstand_money
            )
        )

    def eat(self):
        self.satiety += 15
        House.freezer_food -= 10
        print(
            '{} поел и восстановил силы. Сытость: {}'.format(
                self.name, self.satiety
            )
        )

    def play(self):
        self.satiety -= 5
        print(
            '{} поиграл. Сытость: {}'.format(
                self.name, self.satiety
            )
        )

    def shopping(self):
        House.freezer_food += 20
        House.nightstand_money -= 10
        print(
            '{} сходил в магазин. Остаток еды: {}, остаток кредитов: {}'.format(
                self.name, House.freezer_food, House.nightstand_money
            )
        )


class House:

    nightstand_money = 0
    freezer_food = 50


def research(man_1, man_2):
    days = 0
    while days < 366:
        print('День', days)
        if man_1.satiety < 0:
            print('{} умер. Эксперимент завершен.'.format(man_1.name))
            break
        elif man_2.satiety < 0:
            print('{} умер. Эксперимент завершен.'.format(man_2.name))
            break
        else:

            cube = random.randint(1, 6)

            if man_1.satiety < 20:
                man_1.eat()
                days += 1
            elif man_2.satiety < 20:
                man_2.eat()
                days += 1
            if House.freezer_food < 10:
                man_1.shopping()
                man_2.shopping()
                days += 1
            elif House.nightstand_money < 50:
                man_1.work()
                man_2.work()
                days += 1
            elif cube == 1:
                man_1.work()
                man_2.work()
                days += 1
            elif cube == 2:
                man_1.eat()
                man_2.eat()
                days += 1
            else:
                man_1.play()
                man_2.play()
                days += 1
    else:
        print(
            'Эксперимент удался!\nИтоги:\nОстаток кредитов: {}\n'
            'Остаток еды: {}\nСытость {} - {}\nСытость {} - {}'.format(
                House.nightstand_money, House.freezer_food,
                man_1.name, man_1.satiety, man_2.name, man_2.satiety
            )
        )


man_1 = Man('Jack', 50)
man_2 = Man('Peter', 100)

research(man_1, man_2)
