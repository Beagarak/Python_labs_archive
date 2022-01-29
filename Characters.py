import Weapon
from Weapon import weapon_list


class Character:
    #создает игрока и дает ему базовые функции
    def __init__(self):
        self.health = 100
        self.armor = 0
        self.money = 6000
        self.height = 1
        self.speed = 2
        self.noise = 1
        self.ammunition = 0

    def moving(self):
        # иммитирует перемещение игрока по карте
        if self.height == 0.5:
            print('Присел и крадусь к противнику')
        elif self.noise == 0:
            print('Kрадусь')
        else:
            print('Бегу')

    def sit(self):
        # меняет положение игрока на положение сидя
        self.height = 0.5
        self.speed = 1
        self.noise = 0
        print('так меня не видно из-за укрытия')

    def stand(self):
        # меняет положение игрока на положение стандартное
        self.height = 1
        self.speed = 2
        self.noise = 1
        print('ничто меня не остановит ')

    def sneak(self):
        # делает перемещение бесшумным
        self.speed = 1
        self.noise = 0
        print('надеюсь, меня не заметят')


    def buy_weapon(self):
        # выбирает оружие из списка доступных и вооружается им
        print('Выберите оружие')
        for item in weapon_list:
            print(f'{item.name} стоит {item.cost}')
        choice = input('введите название оружия\n')
        for item in weapon_list:
            if choice == item.name:
                self.money -= item.cost
                self.ammunition = item
                print('Осталось', self.money)


    def shooting(self, aim):
        # иммитация стрельбы
        # aim - указывает на игрока, по которому будет произведен выстрел
        if self.ammunition == 0:
            print('надо купить оружие')
        else:
            self.ammunition.shot()
            aim.health -= self.ammunition.damage

    def reloading(self):
        self.ammunition.reload()


class SWAT(Character):
    # один из типов игроков, может обезвреживать бомбы
    def __init__(self):
        super().__init__()
        self.defuse_ability = 0
        print('Я - солдат, я не спал пять лет...\n')

    def defuse(self):
        #иммитация обезвреживания бомы
        if self.defuse_ability == 0:
            print('обезвреживаю бомбу, справлюсь за 10 сек')
        else:
            print('обезвреживаю бомбу, справлюсь за 5 сек')


class Terrorist(Character):
    # один из типов игроков, может обезвреживать бомбы
    def __init__(self):
        super().__init__()
        print('Бомбим,чувачки\n')

    def plant_bomb(self):
        print('Бомба установлена')


