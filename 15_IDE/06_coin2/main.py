
def coin_search(x, y, r):
    import math
    if math.sqrt(x ** 2 + y ** 2) - r < 1e-15:
        print('Монетка где-то рядом!')
        flag = False
    else:
        print('Монетки нет в области')


flag = True
while flag:
    x = float(input('Введите координату x монетки: '))
    y = float(input('Введите координату y монетки: '))
    r = float(input('Введите радиус: '))
    coin_search(x, y, r)
    print()