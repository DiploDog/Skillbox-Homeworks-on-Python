string = input('Введите строку с количеством h >= 2: ')

part_1 = string[:string.index('h') + 1]
part_2 = string[len(string):-string.index('h') - 2:-1][::-1]
part_mid = string[string.index('h') + 1:-string.index('h') - 1][::-1]
print(part_1 + part_mid + part_2)
