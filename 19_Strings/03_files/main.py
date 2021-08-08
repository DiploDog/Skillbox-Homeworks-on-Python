file_name = input('Введите название файла: ')
spec_sym = '@№$%^&*()'

if not file_name.endswith('.txt') and not file_name.endswith('.docx'):
    print('\nОшибка! неверное расширение файла. Ожидалось .txt или .docx')
else:
    for i in spec_sym:
        if file_name.startswith(i):
            print('\nОшибка: название начинается на один из специальных символов.')
            break
    else:
        print('\nФайл назван верно.')
