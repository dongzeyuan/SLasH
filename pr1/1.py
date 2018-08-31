class Monster(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.ap = 1

    def getstatus(self):
        if self.hp == 0:
            print('{0} is defeated'.format(self.name))
        else:
            print('{0} is alive'.format(self.name))


class Player(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.ap = 2

    def getstatus(self):
        if self.hp == 0:
            print('{0} is defeated'.format(self.name))
        else:
            print('{0} is alive'.format(self.name))


def fight(player, monster):
    while true:
        monster.hp = monster.hp - player.ap
        monster.getstatus()


if __name__ == "__main__":
