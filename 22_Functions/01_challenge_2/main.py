def ar_progr(num):
    if num == 1:
        print(1)
        return 1
    ar_progr(num - 1)
    print(num)
    return num


ar_progr(int(input('Введите число: ')))

