# -*- coding: utf-8 -*-

import time
import random


startTimes = 3
for times in range(0, startTimes):
    # List with all the normal combinations
    defaultLine = ("***********", "***********", "*** D C ***", "*** 1.0 ***", "***********", "***********")
    # List with all the dotted combinations
    dottedLine = ("...........", "...........", "... D C ...","... 1.0 ...", "...........", "...........")
    reversed = [5, 4, 3, 2, 1, 0]
    for j in range(0, 6):
        for i in range(0, len(dottedLine)):
            # the first time j is 0 so reversed[j] is 5
            # when i is 5 it is the last print so it takes the dotted line from index 5
            
            # the secound time j is 1 so reversed[j] is 4
            # when i is 4 it is the secound last print so it takes the dotted line from index 4
            
            # and so on
            if i == reversed[j]:
                print dottedLine[i]
            else:
                print defaultLine[i]
        time.sleep(0.25)
        print "\n"*60

#TODO: make player classes subclasses of a master "player class".
class baseplayer:
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
        self.maxxp = (self.level * 3) ** 2
    
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
        self.maxxp = (self.level * 3) ** 2
    
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
        self.maxxp = (self.level * 3) ** 2

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

class bridgeTroll:
    klass = "Bridge Troll"
    
    level = 15
    maxxp = (level * 3) ** 2
    maxhp = 25
    hp = maxhp
    st = 4
    mp = 0
    ag = 1
    xp = maxhp + st + mp + ag
    def fixhealth(self):
        self.hp = self.maxhp


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
    
    
class rougel:
    def __init__(self):
        self.klass = "RougeLike"
        self.level = 1
        self.maxxp = (self.level * 3) ** 2
        self.maxhp = random.randint(8,20)
        self.hp = self.maxhp
        self.st = random.randint(1,5)
        self.mp = random.randint(0,5)
        self.ag = random.randint(1,3)
        self.xp = self.maxhp + self.st + self.mp + self.ag
    def heal(self):
        self.hp = self.maxhp
    def setXp(self):
        self.maxxp = (self.level * 3) ** 2



class arskaTown_guard:
    klass = "ArskaTown Guard"
    
    level = 5
    maxxp = (level * 3) ** 2
    maxhp = 15
    hp = maxhp
    st = 5
    mp = 0
    ag = 1
    xp = maxhp + st + mp + ag
    def fixhealth(self):
        self.hp = self.maxhp





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
    print "YOU ENCOUNTERED A", entity.klass, "!"
    print
#    print entity.taunt #TODO: FIX ME
    time.sleep(2)
    battle(player,entity)



################
#Choise handler#
################

def tryer(num,string):
    while True:
        print string
        try:
            trynum = input("You chose: ")
            if trynum >= 1 and trynum <= num:
                if type(trynum) == type(1):
                    print "\n"*60
                    return trynum
            else:
                print "try an advertised number"
        except:
            print "Try a number, fool"
        

#############
#Dice roller#
#############

def dice(num): #num -> how big a die you throw
    number = random.randint(1,num)
    return number


###############
#Battle system#
###############
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
        attack = tryer(3,"which attack do you wish to chose?\n(1)Slash\n(2)Fireball\n(3)Nether, i want back to mommy ;(\n")
        print "\n" * 60
        if attack == 1: #TODO?: add hint at how much hp the enemy has (as in for example 75% of maxhp would be one level and 50% would be an other and so on.
            print "You use SLASH!!!"
            time.sleep(1)
            #TODO: add agility chek
            print "It was super effective!"
            entity.hp -= player.st
            time.sleep(1)
            print "The", entity.klass, "has", entity.hp, "/", entity.maxhp, "health" + "\n"
        elif attack == 2:
            print "You use FIREBALL!!!"
            time.sleep(1)
            #TODO: add agility chek
            print "It was super effective!"
            time.sleep(1)
            entity.hp -= player.mp
            print entity.klass, "has", entity.hp, "/", entity.maxhp, "health" + "\n"
        else:
            escape = coward(player,entity)
            time.sleep(2)
            print "\n"*60
            if escape == 0:
                pass
            if escape == 1:
                return player,entity #IMPORTANT TODO: This makes it possible to skip any battle with enough agility
            
        if entity.st > entity.mp: #Simple "AI" to make the AI use weiged random attacks
            if entity.mp <= 0:
                attackE = 1
            else:
                humanizer = dice(3)
                if humanizer == 3:
                    attackE = 2
                else:
                    attackE = 1
        else:
            if entity.st <= 0:
                attackE = 2
            else:
                humanizer = dice(3)
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
            statplus = tryer(4,"WHICH SKILL DO YOU WANT TO INCREASE!\n(1)Health\n(2)Streingth\n(3)Magic")
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
            else:
                print "my nibba, try an advertised number!"
        player.xp -= player.maxxp
        player.setXp()
    print "\nbattle ended\n"
            
