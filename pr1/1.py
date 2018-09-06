# 还是需要再看几遍狗书

import time
import random


class MonPl(object):
    def __init__(self, name, hp, ap, attsp):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.attsp = attsp
        print('{0} has joinned the battle'.format(self.name))

    def getstatus(self):
        return self.hp


class Item(object):
    def __init__(self, itype, rate):
        self.itype = itype
        self.rate = rate

    def droprate(self):
        self.rate = random.choice(0, 1)
        if self.rate > 0.5:
            return self.itype


def fight(player, monster):
    who_round = 'player'
    while monster.getstatus() > 0 and player.getstatus() > 0:
        if who_round == 'player':
            monster.hp = monster.hp - player.ap
            print('The monster has {0} hp left'.format(monster.getstatus()))
            who_round = 'monster'
        else:
            player.hp = player.hp - monster.ap
            print('The player has {0} hp left'.format(player.getstatus()))
            who_round = 'player'
    else:
        print('The monster has been defeated')

def drop(m)


if __name__ == "__main__":
    player = MonPl('V', 100, 3, 2)
    monster = MonPl('GW', 100, 1, 5)
    fight(player, monster)
