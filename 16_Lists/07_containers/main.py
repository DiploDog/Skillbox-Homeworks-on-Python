cont_quant = int(input('Количество контейнеров: '))
cont_list = []
while len(cont_list) != cont_quant:
    cont = int(input('Введите вес контейнера: '))
    if cont < 0 or cont > 200:
        print('Ошибка! Такие контейнеры нельзя разместить на складе!')
    else:
        cont_list.append(cont)


new_cont = int(input('\nВведите вес нового контейнера: '))
if new_cont < 0 or new_cont > 200:
    print('\nОшибка! Такие контейнеры нельзя разместить на складе!')
else:
    for pos in range(cont_quant):
        if new_cont > cont_list[0]:
            print('\nНомер, куда встанет новый контейнер:', pos + 1)
            break
        elif cont_list[pos] > new_cont > cont_list[pos + 1]:
            print('\nНомер, куда встанет новый контейнер:', pos + 2)
            break
        elif new_cont == cont_list[pos] and new_cont > cont_list[pos + 1]:
            print('\nНомер, куда встанет новый контейнер:', pos + 2)
            break
        elif new_cont < cont_list[cont_quant - 1]:
            print('\nНомер, куда встанет новый контейнер:', cont_quant + 1)
            break

