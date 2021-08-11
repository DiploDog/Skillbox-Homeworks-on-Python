order_am = int(input('Введите количество заказов: '))

orders_dict = dict()

for i_order in range(order_am):

    print(i_order + 1, 'заказ:', end=' ')
    order = input().split()

    if not order[0] in orders_dict:
        orders_dict[order[0]] = {order[1]: int(order[2])}
    elif not order[1] in orders_dict.get(order[0]):
        orders_dict[order[0]][order[1]] = int(order[2])
    else:
        orders_dict[order[0]][order[1]] += int(order[2])

for client in orders_dict:
    print('{}:'.format(client))
    for pizza in orders_dict[client]:
        print(' ' * 7, '{}:'.format(pizza), orders_dict[client].get(pizza))
