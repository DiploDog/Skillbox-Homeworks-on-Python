sym_sum = 0
line_count = 0
error = 'Ошибка! В строке {} длина имени меньше 3-х символов'

with open('people.txt', 'r') as file:
    for i_line in file:
        try:
            line_count += 1
            sym_sum += len(i_line) - 1
            if len(i_line) - 1 < 3:
                with open('errors.log', 'a') as er_logs:
                    er_logs.write(error.format(line_count) + '\n')
                    raise ValueError

        except ValueError:
            print((error.format(line_count)))

print('Общее количество символов:', sym_sum)
