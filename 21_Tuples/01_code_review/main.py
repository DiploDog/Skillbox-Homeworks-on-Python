def interests_and_surname_len(guys_dict):

    interests = [
        interest
        for key in guys_dict
        for interest in guys_dict[key].get('interests', [])
    ]

    summ_names_len = 0
    for j_info in students.values():
        summ_names_len += len(j_info.get('surname', ''))

    return interests, summ_names_len


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

for index, i_info in students.items():
    print(index, '-', i_info.get('age'))

int_list, surn_len = interests_and_surname_len(students)
print('Список интересов студентов:', int_list,
      '\nОбщая длина фамилий студентов:', surn_len)
