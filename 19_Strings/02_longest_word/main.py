string = input('Введите строку: ').split()
print('\nСамое длинное слово:', max(string, key=len))
print('Его длина -', len(max(string, key=len)), 'символов.')
