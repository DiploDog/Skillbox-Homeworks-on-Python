import os


def gen_files_path(directory, catalog):
    for element in os.listdir(directory):
        new_dir = os.path.join(directory, element)
        if os.path.isfile(new_dir):
            yield new_dir
        elif new_dir.endswith(catalog):
            print(
                'Директория найдена!: {}'.format(
                    new_dir
                )
            )
            return


my_dir = input('Введите путь до директории: ')
my_catalog = input('Введите искомый каталог: ')
for i_dir in gen_files_path(my_dir, my_catalog):
    print(i_dir)
