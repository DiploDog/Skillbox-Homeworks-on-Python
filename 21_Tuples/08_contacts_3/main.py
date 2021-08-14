def add_cont(cont: list) -> str:
    cont_data = [(cont[0], cont[1]), cont[2]]
    if cont_data[0] not in contacts:
        contacts[cont_data[0]] = cont_data[1]
        return '\nКонтакт успешно добавлен!'
    else:
        return '\nЭтот человек уже есть в списке ваших контактов!'


def cont_search(surname: str, person: tuple) -> bool:
    if person[0].startswith(surname):
        return True


contacts = dict()

while True:
    act = int(input('Выберете действие\n(1 - добавить контакт, 2 - поиск по фамилии): '))
    if act == 1:
        contact = input('Введите данные контакта: ').split()
        print(add_cont(contact), '\nТекущий список контактов:')
        for guy, num in contacts.items():
            print(guy[0], guy[1], '-', num)
        print()
    if act == 2:
        surname = input('Введите фамилию: ').capitalize()
        for person in contacts:
            if cont_search(surname, person):
                print(person[0], person[1], contacts.get(person))
        print()


