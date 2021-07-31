people_am = int(input('Количество человек: '))
rhyme_num = int(input('Какое число в считалке? '))
print('Значит выбывает каждый', rhyme_num, 'человек.')
guys_list = list(range(1, people_am + 1))
person_left = 0

while len(guys_list) > 1:
    print('\nТекущий круг людей:', guys_list)
    if person_left > len(guys_list) - 1:
        print('Начало счета с номера', guys_list[person_left % len(guys_list)])
    else:
        print('Начало счета с номера', guys_list[person_left])
    person_left = (rhyme_num + person_left - 1) % len(guys_list)
    print('Выбывает человек под номером', guys_list[person_left])

    guys_list.remove(guys_list[person_left])

print('\nОстался человек под номером:', guys_list[0])