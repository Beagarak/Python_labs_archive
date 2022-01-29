
class Gun:

    left_bullet = 0
    def __init__(self,name):
        self.name = name

    def shot(self):
        if self.bullets_at_chamber < 0:
            print('ничего не происходит')
        else:
            self.bullets_at_chamber -= self.bullet_per_shot
            self.all_bullets -= self.bullet_per_shot

            print('Бах')
            print(f'Осталось {self.bullets_at_chamber} патронов')
            return self.damage


    def reload(self):
        self.all_bullets -= Gun.left_bullet
        print('*Звук перезарядки*')
        print(f'Еще есть {self.all_bullets} патронов')

class Rifle(Gun):
    def __init__(self, name):
        self.name = name
        self.damage = 30
        self.bullets_at_chamber = 30
        self.bullet_per_shot = 5
        self.all_bullets = 120
        self.cost = 2700


class Machinegun(Rifle):
    def __init__(self, name):
        self.name = name
        self.damage = 20
        self.bullets_at_chamber = 100
        self.bullet_per_shot = 10
        self.all_bullets = 300
        self.cost = 5200


class SniperRifel(Rifle):
    def __init__(self, name):
        self.name = name
        self.damage = 90
        self.bullets_at_chamber = 10
        self.bullet_per_shot = 1
        self.all_bullets = 30
        self.cost = 4700
    def scope(self):
        print('Прицелился')


weapon_list = []
AK_47 = Rifle('AK-47')
AWP = SniperRifel('AWP')
NEGEV = Machinegun('NEGEV')
weapon_list.append(AK_47)
weapon_list.append(AWP)
weapon_list.append(NEGEV)


