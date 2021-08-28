from random import randint
import time


class Parent:

    feed_time = 0

    def __init__(self, relation: str, name: str, age: int):
        self.relation = relation
        self.name = name
        self.age = age
        self.children = []

    def parent_info(self):
        print(
            '\nСтепень родства: {}\nИмя: {}\nВозраст: {}\nДети: {}\n'.format(
                self.relation, self.name, self.age, self.children
            )
        )

    def calm_down_kid(self, child):
        if child.calm is False:
            child.calm = True
            print(
                '{} успокоил(а) {}\n'.format(
                    self.name, child.name
                )
            )
        else:
            print('Ребенок итак спокоен.\n')

    def feed_the_kid(self, child):
        if child.hunger is False:
            Parent.feed_time += 1
            print(
                '{} {} покормил(а) ребенка по имени {}'.format(
                    self.relation, self.name, child.name
                )
            )
            if Parent.feed_time > 2:
                print('\n{} переел(а), нужен Мезим!\n'.format(child.name))
        else:
            print(
                '{} {} покормил(а) ребенка по имени {}'.format(
                    self.relation, self.name, child.name
                )
            )
            Parent.feed_time = 0
            child.hunger = False

    def add_a_child(self, another_parent, child):
        if self.age - child.age >= 16 and another_parent.age - child.age >= 16:
            self.children.append(child.name)
            another_parent.children.append(child.name)
        else:
            print('\nПотенциальные родители еще слишком молоды!\n')


class Child:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.calm = True
        self.hunger = False

    def kid_info(self):
        print(
            '\nИмя: {}\nВозраст: {}\n'.format(
                self.name, self.age
            )
        )

    def is_parent(self, parent):
        if isinstance(parent, Parent) and self.name in parent.children:
            print(
                'Да, {} - {} для ребенка по имени {}\n'.format(
                    parent.name, parent.relation, self.name
                )
            )
        else:
            print(
                'Нет, для ребенка по имени {}, {} - простой прохожий...'.format(
                    self.name, parent
                )
            )

    def crying(self):
        possibility = randint(0, 1)
        if possibility:
            self.hungry()
        else:
            self.frustrated()
        if self.age < 4:
            print('\nРебенок {} плачет! Однако непонятно, что ему требуется!'.format(self.name))
        else:
            print('\nПусть сперва успокоится и расскажет, что произошло. Уже не маленький!')
            time.sleep(5)
            if self.calm is False:
                self.calm = True
                print('\nРебенок сам успокоился!\n')
            if self.hunger is True:
                print('\nРебенок хочет есть!\n')

    def hungry(self):
        self.hunger = True

    def frustrated(self):
        self.calm = False


# Test
mother = Parent('Мать', 'Джессика', 30)
father = Parent('Отец', 'Колин', 32)
mother.parent_info()
father.parent_info()
kid_1 = Child('Рассел', 10)
kid_2 = Child('Мэри', 3)
mother.add_a_child(father, kid_1)
father.add_a_child(mother, kid_2)
mother.parent_info()
father.parent_info()
kid_1.kid_info()
kid_2.is_parent(mother)
kid_1.is_parent('Робин')
kid_1.crying()
kid_2.hungry()
mother.feed_the_kid(kid_2)

for _ in range(3):
    mother.feed_the_kid(kid_1)

kid_2.frustrated()
time.sleep(2)
father.feed_the_kid(kid_2)
father.calm_down_kid(kid_2)
father.calm_down_kid(kid_2)
father_1 = Parent('Отец', kid_2.name, kid_2.age)
mother_1 = Parent('Мать', 'Кэтрин', 90)
father_1.add_a_child(mother_1, kid_2)