def exc_check(data_list):
    if len(data_list) != 3:
        raise IndexError
    if not data_list[0].isalpha():
        raise NameError
    if '@' not in data_list[1] or '.' not in data_list[1]:
        raise SyntaxError
    if not 10 <= int(data_list[2]) <= 99:
        raise ValueError


def err_type(string):
    bad = open('registration_bad.log', 'a', encoding='utf-8')
    bad.write(i_line[:-1] + string + '\n')
    bad.close()


with open('registrations.txt', 'r') as reg_logs:
    for i_line in reg_logs:
        try:
            data = i_line.split()
            res = exc_check(data)
        except IndexError:
            err_type(' - Отсутствует информация в полях')
        except NameError:
            err_type(' - Имя содержит не только буквы')
        except SyntaxError:
            err_type(' - Поле e-mail не содержит "@" или "."')
        except ValueError:
            err_type(' - Некорректный возраст')
        else:
            with open('registration_good.log', 'a', encoding='utf-8') as good:
                good.write(i_line + '\n')
