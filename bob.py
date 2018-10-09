import time #IFYOUSEETHISEDITTHISWORKS. t. julkkis666
import random
starttimes = 5

while starttimes >= 0:
    
    print "***********"
    print "..........."
    print "*** D C ***"
    print "... 1.0 ..."
    print "***********"
    print "..........."
    time.sleep(0.01)
    print "\n"*60
    
    print "..........."
    print "***********"
    print "... D C ..."
    print "*** 1.0 ***"
    print "..........."
    print "***********"
    time.sleep(0.01)
    print "\n"*60
    starttimes -= 1


time.sleep(0)

class warrior:
    klass = "Warrior"
    level = 1
    maxxp = (level * 3) ** 2
    maxhp = 15
    hp = maxhp
    st = 5
    mp = 0
    ag = 1
    xp = maxhp + st + mp + ag
    def heal(self):
        self.hp = self.maxhp
    def setXp(self):
        self.maxxp = (level * 3) ** 2
    
class mage:
    klass = "Mage"
    level = 1
    maxxp = (level * 3) ** 2
    maxhp = 10
    hp = maxhp
    st = 1
    mp = 5
    ag = 1
    xp = maxhp + st + mp + ag
    def heal(self):
        self.hp = self.maxhp
    def setXp(self):
        self.maxxp = (level * 3) ** 2
    
class rouge:
    klass = "Rouge"
    level = 1
    maxxp = (level * 3) ** 2
    maxhp = 10
    hp = maxhp
    st = 3
    mp = 3
    ag = 1
    xp = maxhp + st + mp + ag
    def heal(self):
        self.hp = self.maxhp
    def setXp(self):
        self.maxxp = (level * 3) ** 2

class goblin:
    klass = "Goblin"
    
    level = 1
    maxxp = (level * 3) ** 2
    maxhp = 5
    hp = maxhp
    st = 1
    mp = 0
    ag = 1
    xp = maxhp + st + mp + ag
    def fixhealth(self):
        self.hp = self.maxhp


class evil_wizard:
    klass = "Evil Wizard"
    
    level = 3
    maxxp = (level * 3) ** 2
    maxhp = 10
    hp = maxhp
    st = 2
    mp = 4
    ag = 1
    xp = maxhp + st + mp + ag
    def fixhealth(self):
        self.hp = self.maxhp
    def is_grand(self):
        self.klass = "GRAND Wizard"
        self.level = 45
        self.maxhp = 50
        self.hp = 50
        self.mp = 5


class large_door:
    klass = "Large Door"
    
    level = 3
    maxxp = (level * 3) ** 2
    maxhp = 10
    hp = maxhp
    st = 1
    mp = 0
    ag = 0
    xp = maxhp + st + mp + ag
    def fixhealth(self):
        self.hp = self.maxhp
    
    
class rougel: #TODO: maybe randomize rouge every time you select it?
    klass = "RougeLike"
    level = 1
    maxxp = (level * 3) ** 2
    maxhp = random.randint(8,20)
    hp = maxhp
    st = random.randint(1,5)
    mp = random.randint(0,5)
    ag = random.randint(1,3)
    xp = maxhp + st + mp + ag
    def heal(self):
        self.hp = self.maxhp
    def setXp(self):
        self.maxxp = (level * 3) ** 2



player = "???"
print
name = raw_input("What is your name!\n")
try1 = 1
try2 = 2
while try2 != 1:
    print "\n"*60
    print "___________"
    print
    print "XXX D C XXX"
    print "XXX 1.0 XXX"
    print "___________"
    while try1 == 1:
        klass = raw_input('CHOOSE YOUR CLASS!!\n(1)WARRIOR\n(2)MAGE\n(3)ROUGE\n(?)ROUGE LIKE\n')
        if klass == "1" or klass == "WARRIOR" or klass == "warrior":
            player = warrior()
            try1 = 0
        elif klass == "2" or klass == "MAGE" or klass == "mage":
            player = mage()
            try1 = 0
        elif klass == "3" or klass == "ROUGE" or klass == "rouge":
            player = rouge()
            try1 = 0
        elif klass == "?" or klass == "ROUGE like" or klass == "rouge like":
            player = rougel()
            try1 = 0
        else:
            print "\n"*60
            print "BUG"
            time.sleep(1)
            print "\n"*60
            try1 = 1
    
    print "\n"*60
    print "____________________________"
    print
    print "Your name is ", name
    print "Your class is", player.klass
    print "____________________________"
    print
    print "THESE ARE YOUR EPIC STATS!!!"
    print "____________________________"
    print
    print "Health    Points:",player.hp
    print "Streingth Points:",player.st
    print "Magic     Points:",player.mp
    print "Agility   Points:",player.ag
    print "____________________________"
    print
    try2 = input("enter (1) if you are happy!\nAND (2) IF YOU WANT TO CHOOSE AGAAAIN!!!\n")
    try1 = 1
