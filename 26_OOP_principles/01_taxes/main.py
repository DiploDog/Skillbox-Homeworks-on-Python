class Property:
    def __init__(self, worth):
        self.worth = worth
        self.tax = round(self.worth / 100, 2)

    def calc_tax(self):
        return '\nНалог составит {} рублей'.format(
            self.tax
        )


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.tax = round(self.worth / 1000)

    def __str__(self):
        return 'квартира'


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.tax = round(self.worth / 200)

    def __str__(self):
        return 'авто'


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.tax = round(self.worth / 500)

    def __str__(self):
        return 'дом'


def can_you_buy(prop):
    total_cost = cost + prop.tax
    print(prop.calc_tax())
    difference = round(total_cost - wallet, 2)
    if difference > 0:
        print(
            '\nВам не хватает {} рублей для покупки.'.format(
                difference
            )
        )
    else:
        summary = wallet - total_cost
        print(
            '\nВы купили {}!\nОстаток на счете: {} руб.'.format(
                prop, summary
            )
        )


wallet = int(input('Введите свой бюджет, руб.: '))
prop = input('Имущество, которое Вы хотите приобрести (квартира, авто, дом): ').lower()
cost = int(input('Введите стоимость имущества, руб.: '))

if prop == 'квартира':
    prop = Apartment(cost)
    can_you_buy(prop)
elif prop == 'авто':
    prop = Car(cost)
    can_you_buy(prop)
elif prop == 'дом':
    prop = CountryHouse(cost)
    can_you_buy(prop)



