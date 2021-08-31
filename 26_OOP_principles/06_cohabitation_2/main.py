import random
import logging

logging.basicConfig(filename='year_of_life.log', level=logging.INFO)
log_hus = logging.getLogger('husband')
log_wife = logging.getLogger('wife')
log_cat = logging.getLogger('cat')
common_log = logging.getLogger('family member')


class FamilyGuy:
    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.happiness = 100

    def eat(self):
        if self.satiety < 10:
            self.satiety += 30
            Storage.food -= 30
            common_log.info(
                '{} eaten 30 points of food'.format(
                    self.name
                )
            )
        else:
            food_eaten = random.randint(1, 30)
            self.satiety += food_eaten
            Storage.food -= food_eaten
            common_log.info(
                '{} eaten {} points of food'.format(
                    self.name, food_eaten
                )
            )

    def pet_the_cat(self):
        self.happiness += 5
        common_log.info(
            '{} pet the cat'.format(
                self.name
            )
        )

    def depress(self):
        if Storage.dirt > 90:
            self.happiness -= 10
        else:
            pass


class Storage:
    food = 100
    cat_food = 60
    dirt = 0
    money = 200
    fur_coats = 0


class Husband(FamilyGuy):
    def play(self):
        self.happiness += 20
        self.satiety -= 10
        log_hus.info(
            '{} played videogame'.format(
                self.name
            )
        )

    def work(self):
        Storage.money += 150
        self.satiety -= 10
        log_hus.info(
            '{} worked'.format(
                self.name
            )
        )


class Wife(FamilyGuy):
    def shopping(self):
        if Storage.food < 100:
            food_bought = 100
            Storage.food += food_bought
            Storage.money -= food_bought
            self.satiety -= 10
            log_wife.info(
                '{} bought food for family ({})'.format(
                    self.name, food_bought
                )
            )
        elif Storage.cat_food < 10:
            cat_food_bought = 30
            Storage.cat_food += cat_food_bought
            Storage.money -= cat_food_bought
            self.satiety -= 10
            log_wife.info(
                '{} bought food for cat ({})'.format(
                    self.name, cat_food_bought
                )
            )
        else:
            food_bought = random.randint(50, 100)
            cat_food_bought = random.randint(10, 40)
            Storage.food += food_bought
            Storage.money -= food_bought
            Storage.cat_food += cat_food_bought
            Storage.money -= cat_food_bought
            self.satiety -= 10
            log_wife.info(
                '{} bought food for cat ({}) and family ({})'.format(
                    self.name, cat_food_bought, food_bought
                )
            )

    def buy_fur_coat(self):
        if Storage.money > 500:
            self.satiety -= 10
            self.happiness += 60
            Storage.money -= 350
            Storage.fur_coats += 1
            log_wife.info(
                '{} bought a fur coat'.format(
                    self.name
                )
            )
        else:
            self.happiness += 10
            log_wife.info(
                '{} dreamt of a fur coat all day'.format(
                    self.name
                )
            )

    def cleaning(self):
        try:
            dirt_to_remove = random.randint(10, 100)
            if Storage.dirt - dirt_to_remove > 0:
                Storage.dirt -= dirt_to_remove
                self.satiety -= 10
                log_wife.info(
                    '{} removed {} points of dirt'.format(
                        self.name, dirt_to_remove
                    )
                )
            else:
                raise ValueError('No dirt to remove!')
        except ValueError as ve:
            log_wife.error(ve)


class Cat(FamilyGuy):

    def eat(self):
        if self.satiety < 10:
            self.satiety += 20
            Storage.cat_food -= 10
            log_cat.info(
                '{} eaten 10 points of food'.format(
                    self.name
                )
            )
        else:
            food_eaten = random.randint(1, 10)
            self.satiety += food_eaten
            Storage.cat_food -= food_eaten
            log_cat.info(
                '{} eaten {} points of food'.format(
                    self.name, food_eaten
                )
            )

    def sleep(self):
        self.satiety -= 10
        log_cat.info(
            '{} slept'.format(
                self.name
            )
        )

    def scratch_wallpaper(self):
        self.satiety -= 10
        log_cat.info(
            '{} scrath the wallpaper'.format(
                self.name
            )
        )


def result():
    print(
        'Food left: {}\nCat food left: {}\nMoney left: {}\nFur coats bought: {}'.format(
            Storage.food, Storage.cat_food, Storage.money, Storage.fur_coats
        )
    )


def is_alive(person):
    if person.happiness < 10 or person.satiety <= 0:
        common_log.info(
            '{} died. End of the experiment'.format(
                person.name
            )
        )
        return True
    return False


man = Husband('Jack')
woman = Wife('Marry')
cat = Cat('Garfield')

days = 0
while days < 366:
    dice = random.randint(1, 6)
    common_log.info('день ' + str(days))
    if is_alive(man):
        break
    elif is_alive(woman):
        break
    elif is_alive(cat):
        break
    else:
        days += 1
        Storage.dirt += 5
        if man.satiety < 10:
            man.eat()
        if woman.satiety < 10:
            woman.eat()
        if cat.satiety < 10:
            cat.eat()
        if man.happiness < 20:
            if dice in range(1, 4):
                man.pet_the_cat()
            else:
                man.play()
        if woman.happiness < 20:
            if dice in range(1, 4):
                woman.pet_the_cat()
            else:
                woman.buy_fur_coat()
        elif Storage.food < 50 or Storage.cat_food < 30:
            woman.shopping()
        elif Storage.dirt > 70:
            woman.cleaning()
        elif Storage.money < 100:
            man.work()
        elif dice == 4:
            man.work()
            woman.shopping()
            cat.eat()
        elif dice == 5:
            man.play()
            woman.buy_fur_coat()
            cat.scratch_wallpaper()
        elif dice == 6:
            man.eat()
            woman.eat()
            cat.sleep()

        man.depress()
        woman.depress()

result()
