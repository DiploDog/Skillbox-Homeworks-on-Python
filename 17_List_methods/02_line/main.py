first_grade = list(range(160, 177, 2))
second_grade = list(range(162, 181, 3))
first_grade.extend(second_grade)

for i in range(len(first_grade)):
    for j in range(i + 1, len(first_grade)):
        if first_grade[i] > first_grade[j]:
            first_grade[i], first_grade[j] = first_grade[j], first_grade[i]

print(first_grade)