def is_man(man):
    if man not in famTree_dict:
        return 0
    else:
        return is_man(famTree_dict[man]) + 1


people_num = int(input('Введите количество человек: '))

famTree_dict = dict()

for i_pair in range(people_num - 1):
    print(i_pair + 1, 'пара:', end=' ')
    pair = input().split()
    famTree_dict[pair[0]] = pair[1]

heights = dict()
for man in set(famTree_dict.keys()).union(set(famTree_dict.values())):
    heights[man] = is_man(man)

print('\n"Высота" каждого члена семьи:')
for name in sorted(heights):
    print(name, heights.get(name))