########################
#Run awaay loik a poosy# TODO: make more complex
########################

def coward(player,entity): #returns 1 if escape successfull, returns 0 if escape failed
    test = player.ag - entity.ag
    if test > 0:
        "EZ escape"
        return 1
    if test == 0:
        test2 = dice(2)
        if test2 == 1:
            print "You barely escaped"
            return 1
        else:
            print "You tripped"
            return 0
    if test < 0:
        print "You're worthless at running"
        return 0


###########
#Noob Cave# cordinates (0,0)
###########

def cave(player,goblin):
    print "\n"*60
    print "you walk around in the cave."
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
    yesno1 = tryer(2,"(1)Kick it in\n(2)Run away loik a poossy")
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
            print "~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'"
            print "The further you climb,\n the more of the dark magic you feel in your fingers."
            print "~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'"
            print "\nYou climb the stairs of the tower.\n"
            print "You're on level", upp
            print
            up = tryer(2,"Do you dare to keep climbing?\n(1)Yes! I HAVE THE POWEEEER!!!\n(2)nn-n-no i-i think i-i-i'll just go home now :(\n")
            if up == 1:
                upp += 1
            else:
                upp -= 1
            encounterChanse = random.randint(1,5)
            if upp <= 4:
                if encounterChanse <= 2:
                    goblin.fixhealth()
                    encounter(player,goblin)
                else:
                    print "\n"*60
                    print "think i heard something..."
                    time.sleep(2)
            elif upp > 4 and upp < 10:
                if encounterChanse <= 2:
                    goblin.fixhealth()
                    encounter(player,goblin)
                elif encounterChanse >= 4:
                    evil_wizard.fixhealth()
                    encounter(player,evil_wizard)
                else:
                    print "\n"*60
                    print "It seems like the walls are talking to me :S"
                    time.sleep(3)
            elif upp >= 10:
                print "\n"*60
                print "----------------------------"
                print "You made it to the top floor"
                print "----------------------------"
                evil_wizard.is_grand()
                print "\nin front of you stands a grand wizard."
                time.sleep(2)
                print '\nWizard: "THIS IS MY LAIR! THAU SHALT NOT PASS!"\n\n'
                time.sleep(2)
                battle(player,evil_wizard)
                #TODO: chek if wizard dead, end-taunt, loot, escape
                
                    
            
    else:
        print "The door Laughs at you"
        time.sleep(2)
        return player
    print "You climb the stairs of the tower."
    print
    print "The further you climb, the more of the dark magic you'll start to feel in your fingers."

#########
#Village# cordinates (1,1)
#########

def arskaTown(player,arskaTown_guard):
    global arskaTownAgro
    print "Outside the village you see a sign, it says: Welcome to Arskatown"
    time.sleep(2)
    print "You also see a guard standing in front of you"
    if arskaTownAgro == 0:
        print "Guard: Hello there! You may enter Arskatown."
        time.sleep(2)
        print "You look at the guard and think: Damn I could get xp from that."
        choice = tryer(2,"Do you want to:\n(1) Go to in to Arskatown\n(2) Fight the guard")
        if choice == 1:
            print "You walk past the guard and enter Arskatown"
        if choice == 2:
            arskaTownAgro = 1
    if arskaTownAgro == 1:
        print "Guard: PREPARE FOR BATTLE!" 
        if arskaTown_guard.hp > 0:
            encounter(player,arskaTown_guard)
        if arskaTown_guard.hp <= 0:
            print "Me, defeated?, HOW???"
    pass #add healer, add bridge fetch quest, add travel possibilities.