###########
#Encounter#
###########
def encounter(player,entity):
    
    print "\n"*60
    print "YOU ENCOUNTERED A" entity.klass, "!"
    print
    print entity.taunt
    battle(player,entity)



################
#Choise handler#
################

def tryer(num,string):
    while true:
        print string
        try:
            trynum = input("You chose: ")
        except:
            print "Try a number, fool"
        if trynum >= 1 and trynum <= num:
            if type(trynum) == type(1):
                return trynum
        else:
            print "try an advertised number"





#############
#pokemon 1v1#
#############
def battle(player,entity):
    print "\n"*60
    print "_______________"
    print
    print "BATTLE STARTED!"
    print "_______________"
    print
    print "you are figthing a level", entity.level, entity.klass
    print "_______________"
    print
    while player.hp > 0 and entity.hp > 0:
        print "--------------------------"
        print name, "health:", player.hp, "/", player.maxhp
        print "--------------------------\n"
        attack = input("which attack do you wish to chose?\n(1)Slash\n(2)Fireball\n") #TODO: add chek if string
        print "\n" * 60
        if attack == 1: #TODO: add hint at how much hp the enemy has (as in for example 75% of maxhp would be one level and 50% would be an other and so on.
            print "You use SLASH!!!"
            time.sleep(1)
            #TODO: add agility chek
            print "It was super effective!"
            entity.hp -= player.st
            time.sleep(1)
            print entity.klass, "has", entity.hp, "/", entity.maxhp, "health" + "\n"
        else:
            print "You use FIREBALL!!!"
            time.sleep(1)
            #TODO: add agility chek
            print "It was super effective!"
            time.sleep(1)
            entity.hp -= player.mp
            print entity.klass, "has", entity.hp, "/", entity.maxhp, "health" + "\n"
            
        if entity.st > entity.mp:
            if entity.mp <= 0:
                attackE = 1
            else:
                humanizer = random.randint(1,3)
                if humanizer == 3:
                    attackE = 2
                else:
                    attackE = 1
        else:
            if entity.st <= 0:
                attackE = 2
            else:
                humanizer = random.randint(1,3)
                if humanizer == 3:
                    attackE = 1
                else:
                    attackE = 2
        if entity.hp > 0:
            if attackE == 1:
                time.sleep(1)
                print entity.klass, "used SLASH!"
                time.sleep(1)
                print "it was SUPER EFFECTIVE!" #Add agility chek/roll
                player.hp -= entity.st
                time.sleep(1)
                print name, "has", player.hp, "/", player.maxhp, "HP LEFT!!!" #add armor calculation?
            else:
                time.sleep(1)
                print entity.klass, "used FIREBALL!"
                time.sleep(1)
                print "it was SUPER EFFECTIVE!" #Add agility chek/roll
                player.hp -= entity.mp
                time.sleep(1)
                print name, "has", player.hp, "/", player.maxhp, "HP LEFT!!!" #add armor calculation?
            
    if player.hp > 0:
        player.xp += entity.xp
        print "\n"
        print "Leveling progress:"
        print "------------------"
        print player.xp, "/", player.maxxp
        print "------------------"
        time.sleep(2)
        print "\n"*60
    else:
        print "\n"*60
        print "You died."
        time.sleep(6)
        quit()
    if player.xp >= player.maxxp:
        print
        print
        print "YOU LEVELED UP!"
        print "____________________________"
        print
        print "Level", player.level, player.klass
        print "____________________________"
        print
        print "THESE ARE YOUR EPIC STATS!!!"
        print "____________________________"
        print
        print "Health    Points:",player.hp, "/", player.maxhp
        print "Streingth Points:",player.st
        print "Magic     Points:",player.mp
        print "Agility   Points:",player.ag
        print "____________________________"
        print
        player.level += 1
        trystat = 1
        while trystat == 1:
            statplus = tryer(5,"WHICH SKILL DO YOU WANT TO INCREASE!\n(1)Health\n(2)Streingth\n(3)Magic\n(4)Agility\n(5)Dude, i just want to heal")
            healpoints = player.maxhp
            if statplus == 1:
                player.maxhp += 1
                player.hp += 1
                trystat = 0
            elif statplus == 2:
                player.st += 1
                trystat = 0
            elif statplus == 3:
                player.mp += 1
                trystat = 0
            elif statplus == 4:
                player.ag += 1
                trystat = 0
            elif statplus == 5:
                player.hp = healpoints
                trystat = 0
            else:
                print "my nibba, try an advertised number!"
        player.xp = 0
    print "\nbattle ended\n"
            
#######
#Chase#
#######

  #add chase event here  


