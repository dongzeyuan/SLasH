class MonPl(object):
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap
        print('{0} has joinned the battle'.format(self.name))

    def getstatus(self):
        return self.hp


def fight(player, monster):
    while monster.getstatus() > 0:
        monster.hp = monster.hp - player.ap
        print('The monster has {0} hp left'.format(monster.getstatus()))
    else:
        print('The monster has been defeated')


if __name__ == "__main__":
    player = MonPl('V', 100, 3)
    monster = MonPl('GW', 100, 1)
    fight(player, monster)
