import os.path


def your_path_info(route):

    for element in os.listdir(route):
        new_route = os.path.join(route, element)
        if os.path.isdir(new_route):
            subDir_dict['подкаталоги'] += 1
            your_path_info(new_route)
        if os.path.isfile(new_route):
            weight.append(os.path.getsize(new_route))


weight = []
subDir_dict = {'подкаталоги': 0}

my_path = '/Users/kron/python-ds'

your_path_info(my_path)
dir_size = sum(weight) / 1024
print('Размер каталога {:.2f} Кб:'.format(dir_size))
print('Количество подкаталогов:', subDir_dict.get('подкаталоги'))
print('Количество файлов:', len(weight))

