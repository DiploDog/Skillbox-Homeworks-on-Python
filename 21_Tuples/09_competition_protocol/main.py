def top_boys(score_dict: dict, prev_name: set) -> tuple:
    """Удаляет и возвращает значение ключа с максимальным результатом"""
    max_score = 0
    person_key = ''
    for key in score_dict:
        if int(score_dict.get(key)[0]) > max_score and \
                score_dict.get(key)[1] not in prev_name:
            max_score = int(score_dict.get(key)[0])
            person_key = key

    return score_dict.pop(person_key)


protoc_rec = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
protoc_dict = {num: 0 for num in range(1, protoc_rec + 1)}  # Инициализируем словарь с игроками

for rec in protoc_dict:
    print(rec, 'запись:', end=' ')
    protoc_dict[rec] = tuple(input().split())  # Присваиваем индексу(ключу в словаре) игрока кортеж с очками и именем

print('\nИтоги соревнований:')
place = 1
previous_win = set()  # Инициализируем множество с именами победителей, чтобы избежать повторений в результате

while place < 4:
    score, name = top_boys(protoc_dict, previous_win)
    print(place, 'место. {player} ({points})'.format(
        player=name,
        points=score
    ))
    previous_win.add(name)
    place += 1
