# -*- coding: utf-8 -*-

from time import sleep, time
from random import randint
from random import choice as ranchoice

class game:
    def __init__(self):
        self.main()


################
#PLAYER CLASSES#
################

    #TODO: make player classes subclasses of a master "player class".
    class basePlayer:
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

    class rougel:
        def __init__(self):
            self.klass = "RougeLike"
            self.level = 1
            self.maxxp = (self.level * 3) ** 2
            self.maxhp = randint(8,20)
            self.hp = self.maxhp
            self.st = randint(1,5)
            self.mp = randint(0,5)
            self.ag = randint(1,3)
            self.xp = self.maxhp + self.st + self.mp + self.ag
        def heal(self):
            self.hp = self.maxhp
        def setXp(self):
            self.maxxp = (self.level * 3) ** 2


################
#ENTITY CLASSES#
################


    #TODO: make entity classes subclasses of a master "entity class".
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
        #TODO: add a base "animation".
        



    class goblin:
        klass = "Goblin"
        level = 1 #unnecesary when subclass
        maxxp = (level * 3) ** 2 #unnecesary when subclass
        maxhp = 5
        hp = maxhp #unnecesary when subclass
        st = 1 #unnecesary when subclass
        mp = 0 #unnecesary when subclass
        ag = 1 #unnecesary when subclass
        xp = maxhp + st + mp + ag #?unnecesary when subclass?
        def fixhealth(self): #unnecesary when subclass
            self.hp = self.maxhp


    class evil_wizard: #Use only in drak tower
        klass = "Evil Wizard"
        level = 3
        maxxp = (level * 3) ** 2 #unnecesary when subclass
        maxhp = 10
        hp = maxhp #unnecesary when subclass
        st = 2
        mp = 4
        ag = 1 #unnecesary when subclass
        xp = maxhp + st + mp + ag #?unnecesary when subclass?
        grand = False
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
            

    class bridgeTroll: #Bridge troll should stay dead when killed. maybe affect dialouges in ArskaTown when dead.
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
        st = 1 #TODO: change if new damage type is added. maybe a defensive stat that affects when fysical damage is used
        mp = 0
        ag = 0
        xp = maxhp + st + mp + ag
        def fixhealth(self):
            self.hp = self.maxhp


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

    class boulder:
        klass = "A effing boulder!!!"
        
        level = 100
        maxxp = (level * 3) ** 2
        maxhp = 9001
        hp = maxhp
        st = 9001
        mp = 0 #AAAAAAAAAAAAAAAAAAAAAAAAAAAH!!!
        ag = 9001
        xp = 9001
        def fixhealth(self):
            self.hp = self.maxhp
        

    class sunPriest:
        klass = "Sun priest"
        level = 3
        maxxp = (level * 3) ** 2
        maxhp = 10
        hp = maxhp
        st = 2
        mp = 5
        ag = 1
        xp = maxhp + st + mp + ag
        def fixhealth(self):
            self.hp = self.maxhp
            
    ###########
    #Encounter#
    ###########
    def encounter(self, player,entity,entity2 = 0,entity3 = 0,entity4 = 0,entity5 = 0):

        #TODO: add short animation to all entities
        print "\n"*60
        print "YOU ENCOUNTERED A", entity.klass, "!"
        print
        #entity.taunt #TODO: ADD ME WHEN ENTITIES ARE SUBCLASSES OF baseEntity.
        sleep(2) #TODO: remove this, and place into the baseEntity when it's done.
        self.battle(player,entity,entity2,entity3,entity4,entity5)



    ################
    #Choice handler#
    ################

    def tryer(self, num,string,is_inventory = 0):
        while True:
            print string
            if is_inventory != 1:
                print "(A)open inventory"
            else:
                print "--IN INVENTORY--"
            try:
                trynum = input("   You chose: ")
                if trynum >= 1 and trynum <= num:
                    if type(trynum) == type(1):
                        return trynum
                else:
                    print "try an advertised number"
            except:
                if is_inventory != 1:
                    self.inventory()
                else:
                    print "Try a number, fool"
            

    #############
    #Dice roller#
    #############

    def dice(self, num): #num -> how big a die you throw
        number = randint(1,num)
        return number

    #################
    #jump,duck,dodge# used in sun temple line 599
    #################
    def jumpDuckDodge(self, player,boulder):
        jumpPrompt = "There is a stone on the ground in your way\n"
        duckPrompt = "You see a branch att head level\n"
        dodgePrompt = "A stone falls from the ceiling\n"
        boulderDist = 500
        promptList = [jumpPrompt, duckPrompt, dodgePrompt]
        #tryerPrompt = self.tryer(3,"(1)Jump\n(2)duck\n(3)dodge\n")
        print "Oh no it seems the way to the exit has taken som damage from all the shaking\n"
        for i in range(0, 7):
            start = time()
            event = ranchoice(promptList)
            print event
            eventChoice = self.tryer(3,"(1)Jump\n(2)duck\n(3)dodge\n")
            if event == jumpPrompt:
                if eventChoice == 1:
                    boulderDist -= 50
                    print "You jumped over the stone\n"           #TODO optimize distance and range values, update lore
                else:                                               
                    boulderDist -= 100
                    print "You stumbled over the stone.\n"
            elif event == duckPrompt:
                if eventChoice == 2:
                    boulderDist -= 50
                    print "You managed to run under the branch\n"
                else:
                    boulderDist -= 100
                    print "You smashed your head into the branch\n"
            elif event == dodgePrompt:
                if eventChoice == 3:
                    boulderDist -= 50
                    print "You dodged the stone\n"
                else:
                    boulderDist -= 100
                    print "You got hit by the stone\n"

            end = time()
            if end - start > 3:
                boulderDist -= 50
            if end - start > 10:
                boulderDist -= 50
            if boulderDist <= 0:
                print "It seems you got rolled over by a boulder.\n"
                self.battle(player,boulder)
                #self.player.hp = -999
                return player
            print "The boulder is", boulderDist, "meters away from crushing you.\n"
        print "\n" * 60
        print "You reached the exit."
            
        
            
           
            
        
