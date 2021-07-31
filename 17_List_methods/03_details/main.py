shop = [
    ['каретка', 1200], ['шатун', 1000], ['седло', 300],
    ['педаль', 100], ['седло', 1500], ['рама', 12000],
    ['обод', 2000], ['шатун', 200], ['седло', 2700]
]

part = input('Название детали: ')
total_cost = 0
count = 0

for i in range(len(shop)):
    if shop[i][0] == part:
        total_cost += shop[i][1]
        count += 1

print('\nКоличество деталей -', count)
print('Общая стоимость -', total_cost)