###########
#Noob Cave# cordinates (0,0)
###########

def cave(player,goblin):
    print "\n"*60
    print "you walk arround in the cave."
    whatdo2 = 1
    while whatdo2 == 1:
        chanse = random.randint(0,5)
        if chanse == 1:
            print "YOU ENCOUNTERED A GOBLIN!"
            goblin.fixhealth()
            whatdo = input("what do?\n(1)Attack it\n(2)Run away like a poossy")
            if whatdo != 1:
                chase = random.randint(0,1)
                if chase == 1:
                    print "HA-HA IT FOLLOWED YOU!!!"
                    whatdo = 1
            if whatdo == 1:
                battle(player,goblin)
                try:
                    whatdo2 = input("Do you want to turn over more rocks\n(1)Yes\n(2)No\n")
                except:
                    print "try writing a number, noob."


############
#Dark Tower# cordinates (0,1)
############

def noob_tower(player,goblin,evil_wizard):
    print "\n"*60
    #Add art of the tower
    door = large_door()
    print "The Door is locked."
    yesno1 = input("(1)Kick it in\n(2)Run away loik a poossy")
    if yesno1 == 1:
        battle(player,door)
        time.sleep(2)
        print "\n"*60
        print "The door swears it'll get Zer revenge,\nas it opens with an angry look about it."
        time.sleep(6)
        print "\n"*60
        up = 1
        upp = 1
        while upp >= 1:
            print "\n"*60
            print "'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'"
            print "The further you climb,\n the more of the dark magic you feel in your fingers."
            print "'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'¨´'~'"
            print "\nYou climb the stairs of the tower.\n"
            print "You're on level", upp
            print
            up = input("Do you dare to keep climbing?\n(1)Yes! I HAVE THE POWEEEER!!!\n(2)nn-n-no i-i think i-i-i'll just go home now :(\n")
            if up == 1:
                upp += 1
            else:
                upp -= 1
            encounter = random.randint(1,5)
            if upp <= 4:
                if encounter <= 2:
                    print "\n"*60
                    print "Oh crap! a goblin!"
                    goblin.fixhealth()
                    time.sleep(1)
                    battle(player,goblin)
                else:
                    print "\n"*60
                    print "think i heard something..."
                    time.sleep(2)
            elif upp > 4 and upp < 10:
                if encounter <= 2:
                    print "\n"*60
                    print "Oh crap! a goblin!"
                    goblin.fixhealth()
                    time.sleep(1)
                    battle(player,goblin)
                elif encounter >= 4:
                    print "\n"*60
                    print "Wh-What?"
                    evil_wizard.fixhealth()
                    time.sleep(1)
                    battle(player,evil_wizard)
                else:
                    print "\n"*60
                    print "It seems like the walls are talking to me :S"
                    time.sleep(3)
            elif upp >= 10:
                print "\n"*60
                print "----------------------------"
                print "You made it to the top floor"
                print "----------------------------"
                evil_wizard.fixhealth
                evil_wizard.is_grand()
                print "\nin front of you stands a grand wizard."
                time.sleep(3)
                print '\nWizard: "THIS IS MY LAIR! THAU SHALT NOT PASS!"\n\n'
                time.sleep(3)
                battle(player,evil_wizard)
                
                    
            
    else:
        print "The door Laughs at you"
        time.sleep(2)
        return player
    print "You climb the stairs of the tower."
    print
    print "The further you climb, the more of the dark magic you'll start to feel in your fingers."



###########
#World Map#
###########






location = [0,0]

while player.hp > 0:
    print "\n"*60
    print "-----------"
    print "|OVERWORLD|"
    print "-----------"

    if location == [0,0]: #NoobCave
        print "You see a cave!"
        yesno1 = input("Do you want to enter?\n(1)Yes\n(2)No")
        if yesno1 == 1:
            goblin = goblin()
            cave(player,goblin)
        else:
            print "\n"*60
            print "-----------------------------------"
            print "North of you there is a Dark tower.\nIn all other directions there are mountains."
            print "-----------------------------------"
            testmove1 = 2
            testmove1 = input("Move North?\n(1)Yes\n(2)No.\n")
            if testmove1 == 1:
                location[1] += 1

    if location == [0,1]:
        print "You see a DARK TOWER!!!"
        yesno2 = input("Do you want to enter?\n(1)Yes\n(2)No")
        if yesno2 == 1:
#            goblin = goblin()
            evil_wizard = evil_wizard()
            noob_tower(player,goblin,evil_wizard)







print "add stuff here"
        

#class player:
#    hp=10
#    def setHP(self,x):
#        self.hp = x
#class animal:
#    hp=3
#    

#bob = player()
#bob.setHP(123)
#print bob.hp
#karl = player()
#karl.setHP(69)
#print karl.hp

