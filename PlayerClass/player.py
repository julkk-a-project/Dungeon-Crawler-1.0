class Player:
    level = 1
    maxxp = (level * 3) ** 2
    maxhp = 1
    hp = maxhp
    st = 1
    mp = 0
    ag = 1
    xp = 0

    def heal(self):
        self.hp = self.maxhp

    def setXp(self):
        self.maxxp = (self.level * 3) ** 2

class Mage(Player):
    klass = "Mage"
    maxhp = 10
    st = 1
    mp = 5
    ag = 1
    xp = maxhp + st + mp + ag
    pass

class Rouge(Player):
    klass = "Rouge"
    maxhp = 10
    st = 3
    mp = 3
    ag = 1
    xp = maxhp + st + mp + ag
    pass

class Warrior(Player):
    klass = "Warrior"
    maxhp = 15
    st = 5
    xp = maxhp + st + mp + ag
    pass