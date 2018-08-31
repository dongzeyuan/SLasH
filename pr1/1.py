class MonPl(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.ap = 1
        print('{0} has joinned the battle'.format(self.name))

    def getstatus(self):
        return self.hp


def fight(player, monster):
        monster.hp = monster.hp - player.ap
        print('The monster has {0} hp left'.format(monster.getstatus()))


if __name__ == "__main__":
    player = MonPl('V',100)
    monster = MonPl('GW', 100)
    fight(player, monster)
