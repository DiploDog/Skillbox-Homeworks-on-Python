file = open('first_tour.txt', 'r')
new_file = open('second_tour.txt', 'w')
min_score = int(file.read(2))
participants = dict()
file.seek(3)

for i_line in file:
    a_line = i_line.split()
    print(a_line)
    participants[int(a_line[2])] = (a_line[1][:1] + '.', a_line[0])

new_dict = dict()
score_list = sorted(participants)

for i_score in range(len(score_list) - 1, -1, -1):
    if score_list[i_score] > min_score:
        new_dict[score_list[i_score]] = participants.get(score_list[i_score])

print(new_dict)
new_file.write(str(len(new_dict)))
new_file.write('\n')
i = 1

for i_score, value in new_dict.items():
    data = new_dict.get(i_score)
    new_file.write('{pos}) {name} {surname}: {score}\n'.format(
        pos=i,
        name=data[0],
        surname=data[1],
        score=i_score
    ))
    i += 1

file.close()
new_file.close()
