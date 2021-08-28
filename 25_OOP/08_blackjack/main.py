import random


class Two:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Двойка'
    value = 2
    random.shuffle(suits)
    pick = suits.pop()


class Three:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Тройка'
    value = 3
    random.shuffle(suits)
    pick = suits.pop()


class Four:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Четверка'
    value = 4
    random.shuffle(suits)
    pick = suits.pop()


class Five:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Пятерка'
    value = 5
    random.shuffle(suits)
    pick = suits.pop()


class Six:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Шестерка'
    value = 6
    random.shuffle(suits)
    pick = suits.pop()


class Seven:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Семерка'
    value = 7
    random.shuffle(suits)
    pick = suits.pop()


class Eight:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Восьмерка'
    value = 8
    random.shuffle(suits)
    pick = suits.pop()


class Nine:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Девятка'
    value = 9
    random.shuffle(suits)
    pick = suits.pop()


class Ten:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Пятерка'
    value = 5
    random.shuffle(suits)
    pick = suits.pop()


class Jack:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Валет'
    value = 10
    random.shuffle(suits)
    pick = suits.pop()


class Queen:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Дама'
    value = 10
    random.shuffle(suits)
    pick = suits.pop()


class King:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Король'
    value = 10
    random.shuffle(suits)
    pick = suits.pop()


class Ace:
    suits = ['бубны', 'червы', 'трефы', 'пики']
    name = 'Туз'
    value = 11
    random.shuffle(suits)
    pick = suits.pop()


def shuffle():
    cards_list = [Two, Three, Four, Five, Six, Seven, Eight,
                  Nine, Ten, Jack, Queen, King, Ace]
    random.shuffle(cards_list)
    return cards_list[0]


def check(card_tpl):
    if card_tpl in your_cards_list or card_tpl in comp_cards_list:
        return True
    return False


your_cards_list = []
comp_cards_list = []
your_score = 0
comp_score = 0

answer = input('Нажмите любую кнопку для начала игры')
while answer != 'нет':

    if len(your_cards_list) != 0:
        print('Ваша рука: ', your_score)

        for i_card in your_cards_list:
            print(i_card[0], i_card[1])
        print('Стоимость руки:', your_score)

    answer = input('\nТянуть карту? ').lower()

    if answer == 'да':
        your_card = shuffle()
        while check((your_card.name, your_card.pick)) is True:
            your_card = shuffle()
        if your_card == Ace and your_score >= 20:
            your_card.value = 1
        print(
            'Вы вытянули {}. Масть: {}\n'.format(
                your_card.name, your_card.pick
            )
        )
        your_cards_list.append((your_card.name, your_card.pick))
        your_score += your_card.value

        print('\nХод компьютера...\n')
        if comp_score < 17:
            comp_card = shuffle()
            while check((comp_card.name, comp_card.pick)) is True:
                comp_card = shuffle()
            if comp_card == Ace and comp_score >= 20:
                comp_card.value = 1
            comp_cards_list.append((comp_card.name, comp_card.pick))
            comp_score += comp_card.value
        else:
            continue


if (comp_score < your_score <= 21) or your_score <= 21 < comp_score:
    print('\nВы победили!\nСчет: {}(Вы):{}'.format(your_score, comp_score))
else:
    print('\nКомпьютер победил!\nСчет: {}(Вы):{}'.format(your_score, comp_score))

print('\nРука компьютера:')
for i_card in comp_cards_list:
    print(i_card[0], i_card[1])
