class baseEntity:
    klass = "???"
    level = 1
    maxxp = (level * 3) ** 2
    maxhp = 1
    hp = maxhp
    st = 1
    mp = 0
    ag = 1
    xp = maxhp + st + mp + ag
    def taunt(self):
        print '"Taunt"'
        sleep(2)
    def fixhealth(self):
        self.hp = self.maxhp

class goblin(baseEntity):
    klass = "Goblin"
    maxhp = 5

class evil_wizard(baseEntity):
    level = 3
    maxhp = 10
    st = 2
    mp = 4
    grand = false
    def fixhealth(self):
            if self.grand != True:
                self.hp = self.maxhp
            else:
                print "The Grand Wizard uses a minor healing spell"
                self.hp += 1
        def is_grand(self):
            self.grand = True
            self.klass = "GRAND Wizard"
            self.level = 45
            self.maxhp = 50
            self.hp = 50
            self.mp = 5

class bridgeTroll(baseEntity):
    klass = "Bridge Troll"
    level = 15
    maxhp = 25
    st = 4
    mp = 0
    ag = 1

class large_door(baseEntity):
    klass = "Large Door"
    level = 3
    maxhp = 10
    st = 1
    mp = 0
    ag = 0

class arskaTown_guard(baseEntity):
    klass = "ArskaTown Guard"
    level = 5
    maxhp = 15
    st = 5
    mp = 0
    ag = 1

class boulder(baseEntity):
    klass = "A effing boulder!!!"
    level = 100
    maxhp = 9001
    st = 9001
    mp = 0
    ag = 9001
    xp = 9001

class sunPriest(baseEntity):
    klass = "Sun priest"
    level = 3
    maxhp = 10
    st = 2
    mp = 5
    ag = 1