#\                            ___Help!___
# \  - -\   #*#*#*#*#*#*#*#  |    \0/    |  #*#*#*#*#*#*#*#
# >> - -<>  # B a t t l e #  | Ver X Sus |  # s y s t e m #
# /  - -/   #*#*#*#*#*#*#*#  |____/ \____|  #*#*#*#*#*#*#*#
#/

    
    def battle(self, player,entity1,entity2 = 0,entity3 = 0,entity4 = 0,entity5 = 0):
            #Multiple enemy handler
        test = "" #to test if entity is an actual entity
        listA = [entity2,entity3,entity4,entity5]
        listE = [entity1] #entity1 is always an entity. you can't encounter zero entities.
        emptyList = [] #To compare with listE in while loop
        for i in listA:
            try:
                test += i.klass
                listE.append(i)
                print listE.klass
            except:
                print "removed", i
        


        
        print "\n"*60
        print "_______________"
        print
        print "BATTLE STARTED!"
        print "_______________"
        print
        print "you are figthing:"
        for i in listE:
            print i.klass, "lvl", i.level
        print "_______________"
        print
        while player.hp > 0 and listE != emptyList:
            print "--------------------------"
            print self.name, "health:", player.hp, "/", player.maxhp
            print "--------------------------\n"






                #PLAYER ATTACK HANDLER
            
            numb1 = 0
            if len(listE) > 0:
                for i in listE:
                    numb1 += 1
                    print "("+str(numb1)+")"+"lvl", i.level, i.klass, "["+str(i.hp)+"/"+str(i.maxhp)+"]" #Display enemy names and hp
                numb1 = 0
                
                entityNum = self.tryer(len(listE),"which entity do you want to attack from 1 - 5?\n") #TODO: make special adjustment to tryer to make this look beautiful
                entity = listE[entityNum-1]
            else:
                break

            attack = self.tryer(3,"which attack do you wish to chose?\n(1)Slash\n(2)Fireball\n(3)Nether, i want back to mommy ;(\n")
            print "\n" * 60
            
                    #PLAYER STREINGTH ATTACK
            if attack == 1:
                print "You use SLASH!!!"
                sleep(0.5)
                playerHit = self.agChek(player,entity)
                if playerHit == 1:
                    print "It was super effective!"
                    entity.hp -= player.st
                else:
                    print "The", entity.klass, "dodged your attack!!!"
                sleep(1)
                print "The", entity.klass, "has", entity.hp, "/", entity.maxhp, "health" + "\n"


                    #PLAYER MAGIC ATTACK
            elif attack == 2:
                print "You use FIREBALL!!!"
                sleep(0.5)
                playerHit = self.agChek(player,entity)
                if playerHit == 1:
                    print "It was super effective!"
                    entity.hp -= player.mp
                else:
                    print "The", entity.klass, "dodged your attack!!!"
                sleep(1)
                print entity.klass, "has", entity.hp, "/", entity.maxhp, "health" + "\n"


                    #PLAYER BEING A PUSSY
            else:
                escape = self.coward(player,entity)
                sleep(2)
                print "\n"*60
                if escape == 0:
                    pass
                if escape == 1:
                    return player,entity #IMPORTANT TODO: This makes it possible to skip any battle with enough agility



             #-#-#-#-#-#-#-#
            # XP and Death! #
             #-#-#-#-#-#-#-#

            if player.hp > 0:
                player.xp += entity.xp
                print "\n"
                print "Leveling progress:"
                print "------------------"
                print player.xp, "/", player.maxxp
                print "------------------"
                sleep(2)
                print "\n"*60
            else:
                print "\n"*60
                print "You died."
                sleep(6)
                quit()
        
                #dead entity eliminator
            indexMem = -1
            for i in listE:
                indexMem += 1
                if i.hp <= 0:
                    listE.remove(entity)


             #-#-#-#-#-#
            # Level up! #
             #-#-#-#-#-#


                
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
                    statplus = self.tryer(4,"WHICH SKILL DO YOU WANT TO INCREASE!\n(1)Health\n(2)Streingth\n(3)Magic")
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





            for i in range(len(listE)):
                entity = listE[i-1]

                    #ENTITY ATTACK HANDLER
                    
                if entity.st > entity.mp: #Simple "AI" to make the AI use weiged random attacks
                    if entity.mp <= 0:
                        attackE = 1
                    else:
                        humanizer = self.dice(3)
                        if humanizer == 3:
                            attackE = 2
                        else:
                            attackE = 1
                else:
                    if entity.st <= 0:
                        attackE = 2
                    else:
                        humanizer = self.dice(3)
                        if humanizer == 3:
                            attackE = 1
                        else:
                            attackE = 2
                if entity.hp > 0:


                        #ENEMY STREINGTH ATTACK
                    
                    if attackE == 1:
                        #sleep(1)
                        print entity.klass, "used SLASH!"
                        sleep(0.5)
                        playerDodge = self.agChek(entity, player)
                        if playerDodge == 1:
                            print "it was SUPER EFFECTIVE!" #Add agility chek/roll
                            player.hp -= entity.st
                        else:
                            print "You dodged the attack"
                        sleep(1)
                        print self.name, "has", player.hp, "/", player.maxhp, "HP LEFT!!!" #add armor calculation?


                        #ENEMY MAGIC ATTACK
                    
                    else:
                        #sleep(1)
                        print entity.klass, "used FIREBALL!"
                        sleep(0.5)
                        playerDodge = self.agChek(entity, player)
                        if playerDodge == 1:
                            print "it was SUPER EFFECTIVE!" #Add agility chek/roll
                            player.hp -= entity.mp
                        sleep(1)
                        print self.name, "has", player.hp, "/", player.maxhp, "HP LEFT!!!" #add armor calculation?




