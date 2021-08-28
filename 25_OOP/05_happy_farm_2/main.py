import operator

from time import sleep


class Potato:

    ripe_level = {0: 'зеленая', 1: 'росток', 2: 'клубень', 3: 'зрелая'}

    def __init__(self, index):
        self.index = index
        self.ripe = 0

    def potato_info(self):
        print(
            'Картошка под номером {} - {}'.format(
                self.index, Potato.ripe_level.get(self.ripe)
            )
        )

    def grow(self):
        if self.ripe >= 3:
            print(
                'Картошка под номером {} созрела, можно собирать!'.format(
                    self.index
                )
            )
        else:
            self.ripe += 1
            print(
                'Теперь картошка {} - {}'.format(
                    self.index, Potato.ripe_level.get(self.ripe)
                )
            )


class Garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def garden_info(self):
        if len(self.potatoes) == 0:
            print('Грядка пуста!')
        else:
            for i_potato in self.potatoes:
                i_potato.potato_info()

    def grow_potato(self):
        for j_potato in self.potatoes:
            j_potato.grow()
        if all(j_potato.ripe >= 3 for j_potato in self.potatoes):
            print('Вся картошка созрела, можно собирать!')

    def reaped(self):
        if not len(self.potatoes):
            print('Картошка собрана. Засадите грядку!')
        else:
            print('На грядке есть картошка.')


class Gardener:

    harvest = []

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def water(self):
        print('Садовник {} полил грядку'.format(self.name))
        sleep(3)
        self.garden.grow_potato()

    def harv(self):
        Gardener.harvest.extend(self.garden.potatoes)
        self.garden.potatoes = []
        print(
            'Садовник {} собрал урожай. Теперь у него {} зрелых картофелин'.format(
                self.name, len(self.harvest)
            )
        )


for _ in range(2):
    gardener = Gardener('Jack', Garden(5))
    for _ in range(3):
        gardener.water()

    gardener.harv()
    gardener.garden.garden_info()
