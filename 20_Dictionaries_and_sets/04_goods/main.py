goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for good in goods:

    curr_good = goods.get(good)
    summ_amount = 0
    summ_price = 0

    for value in store[curr_good]:
        summ_amount += value.get('quantity')
        summ_price += value.get('price') * value.get('quantity')

    print('{label} - {quantity} шт, '
          'стоимость {total_price} руб.'.format(
        label=good,
        quantity=summ_amount,
        total_price=summ_price
    ))
