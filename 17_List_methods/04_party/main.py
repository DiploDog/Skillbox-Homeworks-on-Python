guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    guest_status = input('Гость пришел или ушел? ')
    if guest_status == 'пришел':
        guest_name = input('Имя гостя: ')
        if len(guests) < 6:
            guests.append(guest_name)
            print('Привет,', guest_name + '!')
        else:
            print('Прости,', guest_name + ', но места нет :(')
    elif guest_status == 'ушел':
        guest_name = input('Имя гостя: ')
        print('Пока,', guest_name + '!')
        guests.remove(guest_name)
    elif guest_status == 'пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break