class Player:
    name = "Defaultskin"
    level = 1
    maxxp = (level * 3) ** 2
    maxhp = 1
    hp = maxhp
    st = 1
    mp = 0
    ag = 1
    xp = 0
    score = 0

    def heal(self):
        self.hp = self.maxhp

    def setXp(self):
        self.maxxp = (self.level * 3) ** 2


class Mage(Player):
    klass = "Mage"
    maxhp = 10
    hp = maxhp
    st = 1
    mp = 5
    pass


class Rouge(Player): #a really worthless "class" atm
    klass = "Rouge"
    maxhp = 10
    hp = maxhp
    st = 3
    mp = 3
    pass


class Warrior(Player):
    klass = "Warrior"
    maxhp = 15
    hp = maxhp
    st = 5
    pass
