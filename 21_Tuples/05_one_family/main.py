family_membs = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Петров', 'Даниил'): 99,
    ('Петрова', 'Галина'): 25,
    ('Петров', 'Петр'): 7
}

surname = input('Введите фамилию: ').capitalize()
for i_member in family_membs:
    if i_member[0].startswith(surname):
        print(i_member[0], i_member[1], family_membs.get(i_member))
