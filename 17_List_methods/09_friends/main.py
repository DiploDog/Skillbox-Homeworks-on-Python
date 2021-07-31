N = int(input('Количество друзей: '))
K = int(input('Долговых расписок: '))
friends = []
for i in range(N):
    temp_list = []
    temp_list.append(i + 1)
    temp_list.append(0)
    friends.append(temp_list)

for i_iou in range(K):
    print()
    print(i_iou + 1, 'расписка')
    to_whom = int(input('Кому: '))
    from_who = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends[to_whom - 1][1] += how_much
    friends[from_who - 1][1] -= how_much

print('\nБаланс друзей:')
for i_friend in range(N):
    print(friends[i_friend][0], ':', friends[i_friend][1])