########
#Bridge# cordinates (1,2)
########
def bridge(player, bridgeTroll):
    global location
    if bridgeTroll.hp > 0:
        print "A troll appears from below the bridge\n"
        encounter(player, bridgeTroll)#line 265
        print "The troll growls painfully as it sinks down into the river."
        time.sleep(2)
    if bridgeTroll.hp <= 0:
        print "You see a dead troll by the bridge"
        time.sleep(2)
        print "\n" * 60
        choice = tryer(2,"You crossed the bridge safely\n(1)Go west\n(2)Go east")
        if choice == 1:
            location = [1,1]
            return player, bridgeTroll
        if choice == 2:
            location = [3,1]
            return player, bridgeTroll
        
    
    
    
    
###########
#World Map#
###########


location = [0,0]
arskaTownAgro = 0 #0 -> agro no. 1 -> agro yes.
arskaTownQuest1 = 0 #0 -> fetchquest not taken yet. 1 -> fetchquest taken. 2 -> fetchquest finnished(allow crossing to bridge)
darkTowerBoss = 1 #1 -> boss alive. 0 -> boss killed and loot collected
evil_wizard = evil_wizard()
goblin = goblin()
door = large_door() #in DarkTower
arskaTown_guard = arskaTown_guard()
bridgeTroll = bridgeTroll()
while player.hp > 0:
    print "\n"*60
    print "-----------\n|OVERWORLD|\n-----------"

    if location == [0,0]: #NoobCave
        print "You see a cave!"
        yesno1 = tryer(2,"Do you want to enter?\n(1)Yes\n(2)No")
        if yesno1 == 1:
            cave(player,goblin)
        else:
            print "\n"*60
            print "-----------------------------------"
            print "North of you there is a Dark tower.\nIn all other directions there are mountains."
            print "-----------------------------------"
            testmove1 = 2
            testmove1 = tryer(2,"Move North?\n(1)Yes\n(2)No.\n")
            if testmove1 == 1:
                location = [0,1]

    if location == [0,1]: #Dark Tower
        print "You see a DARK TOWER!!!"
        yesno2 = tryer(2,"Do you want to enter?\n(1)Yes\n(2)No")
        if yesno2 == 1:
            noob_tower(player,goblin,evil_wizard)
        if yesno2 == 2:
            print "\n"*60
            yesno2_2 = tryer(4,"(1)in the north you see TOBEADDED\n(2)in the east you see a friendly looking village\n(3)in the south you see a cave in the mountains\n(4)i think i want to stay here.")
            if yesno2_2 == 1:
                location = [0,2]
            if yesno2_2 == 2:
                location = [1,1]
            if yesno2_2 == 3:
                location = [0,0]
            else:
                pass

    if location == [1,1]: #ArskaTown
        print "\n"*60
        yesno3 = tryer(2,"You see a village! It looks nice and comfortable.\nDo you want to go to the village?\n(1)Yes\n(2)No.\n")
        if yesno3 == 1:
            arskaTown(player,arskaTown_guard)
        if yesno3 == 2:
            yesno3_2 = tryer(2,"(1)DEV_TP to bridge or return to (2)tower?")
            if yesno3_2 == 1: #TODO: REMOVE AFTER FETCHQUEST IS ADDED
                location = [1,2]
            if yesno3_2 == 2:
                location = [1,0]
            else:
                pass

    if location == [1,2]:
        print "You have arrived to a bridge" #update later, tryer() line 265
        print "There is an old warning sign next to the bridge. it looks menacing."
        time.sleep(4)
        print "\n"*60
        cross = tryer(2,"You sense something under the bridge\ndo you want to approach?\n(1)Yes\n(2)No\n")
        if cross == 1:
            bridge(player, bridgeTroll)
        if cross == 2:
            yesno4_2 = tryer(2,"(1) Back to ArkaTown\n(2)Try crossing the bridge")
            if yesno4_2 == 1:
                location = [1,1]
            if yesno4_2 == 2:
                pass






    print "ERROR ERROR MISSING LOCATION!!!!"




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

