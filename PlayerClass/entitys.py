from time import sleep


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
    agXp = 0 #just to prevent errors
    def taunt(self):
        print ('"Taunt"')
        sleep(2)
    def fixhealth(self):
        self.hp = self.maxhp

class goblin(baseEntity):
    klass = "Goblin"
    maxhp = 5
    hp = maxhp
    xp = 7

class evil_wizard(baseEntity):
    klass = "Evil Wizard"
    level = 3
    maxhp = 10
    hp = maxhp
    st = 2
    mp = 4
    xp = 17
    grand = False
    def fixhealth(self):
        if self.grand != True:
            self.hp = self.maxhp
        else:
            print ("The Grand Wizard uses a minor healing spell")
            self.hp += 1

    def is_grand(self):
        self.grand = True
        self.klass = "GRAND Wizard"
        self.level = 45
        self.maxhp = 50
        self.hp = 50
        self.mp = 5
        self.xp = self.maxhp + self.st + self.mp + self.ag

class bridgeTroll(baseEntity):
    klass = "Bridge Troll"
    level = 15
    maxhp = 25
    hp = maxhp
    st = 4
    mp = 0
    ag = 1
    xp = maxhp + st + mp + ag
    def taunt(self):
        print ('"WHO DARES CROSS MY BRIDGE!"')
        #add a meme where you must ether say your name, or just weap in fear, maybe giving initiative to the troll. lol.
        sleep(2)

class large_door(baseEntity):
    klass = "Large Door"
    level = 3
    maxhp = 10
    hp = maxhp
    st = 1
    mp = 0
    ag = 0
    xp = maxhp + st + mp + ag

class arskaTown_guard(baseEntity):
    klass = "ArskaTown Guard"
    level = 5
    maxhp = 15
    hp = maxhp
    st = 5
    mp = 0
    ag = 1
    xp = 26

class boulder(baseEntity):
    klass = "A effing boulder!!!"
    level = 100
    maxhp = 9001
    hp = maxhp
    st = 9001
    mp = 0
    ag = 9001
    xp = 9001
    xp = maxhp + st + mp + ag

class sunPriest(baseEntity):
    klass = "Sun priest"
    level = 3
    maxhp = 10
    hp = maxhp
    st = 2
    mp = 5
    ag = 1
    xp = maxhp + st + mp + ag

class eulersMonster(baseEntity):
    klass = "Euler's Monster"
    def taunt(self):
        print ('"WHO DARES CROSS MY BRIDGES ILLOGICALLY????!?!?"')
        #add a meme where you must ether say your name, or just weap in fear, maybe giving initiative to euler. lol.
        sleep(2)
    level = 69
    maxhp = 69
    mp = 0
    hp = maxhp
    st = 5
    ag = 1
    xp = maxhp + st + mp + ag 

class pimpGuard(baseEntity):
    klass = "Pimp's Guard"
    level = 5
    maxhp = 10
    hp = maxhp
    st = 3
    mp = 0
    ag = 1
    xp = 19