##         #-#-#-#-#-#-#-#
##        # XP and Death! #
##         #-#-#-#-#-#-#-#
##
##        if player.hp > 0:
##            player.xp += entity.xp
##            print "\n"
##            print "Leveling progress:"
##            print "------------------"
##            print player.xp, "/", player.maxxp
##            print "------------------"
##            sleep(2)
##            print "\n"*60
##        else:
##            print "\n"*60
##            print "You died."
##            sleep(6)
##            quit()
##    
##            #dead entity eliminator
##        indexMem = -1
##        for i in listE:
##            indexMem += 1
##            if i.hp <= 0:
##                listE.remove(entity)
##
##
##         #-#-#-#-#-#
##        # Level up! #
##         #-#-#-#-#-#
##
##
##            
##        if player.xp >= player.maxxp:
##            print
##            print
##            print "YOU LEVELED UP!"
##            print "____________________________"
##            print
##            print "Level", player.level, player.klass
##            print "____________________________"
##            print
##            print "THESE ARE YOUR EPIC STATS!!!"
##            print "____________________________"
##            print
##            print "Health    Points:",player.hp, "/", player.maxhp
##            print "Streingth Points:",player.st
##            print "Magic     Points:",player.mp
##            print "Agility   Points:",player.ag
##            print "____________________________"
##            print
##            player.level += 1
##            trystat = 1
##            while trystat == 1:
##                statplus = self.tryer(4,"WHICH SKILL DO YOU WANT TO INCREASE!\n(1)Health\n(2)Streingth\n(3)Magic")
##                healpoints = player.maxhp
##                if statplus == 1:
##                    player.maxhp += 1
##                    player.hp += 1
##                    trystat = 0
##                elif statplus == 2:
##                    player.st += 1
##                    trystat = 0
##                elif statplus == 3:
##                    player.mp += 1
##                    trystat = 0
##                elif statplus == 4:
##                    player.ag += 1
##                    trystat = 0
##                else:
##                    print "my nibba, try an advertised number!"
##            player.xp -= player.maxxp
##            player.setXp()
                        
        print "\nbattle ended\n"
                
    ########################
    #Run awaay loik a poosy#
    ########################

    def coward(self, player,entity):
        #playerA = 0
        playerA = player.ag
        playerD = 0
        #entityA 
        entityA = entity.ag
        entityD = 0
        
        while playerA > 0:
            playerD += self.dice(6)
            playerA -= 1
        while entityA > 0:
            entityD += self.dice(6)
            entityA -= 1

        print "you got", playerD
        print "The", entity.klass, "got", entityD
        
        if playerD > entityD:
            print "EZ escape"
            return 1
        elif playerD == entityD:
            test2 = self.dice(2)
            if test2 == 1:
                print "You barely escaped"
                return 1
            else:
                print "You tripped"
                return 0
        elif playerD < entityD:
            print "You're worthless at running"
            return 0

                
    #######################
    #DIRTY COPY OF RUNNING# <-- aka agility chek for attack. (USE WHEN WANT TO CHEK AGILITY W/O RANDOM TEXTS)
    #######################     TODO: Could be combined with "coward(X,Y)"

    def agChek(self, attacker,defender): #return 1 if hit, 0 if miss.
        print "----------------------------------------------------"
        playerA = attacker.ag #TODO: change player variable to attacker
        playerD = 0
        entityA = defender.ag #TODO: change entity variable to defender
        entityD = 0
        
        while playerA > 0:
            playerD += self.dice(6)
            playerA -= 1
        while entityA > 0:
            entityD += self.dice(6)
            entityA -= 1

        print attacker.klass, "got", playerD
        print defender.klass, "got", entityD
        entityDMod = int(entityD * 0.5)
        print "Dodge modifier changes defender's value to", entityDMod
        print "----------------------------------------------------"
        sleep(1)
        
        if playerD > entityD:
            print "EZ Hit"
            return 1
        elif playerD >= entityDMod:
            test2 = self.dice(2)
            if test2 == 1:
                print attacker.klass, "barely hit"
                return 1
            else:
                print attacker.klass, "tripped"
                return 0
        elif playerD < entityDMod:
            print attacker.klass, "Is worthless at aiming"
            return 0


    ###########
    #Noob Cave# cordinates (0,0)
    ###########

    def cave(self):
        print "\n"*60
        print "you walk around in the cave."
        while True:
            chanse = randint(0,5)
            chanse = 1 # since 1 is the only thing that allows the program to continue might as well save resourcess till some other events are added
            if chanse == 1:
                self.goblin.fixhealth()
                self.encounter(self.player,self.goblin)
                print "\n"*60
                choice = self.tryer(2,"Do you want to turn over more rocks\n(1)Yes\n(2)No\n")
                if choice == 2:
                    return
            else:
                self.goblin.fixhealth()
                self.encounter(self.player,self.goblin)
                print "\n"*60
                choice = self.tryer(2,"Do you want to turn over more rocks\n(1)Yes\n(2)No\n")
                if choice == 2:
                    return



    ############
    #Dark Tower# cordinates (0,1)
    ############

    def noob_tower(self):
        print "\n"*60
        #Add art of the tower
        print "The Door is locked."
        yesno1 = self.tryer(2,"(1)Kick it in\n(2)Run away loik a poossy")
        if yesno1 == 1:
            self.battle(self.player,self.door)
            sleep(2)
            print "\n"*60
            print "The door swears it'll get Zer revenge,\nas it opens with an angry look about it."
            sleep(6)
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
                up = self.tryer(2,"Do you dare to keep climbing?\n(1)Yes! I HAVE THE POWEEEER!!!\n(2)nn-n-no i-i think i-i-i'll just go home now :(\n")
                if up == 1:
                    upp += 1
                else:
                    upp -= 1
                encounterChanse = randint(1,5)
                if upp <= 4:
                    if encounterChanse <= 2:
                        self.goblin.fixhealth()
                        self.encounter(self.player,self.goblin)
                    else:
                        print "\n"*60
                        print "think i heard something..."
                        sleep(2)
                elif upp > 4 and upp < 10:
                    if encounterChanse <= 2:
                        self.goblin.fixhealth()
                        self.encounter(self.player,self.goblin)
                    elif encounterChanse >= 4:
                        self.evil_wizard.fixhealth()
                        self.encounter(self.player,self.evil_wizard)
                    else:
                        print "\n"*60
                        print "It seems like the walls are talking to me :S"
                        sleep(3)
                elif upp >= 10:
                    print "\n"*60
                    print "----------------------------"
                    print "You made it to the top floor"
                    print "----------------------------"
                    self.evil_wizard.is_grand()
                    print "\nin front of you stands a grand wizard."
                    sleep(2)
                    print '\nWizard: "THIS IS MY LAIR! THAU SHALT NOT PASS!"\n\n'
                    sleep(2)
                    self.battle(self.player,self.evil_wizard)
                    #TODO: chek if wizard dead, end-taunt, loot, escape
                    
                        
                
        else:
            print "The door Laughs at you"
            sleep(2)
            return
        print "You climb the stairs of the tower."
        print
        print "The further you climb, the more of the dark magic you'll start to feel in your fingers."

    #########
    #Village# cordinates (1,1)
    #########

    def arskaTown(self, arskaTownAgro):
        print "Outside the village you see a sign, it says: Welcome to Arskatown"
        sleep(2)
        print "You also see a guard standing in front of you"
        if arskaTownAgro == 0:
            print "Guard: Hello there! You may enter Arskatown."
            sleep(2)
            print "You look at the guard and think: Damn I could get xp from that."
            choice = self.tryer(2,"Do you want to:\n(1) Go to in to Arskatown\n(2) Fight the guard")
            if choice == 1:
                print "You walk past the guard and enter Arskatown"
                self.Town()
                return arskaTownAgro
            elif choice == 2:
                arskaTownAgro = 1
    #    elif arskaTownAgro == 1:
        print "Guard: PREPARE FOR BATTLE!" 
        self.arskaTown_guard.fixhealth()
        sleep(3)
        if self.arskaTown_guard.hp > 0:
            self.encounter(self.player,self.arskaTown_guard)
        if self.arskaTown_guard.hp <= 0:
            print "Me, defeated?, HOW???"
            choice = self.tryer(2,"Where do you want to go?\n(1) Go to Dark Tower\n(2) Enter Town")
            if choice == 1:
                self.location = [0,1] 
                return arskaTownAgro
            elif choice == 2:
                self.Town()
                return arskaTownAgro
                
    def Town(self):
        global arskaTownQuest1
        while True:
            choice = self.tryer(4,"What do you want to do?\n(1) ?Healer?/Church?\n(2) Go to the bar.\n(3) Cross the bridge\n(4) Leave Arskatown")
            if choice == 1:
                self.herbalist()
            elif choice == 2:
                drunk = 0
                drunk = self.arskaBar()
                if drunk == 1:
                    return
            elif choice == 3:
                if arskaTownQuest1 == 0:
                    print "To cross the bridge you need to complete the Quest"
                    self.location = [1,2]
                    return 
                elif arskaTownQuest1 == 1:
                    print "Aha! i see you have the idol! you know who to show it to!"
                elif arskaTownQuest1 == 2:
                    print"You can cross the bridge"
                    self.location = [1,2]
                    return
            elif choice == 4:
                choice = self.tryer(2,"Hmm... Where to go?\n(1) Dark Tower\n(2) ??")
                if choice == 1:
                    self.location = [0,1]
                    return
                elif choice == 2:
                    #self.location = [?,?]
                    return
            #add healer, add bridge fetch quest, add travel possibilities.

    def herbalist(self):
        choice = self.tryer(2, "Do you want to heal?\n(1) Yes\n (2) No")
        self.player.heal()
        return

    def arskaBar(self):
        drunk = 0 
        locations = ([0,1],[1,1],[2,0],[1,2],[0,0])
        while True:
            choice = self.tryer(2,"Do you want to:\n(1) Take a drink\n(2) Leave the bar")
            if choice == 1:
                drunk += 1 
            elif choice == 2:
                print "You leave the bar"
                return 0
            if drunk == 6:
                print "\n"*60
                print "You are drunk"
                sleep(1)
                print "!"
                self.location = ranchoice(locations)
                print "\nyou find you wake up but you don't remember getting here"
                sleep(1)
                return 1
        

    ########
    #Bridge# cordinates (1,2)
    ########
    def bridge(self):
        justKilled = 0 #so troll status isn't displayed 2x
        if self.bridgeTroll.hp > 0:
            print "A troll appears from below the bridge\n"
            self.encounter(self.player, self.bridgeTroll)#line 265
            if self.bridgeTroll.hp <= 0:
                print "The troll growls painfully as it sinks down into the river."
                justKilled = 1
                sleep(2)
            else:
                return
        if self.bridgeTroll.hp <= 0:
            if justKilled != 1:
                print "You see a dead troll by the bridge"
                sleep(2)
            print "\n" * 60
            choice = self.tryer(2,"You crossed the bridge safely\n(1)Go west\n(2)Go east")
            if choice == 1:
                self.location = [1,1]
                return
            elif choice == 2:
                self.location = [3,1] # returns value to location
                return

    ############
    #Sun temple# cordinates [2,0]     
    ############    
    def sunTemple(self, player,boulder):
        print "After picking up the statue the ground starts shaking and you hear something huge coming towards you."        #TODO battles, pussles and other activities
        print "You probably should start running towards the exit."
        choice1 = self.tryer(2, "(1)Run\n(2)Stand still like a moron\n")
        if choice1 == 1:
           self.jumpDuckDodge(player,boulder)#line 287
        elif choice1 == 2:
            self.battle(player,boulder)
            print "Good job you just got smashed by a boulder and died."
            time(3)
        
    ###########
    # INVENTORY
    ###########
    #
    def inventory(self):
        
        if len(self.var_inventory) != 0: #If inventory empty, can't drop
            choice = self.tryer(3, "(1)Use an item\n(2)Check inventory\n(3)Drop an item",1)
        else:
            choice = self.tryer(2, "(1)Use an item\n(2)Check inventory",1)
        for i in range(len(self.var_inventory)):
            print i+1 ,self.var_inventory[i]
        if choice == 3:
            choice = self.tryer(len(self.var_inventory), "Which item to drop",1)
            self.var_inventory.pop(choice-1) #TODO: Can you drop multiples if more than one?
        elif choice == 1:
            choice = self.tryer(len(self.var_inventory), "Enter number of item to use",1)
            print item_values[self.var_inventory[choice-1]]
            # ASSIGN VALUES TO WHERE THEY SHOULD GO
            
            
            # remove item once used
            self.var_inventory.pop(choice-1)
        elif choice == 2:
            raw_input("Press enter to leave")

    def main(self):
        # PRE DEFINED ITEMS
        # TEST items               EX   NAME/ atk/ag/hp/mana
        item_values = {'HP POT':['HP POT',0,0,15,0],
                       'MANA POT':['MANA POT',0,0,0,10], 
                       'BEER':['BEER',5,-5,0,0], 
                       'BEEF':['BEEF',0,0,100,0]}


        self.var_inventory = []
        self.var_inventory.append("HP POT") 
        self.var_inventory.append("MANA POT")
        self.var_inventory.append("BEER")
        self.var_inventory.append("BEEF")

        # USE FOR DEBUGGING
        #for i in var_inventory:
        #    print str(i)
        #sleep(3)
        #

        #
        # Use the code on the below row when you want to use or drop item 
        # inventory(var_inventory)




        ############### Intro animation #TODO: make intro animation "grow", staring from just "D C" and "1.0", then the other stuff comes into existance. maybe with dots where it "grows", and then turn into "#".
        startTimes = 1
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
                sleep(0.25)
                print "\n"*60


        ################# CLASS CHOICE
        self.player = "???"
        print
        self.name = raw_input("What is your name!\n")
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
                    self.player = self.warrior()
                    try1 = 0
                elif klass == "2" or klass == "MAGE" or klass == "mage":
                    self.player = self.mage()
                    try1 = 0
                elif klass == "3" or klass == "ROUGE" or klass == "rouge":
                    self.player = self.rouge()
                    try1 = 0
                elif klass == "?" or klass == "ROUGE like" or klass == "rouge like":
                    self.player = self.rougel()
                    try1 = 0
                else:
                    print "\n"*60
                    print "BUG"
                    sleep(1)
                    print "\n"*60
                    try1 = 1
            
            print "\n"*60
            print "____________________________"
            print
            print "Your name is ", self.name
            print "Your class is", self.player.klass
            print "____________________________"
            print
            print "THESE ARE YOUR EPIC STATS!!!"
            print "____________________________"
            print
            print "Health    Points:",self.player.hp
            print "Streingth Points:",self.player.st
            print "Magic     Points:",self.player.mp
            print "Agility   Points:",self.player.ag
            print "____________________________"
            print
            try2 = input("enter (1) if you are happy!\nAND (2) IF YOU WANT TO CHOOSE AGAAAIN!!!\n")
            try1 = 1




        ###########
        #World Map#
        ###########


        self.location = [0,0]
        arskaTownAgro = 0 #0 -> agro no. 1 -> agro yes.
        arskaTownQuest1 = 0 #0 -> fetchquest not taken yet. 1 -> fetchquest taken. 2 -> fetchquest finnished(allow crossing to bridge)
        self.darkTowerBoss = 1 #1 -> boss alive. 0 -> boss killed and loot collected
        self.evil_wizard = self.evil_wizard()
        self.goblin = self.goblin()
        self.door = self.large_door() #in DarkTower
        self.arskaTown_guard = self.arskaTown_guard()
        self.bridgeTroll = self.bridgeTroll()
        self.boulder = self.boulder()
        while self.player.hp > 0:
            print "\n"*60
            print " _________"
            print "/         \\"
            print "|OVERWORLD|"
            print "\_________/"

            if self.location == [0,0]: #NoobCave
                print "You see a cave!"
                yesno1 = self.tryer(2,"Do you want to enter?\n(1)Yes\n(2)No")
                if yesno1 == 1:
                    self.cave()
                else:
                    print "\n"*60
                    print "-----------------------------------"
                    print "North of you there is a Dark tower.\nIn all other directions there are mountains."
                    print "-----------------------------------"
                    testmove1 = 2
                    testmove1 = self.tryer(2,"Move North?\n(1)Yes\n(2)No.\n")
                    if testmove1 == 1:
                        self.location = [0,1]

            elif self.location == [0,1]: #Dark Tower
                print "You see a DARK TOWER!!!"
                yesno2 = self.tryer(2,"Do you want to enter?\n(1)Yes\n(2)No")
                if yesno2 == 1:
                    self.noob_tower()
                elif yesno2 == 2:
                    print "\n"*60
                    yesno2_2 = self.tryer(4,"(1)in the north you see TOBEADDED\n(2)in the east you see a friendly looking village\n(3)in the south you see a cave in the mountains\n(4)i think i want to stay here.")
                    if yesno2_2 == 1:
                        self.location = [2,0]
                    elif yesno2_2 == 2:
                        self.location = [1,1]
                    elif yesno2_2 == 3:
                        self.location = [0,0]

            elif self.location == [1,1]: #ArskaTown
                print "\n"*60
                yesno3 = self.tryer(2,"You see a village! It looks nice and comfortable.\nDo you want to go to the village?\n(1)Yes\n(2)No.\n")
                if yesno3 == 1:
                    arskaTownAgro  = self.arskaTown(arskaTownAgro)
                elif yesno3 == 2:
                    yesno3_2 = self.tryer(2,"(1)DEV_TP to bridge or return to (2)tower?")
                    if yesno3_2 == 1: #TODO: REMOVE AFTER FETCHQUEST IS ADDED
                        self.location = [1,2]
                    elif yesno3_2 == 2:
                        self.location = [0,1]

            elif self.location == [1,2]:
                print "You have arrived to a bridge" #update later, self.tryer() line 265
                print "There is an old warning sign next to the bridge. it looks menacing."
                sleep(4)
                print "\n"*60
                cross = self.tryer(2,"You sense something under the bridge\ndo you want to approach?\n(1)Yes\n(2)No\n")#line 261
                if cross == 1:
                    self.bridge()
                elif cross == 2:
                    yesno4_2 = self.tryer(2,"(1) Back to ArkaTown\n(2)Try crossing the bridge")
                    if yesno4_2 == 1:
                        self.location = [1,1]
                    elif yesno4_2 == 2:
                        pass

            elif self.location == [2,0]: #Sun temple, check cordinates with master ;)
                print "You see a temple" #Improve lore
                print "You feel something strong coming from the temple, you can't resit the urge to enter."  #TODO where to next?, what if no pickup statue?
                sleep(3)
                print "\n" * 20
                print "after walking for a couple minutes you arrive at a pedestal where you see a idol, you feel a strong presence from it."
                choice = self.tryer(2, "Take the statue?\n(1)Yes\n(2)No\n")#line 261
                if choice == 1:
                    self.sunTemple(self.player,self.boulder)#line 597
                
            else:
                print "ERROR ERROR MISSING LOCATION!!!!"
                self.location = [0,0]
                sleep(3)
        # Location that can make Agro == 0


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

game()
