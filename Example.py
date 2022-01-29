import time
import Weapon
from Characters import Terrorist, SWAT
from Weapon import weapon_list

player_swat = SWAT()
player_swat.buy_weapon()  # нужно передать значения на выбор: AK-47, AWP , NEGEV

player_ter = Terrorist()
player_ter.buy_weapon()   # нужно передать значения на выбор: AK-47, AWP , NEGEV

player_swat.moving()
time.sleep(2)
player_swat.sit()
time.sleep(2)
player_swat.moving()
time.sleep(2)
player_swat.shooting(player_ter)
player_swat.shooting(player_ter)
time.sleep(2)
player_swat.stand()
player_swat.reloading()
time.sleep(2)
print('Здоровье у player_ter', player_ter.health)
player_ter.sneak()
time.sleep(2)
player_ter.plant_bomb()
time.sleep(2)
player_swat.moving()
player_ter.shooting(player_swat)
time.sleep(2)
player_swat.defuse()