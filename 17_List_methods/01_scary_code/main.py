main = [1, 5, 3]
side_1 = [1, 5, 1, 5]
side_2 = [1, 3, 1, 5, 3, 3]
main.extend(side_1)
count_5 = 0
count_3 = 0
for i in main:
    if i == 5:
        main.remove(i)
        count_5 += 1
print('Количество цифр', 5, 'при первом объединении:', count_5)

main.extend(side_2)
for j in main:
    if j == 3:
        count_3 += 1
print('Количество цифр', 3, 'при первом объединении:', count_3)

print('Итоговый список:', main)