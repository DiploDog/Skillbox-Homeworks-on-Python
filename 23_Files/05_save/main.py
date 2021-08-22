import os

text = input('Введите строку: ')

print('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
dirs_seq = input().split()
my_path = os.path.sep.join(dirs_seq)

if os.path.exists(os.path.join(os.path.sep, my_path)):
    file_name = input('Введите имя файла: ')
    while True:
        if os.path.exists(os.path.join(os.path.sep, my_path, file_name)):
            quest = input('Вы действительно хотите перезаписать файл? ').lower()
            if quest == 'да':
                file = open(os.path.join(os.path.sep, my_path, file_name), 'w')
                file.write(text)
                file.close()
                print('Файл успешно перезаписан!')
                break
            if quest == 'нет':
                file_name = input('Введите имя файла: ')
        if not os.path.exists(os.path.join(os.path.sep, my_path, file_name)):
            file = open(os.path.join(os.path.sep, my_path, file_name), 'w')
            file.write(text)
            file.close()
            print('Файл успешно записан!')
            break
else:
    print('Указанного пути не существует!')
