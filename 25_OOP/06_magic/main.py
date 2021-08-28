class Water:

    def __init__(self):
        pass

    def __add__(self, other):
        if isinstance(other, Air):
            print('Вы получили Шторм!')
            return Storm()
        if isinstance(other, Fire):
            print('Вы получили Пар!')
            return Steam()
        if isinstance(other, Ground):
            print('Вы получили Грязь!')
            return Mud()
        return None


class Air:

    def __init__(self):
        pass

    def __add__(self, other):
        if isinstance(other, Water):
            print('Вы получили Шторм!')
            return Storm()
        if isinstance(other, Fire):
            print('Вы получили Молнию!')
            return Lightning()
        if isinstance(other, Ground):
            print('Вы получили Пыль!')
            return Dust()
        else:
            return None


class Fire:

    def __init__(self):
        pass

    def __add__(self, other):
        if isinstance(other, Water):
            print('Вы получили Пар!')
            return Steam()
        if isinstance(other, Air):
            print('Вы получили Молнию!')
            return Lightning()
        if isinstance(other, Ground):
            print('Вы получили Лаву!')
            return Lava()


class Ground:

    def __init__(self):
        pass

    def __add__(self, other):
        if isinstance(other, Water):
            print('Вы получили Грязь!')
            return Mud()
        if isinstance(other, Air):
            print('Вы получили Пыль!')
            return Dust()
        if isinstance(other, Fire):
            print('Вы получили Лаву!')
            return Lava()
        else:
            return None


class Storm:

    def __init__(self):
        pass

    def __add__(self, other):
        if isinstance(other, Storm):
            print('Вы получили Смерч!')
            return Tornado()
        else:
            return None

class Steam:

    def __init__(self):
        pass


class Mud:

    def __init__(self):
        pass


class Lightning:

    def __init__(self):
        pass


class Dust:

    def __init__(self):
        pass


class Lava:

    def __init__(self):
        pass


class Tornado:

    def __init__(self):
        pass


water = Water()
air = Air()
smth = water + air
smth_2 = smth + smth
smth_3 = water + smth