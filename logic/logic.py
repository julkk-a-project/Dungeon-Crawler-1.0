from random import randint
from random import choice as ranchoice
from time import sleep, time

###########
#Encounter#
###########
def encounter(self, player,entity1,entity2 = 0,entity3 = 0,entity4 = 0,entity5 = 0):

    #TODO: add short animation to all entities
    print("\n"*60)
    print("YOU ENCOUNTERED A", entity1.klass, "!")
    print()
    entity1.taunt()
    battle(player,entity1,entity2,entity3,entity4,entity5)



################
#Choice handler#
################

def tryer(num,string,is_inventory = 0):
    while True:
        print(string)
        if is_inventory != 1:
            print("(A)open inventory")
        else:
            print("--IN INVENTORY--")
        try:
            trynum = eval(input("   You chose: "))
            if trynum >= 1 and trynum <= num:
                if type(trynum) == type(1):
                    return trynum
            else:
                print("try an advertised number")
        except:
            if is_inventory != 1 and trynum == "A":
                inventory()
            else:
                print("Try a number, fool")


#############
#Dice roller#
#############

def dice( num): #num -> how big a die you throw
    number = randint(1,num)
    return number

#################
#jump,duck,dodge# used in sun temple line 599
#################
def jumpDuckDodge( player,boulder):
    jumpPrompt = "There is a stone on the ground in your way\n"
    duckPrompt = "You see a branch att head level\n"
    dodgePrompt = "A stone falls from the ceiling\n"
    boulderDist = 500
    promptList = [jumpPrompt, duckPrompt, dodgePrompt]
    #tryerPrompt = tryer(3,"(1)Jump\n(2)duck\n(3)dodge\n")
    print("Oh no it seems the way to the exit has taken som damage from all the shaking\n")
    for i in range(0, 7):
        start = time()
        event = ranchoice(promptList)
        print(event)
        eventChoice = tryer(3,"(1)Jump\n(2)duck\n(3)dodge\n")
        if event == jumpPrompt:
            if eventChoice == 1:
                boulderDist -= 50
                print("You jumped over the stone\n")           #TODO optimize distance and range values, update lore
            else:
                boulderDist -= 100
                print("You stumbled over the stone.\n")
        elif event == duckPrompt:
            if eventChoice == 2:
                boulderDist -= 50
                print("You managed to run under the branch\n")
            else:
                boulderDist -= 100
                print("You smashed your head into the branch\n")
        elif event == dodgePrompt:
            if eventChoice == 3:
                boulderDist -= 50
                print("You dodged the stone\n")
            else:
                boulderDist -= 100
                print("You got hit by the stone\n")

        end = time()
        if end - start > 3:
            boulderDist -= 50
        if end - start > 10:
            boulderDist -= 50
        if boulderDist <= 0:
            print("It seems you got rolled over by a boulder.\n")
            battle(player,boulder)
            #self.player.hp = -999
            return player
        print("The boulder is", boulderDist, "meters away from crushing you.\n")
    print("\n" * 60)
    print("You reached the exit.")






#\                            ___R.I.P___
# \  - -\   #*#*#*#*#*#*#*#  |    \0/    |  #*#*#*#*#*#*#*#
# >> - -<>  # B a t t l e #  | Ver X Sus |  # s y s t e m #
# /  - -/   #*#*#*#*#*#*#*#  |____/ \____|  #*#*#*#*#*#*#*#
#/


def battle(player,entity1,entity2 = 0,entity3 = 0,entity4 = 0,entity5 = 0):
        #Multiple enemy handler
    test = "" #to test if entity is an actual entity
    listA = [entity2,entity3,entity4,entity5]
    listE = [entity1] #entity1 is always an entity. you can't encounter zero entities.
    emptyList = [] #To compare with listE in while loop
    for i in listA:
        if type(i) == object:
            listE.append(i)




    print("\n"*60)
    print("_______________")
    print()
    print("BATTLE STARTED!")
    print("_______________")
    print()
    print("you are figthing:")
    for i in listE:
        print(i.klass, "lvl", i.level)
    print("_______________")
    print()
    while player.hp > 0 and listE != emptyList:
        print("--------------------------")
        print(player.name, "health:", player.hp, "/", player.maxhp)
        print("--------------------------\n")






            #PLAYER ATTACK HANDLER

        numb1 = 0
        if len(listE) > 0:
            for i in listE:
                numb1 += 1
                print("("+str(numb1)+")"+"lvl", i.level, i.klass, "["+str(i.hp)+"/"+str(i.maxhp)+"]") #Display enemy names and hp
            numb1 = 0

            entityNum = tryer(len(listE),"which entity do you want to attack from 1 - 5?\n") #TODO: make special adjustment to tryer to make this look beautiful
            entity = listE[entityNum-1]
        else:
            break

        attack = tryer(3,"which attack do you wish to chose?\n(1)Slash\n(2)Fireball\n(3)Nether, i want back to mommy ;(\n")
        print("\n" * 60)

                #PLAYER STREINGTH ATTACK
        if attack == 1:
            print("You use SLASH!!!")
            sleep(0.5)
            playerHit = agChek(player,entity)
            if playerHit == 1:
                print("It was super effective!")
                entity.hp -= player.st
            else:
                print("The", entity.klass, "dodged your attack!!!")
            sleep(1)
            print("The", entity.klass, "has", entity.hp, "/", entity.maxhp, "health" + "\n")


                #PLAYER MAGIC ATTACK
        elif attack == 2:
            print("You use FIREBALL!!!")
            sleep(0.5)
            playerHit = agChek(player,entity)
            if playerHit == 1:
                print("It was super effective!")
                entity.hp -= player.mp
            else:
                print("The", entity.klass, "dodged your attack!!!")
            sleep(1)
            print(entity.klass, "has", entity.hp, "/", entity.maxhp, "health" + "\n")


                #PLAYER BEING A PUSSY
        else:
            escape = coward(player,entity)
            sleep(2)
            print("\n"*60)
            if escape == 0:
                pass
            if escape == 1:
                return player,entity #This makes it possible to skip any battle with enough agility



         #-#-#-#-#-#-#-#
        # XP and Death! #
         #-#-#-#-#-#-#-#

        if player.hp > 0 and entity.hp <= 0:
            player.xp += entity.xp
            player.score += entity.xp #Change this to an entity score, when every entity has their own "score value". good for removing score when killing civilians.
            print("\n")
            print("Leveling progress:")
            print("------------------")
            print(player.xp, "/", player.maxxp)
            print("------------------")
            sleep(2)
            print("\n"*60)
        if player.hp <= 0:
            print("\n"*60)
            print("You died. your score was", player.score)
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
            print()
            print()
            print("YOU LEVELED UP!")
            print("____________________________")
            print()
            print("Level", player.level, player.klass)
            print("____________________________")
            print()
            print("THESE ARE YOUR EPIC STATS!!!")
            print("____________________________")
            print()
            print("Health    Points:",player.hp, "/", player.maxhp)
            print("Streingth Points:",player.st)
            print("Magic     Points:",player.mp)
            print("Agility   Points:",player.ag)
            print("____________________________")
            print()
            player.level += 1
            if player.agXp >= player.agMax:
                trystat = 2
            else:
                trystat = 1
            while trystat != 0:
                if trystat == 2:
                    statplus = tryer(4,"WHICH SKILL DO YOU WANT TO INCREASE!\n(1)Health\n(2)Streingth\n(3)Magic\n(4)Agility")
                else:
                    statplus = tryer(3,"WHICH SKILL DO YOU WANT TO INCREASE!\n(1)Health\n(2)Streingth\n(3)Magic")
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
                    if trystat == 2:
                        player.ag += 1
                        trystat = 0
                        player.AgXp = 0
                        player.setAgXp()
                        
                else:
                    print("my nibba, try an advertised number!")
            player.xp -= player.maxxp
            player.setXp()





        for i in range(len(listE)):
            entity = listE[i-1]

                #ENTITY ATTACK HANDLER

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


                    #ENEMY STREINGTH ATTACK

                if attackE == 1:
                    #sleep(1)
                    print(entity.klass, "used SLASH!")
                    sleep(0.5)
                    playerDodge = agChek(entity, player)
                    if playerDodge == 1:
                        print("it was SUPER EFFECTIVE!") #Add agility chek/roll
                        player.hp -= entity.st
                    else:
                        print("You dodged the attack")
                    sleep(1)
                    print(player.name, "has", player.hp, "/", player.maxhp, "HP LEFT!!!") #add armor calculation?


                    #ENEMY MAGIC ATTACK

                else:
                    #sleep(1)
                    print(entity.klass, "used FIREBALL!")
                    sleep(0.5)
                    playerDodge = agChek(entity, player)
                    if playerDodge == 1:
                        print("it was SUPER EFFECTIVE!") #Add agility chek/roll
                        player.hp -= entity.mp
                    sleep(1)
                    print(player.name, "has", player.hp, "/", player.maxhp, "HP LEFT!!!") #add armor calculation?


    print("\nbattle ended\n")

####################
#Agility XP Chekker#
####################

def agXpChekker(player):
    if player.agXp >= player.agXp:
        print("\nYour failiures have resulted in you learning how to actually use your muscles.\nYou can now increase your agility skill.")
        sleep(2)
        return
    else:
        return






########################
#Run awaay loik a poosy#
########################

def coward( player,entity):
    #playerA = 0
    playerA = player.ag
    playerD = 0
    #entityA
    entityA = entity.ag
    entityD = 0

    while playerA > 0:
        playerD += dice(6)
        playerA -= 1
    while entityA > 0:
        entityD += dice(6)
        entityA -= 1

    print("you got", playerD)
    print("The", entity.klass, "got", entityD)

    if playerD > entityD:
        print("EZ escape")
        return 1
    elif playerD == entityD:
        test2 = dice(2)
        if test2 == 1:
            print("You barely escaped")
            return 1
        else:
            print("You tripped")
            return 0
    elif playerD < entityD:
        print("You're worthless at running")
        player.agXp += 1
        agXpChekker(player)
        return 0


#######################
#DIRTY COPY OF RUNNING# <-- aka agility chek for attack. (USE WHEN WANT TO CHEK AGILITY W/O RANDOM TEXTS)
#######################     TODO: Could be combined with "coward(X,Y)"

def agChek( attacker,defender): #return 1 if hit, 0 if miss.
    print("----------------------------------------------------")
    playerA = attacker.ag #TODO: change player variable to attacker
    playerD = 0
    entityA = defender.ag #TODO: change entity variable to defender
    entityD = 0

    while playerA > 0:
        playerD += dice(6)
        playerA -= 1
    while entityA > 0:
        entityD += dice(6)
        entityA -= 1

    print(attacker.klass, "got", playerD)
    print(defender.klass, "got", entityD)
    entityDMod = int(entityD * 0.5)
    print("Dodge modifier changes defender's value to", entityDMod)
    print("----------------------------------------------------")
    sleep(1)

    if playerD > entityDMod:
        print("EZ Hit")
        return 1
    elif playerD == entityDMod:
        test2 = dice(2)
        if test2 == 1:
            print(attacker.klass, "barely hit")
            return 1
        else:
            print(attacker.klass, "tripped")
            return 0
    elif playerD < entityDMod:
        print(attacker.klass, "Is worthless at aiming")
        attacker.agXp += 1
        agXpChekker(attacker)
        return 0


###########
#Noob Cave# cordinates (0,0)
###########

def cave(self):
    print("\n"*60)
    print("you walk around in the cave.")
    while True:
        chanse = randint(0,5)
        chanse = 1 # since 1 is the only thing that allows the program to continue might as well save resourcess till some other events are added
        if chanse == 1:
            self.goblin.fixhealth()
            encounter(self, self.player,self.goblin)
            print("\n"*60)
            choice = tryer(2,"Do you want to turn over more rocks\n(1)Yes\n(2)No\n")
            if choice == 2:
                return
        else:
            self.goblin.fixhealth()
            encounter(self, self.player,self.goblin)
            print("\n"*60)
            choice = tryer(2,"Do you want to turn over more rocks\n(1)Yes\n(2)No\n")
            if choice == 2:
                return



############
#Dark Tower# cordinates (0,1)
############

def noob_tower(self):
    print("\n"*60)
    #Add art of the tower
    print("The Door is locked.")
    yesno1 = tryer(2,"(1)Kick it in\n(2)Run away loik a poossy")
    if yesno1 == 1:
        encounter(self, self.player,self.door)
        sleep(2)
        print("\n"*60)
        print("The door swears it'll get Zer revenge,\nas it opens with an angry look about it.")
        sleep(6)
        print("\n"*60)
        up = 1
        upp = 1
        while upp >= 1:
            print("\n"*60)
            print("~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'")
            print("The further you climb,\n the more of the dark magic you feel in your fingers.")
            print("~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'~'")
            print("\nYou climb the stairs of the tower.\n")
            print("You're on level", upp)
            print()
            up = tryer(2,"Do you dare to keep climbing?\n(1)Yes! I HAVE THE POWEEEER!!!\n(2)nn-n-no i-i think i-i-i'll just go home now :(\n")
            if up == 1:
                upp += 1
            else:
                upp -= 1
            encounterChanse = randint(1,5)
            if upp <= 4:
                if encounterChanse <= 2:
                    self.goblin.fixhealth()
                    encounter(self, self.player,self.goblin)
                else:
                    print("\n"*60)
                    print("think i heard something...")
                    sleep(2)
            elif upp > 4 and upp < 10:
                if encounterChanse <= 2:
                    self.goblin.fixhealth()
                    encounter(self, self.player,self.goblin)
                elif encounterChanse >= 4:
                    self.evil_wizard.fixhealth()
                    encounter(self, self.player,self.evil_wizard)
                else:
                    print("\n"*60)
                    print("It seems like the walls are talking to me :S")
                    sleep(3)
            elif upp >= 10:
                print("\n"*60)
                print("----------------------------")
                print("You made it to the top floor")
                print("----------------------------")
                self.evil_wizard.is_grand()
                print("\nin front of you stands a grand wizard.")
                sleep(2)
                print('\nWizard: "THIS IS MY LAIR! THAU SHALT NOT PASS!"\n\n')
                sleep(2)
                battle(self.player,self.evil_wizard)
                #TODO: chek if wizard dead, end-taunt, loot, escape



    else:
        print("The door Laughs at you")
        sleep(2)
        return
    print("You climb the stairs of the tower.")
    print()
    print("The further you climb, the more of the dark magic you'll start to feel in your fingers.")

#########
#Village# cordinates (1,1)
#########

def arskaTown(self, arskaTownAgro, arskaTownQuest1):
    print("Outside the village you see a sign, it says: Welcome to Arskatown")
    sleep(2)
    print("You also see a guard standing in front of you")
    if arskaTownAgro == 0:
        print("Guard: Hello there! You may enter Arskatown.")
        sleep(2)
        print("You look at the guard and think: Damn I could get xp from that.")
        choice = tryer(2,"Do you want to:\n(1) Go to in to Arskatown\n(2) Fight the guard")
        if choice == 1:
            print("You walk past the guard and enter Arskatown")
            Town(self,  arskaTownQuest1)
            return arskaTownAgro, arskaTownQuest1
        elif choice == 2:
            arskaTownAgro = 1
#    elif arskaTownAgro == 1:
    print("Guard: PREPARE FOR BATTLE!")
    self.arskaTown_guard.fixhealth()
    sleep(3)
    if self.arskaTown_guard.hp > 0:
        encounter(self, self.player,self.arskaTown_guard)
    if self.arskaTown_guard.hp <= 0:
        print("Me, defeated?, HOW???")
        choice = tryer(2,"Where do you want to go?\n(1) Go to Dark Tower\n(2) Enter Town")
        if choice == 1:
            self.location = [0,1]
            return arskaTownAgro, arskaTownQuest1
        elif choice == 2:
            Town(self, arskaTownQuest1)
            return arskaTownAgro, arskaTownQuest1

def Town(self, arskaTownQuest1):
    while True:
        choice = tryer(4,"What do you want to do?\n(1) ?Healer?/Church?\n(2) Go to the bar.\n(3) Cross the bridge\n(4) Leave Arskatown")
        if choice == 1:
            herbalist(self)
        elif choice == 2:
            drunk = 0
            drunk = arskaBar(self, arskaTownQuest1)
            if drunk == 1:
                return arskaTownQuest1
        elif choice == 3:
            if self.arskaTownQuest1 == 0:
                print("To cross the bridge you need to complete the Quest")
                self.location = [1,2]
                return arskaTownQuest1
            elif self.arskaTownQuest1 == 1:
                print("Aha! i see you have the idol! you know who to show it to!")
            elif self.arskaTownQuest1 == 2:
                print("You can cross the bridge")
                self.location = [1,2]
                return arskaTownQuest1
        elif choice == 4:
            choice = tryer(2,"Hmm... Where to go?\n(1) Dark Tower\n(2) ??")
            if choice == 1:
                self.location = [0,1]
                return arskaTownQuest1
            elif choice == 2:
                #self.location = [?,?]
                return arskaTownQuest1
        #add healer, add bridge fetch quest, add travel possibilities.

def herbalist(self):
    choice = tryer(2, "Do you want to heal?\n(1) Yes\n (2) No")
    self.player.heal()
    return

def arskaBar(self, arskaTownQuest1):
    self.pimpGuard1.fixhealth()
    self.pimpGuard2.fixhealth()
    if arskaTownQuest1 == 0:
        pimp = 0 #can't talk to yet
    elif arskaTownQuest1 == 1:
        pimp = 2 #"Have you completed my quest?"
    elif arskaTownQuest1 == 2:
        pimp = 3
    elif arskaTownQuest1 == 3:
        pimp = 4 #"Get out of my face. you lrdy have access."
    elif arskaTownQuest1 == -1:
        pimp -1 #Agro
        print("The pimp's guards are looking quite angrily at you....")
    drunk = 0 
    locations = ([0,1],[1,1],[2,0],[1,2],[0,0])
    print("The bar is full of people, drinking and having fun. some of them are even smiling!")
    sleep(3)
    print("\n*60")
    print("")
    while True:
        if pimp == 0:
            choice = tryer(3,"Do you want to:\n(1) Take a drink\n(2) Try to talk to someone\n(3) Leave the bar")
        elif pimp == 1:
            choice = tryer(4,"Do you want to:\n(1) Take a drink\n(2) Try to talk to someone\n(3) Try to talk to the fat pimp\n(4) Leave the bar")

            
            #Drink
        if choice == 1:
            drunk += 1
            if drunk == 6:
                print("\n"*60)
                print("You are drunk")
                sleep(1)
                print("!")
                self.location = ranchoice(locations)
                print("\nyou find you wake up but you don't remember getting here")
                sleep(1)
                return arskaTownQuest1
            

            #Socialize
        elif choice == 2 and pimp != -1:
            if drunk < 1:
                print("You're a reserved person. you'd never be able to talk to a stranger.")
                sleep(2)
                print("\n\n...not without some social lubricant")
                sleep(2)
                print("\n*60")
            else:
                print("you try to make conversation with the people, but those you tried to speak to had better things on their mind than your depressed ass.")
                sleep(2)
                if drunk > 3 and pimp == 0:
                    print("\nYou did see a fat pimp wearing a violet jacket and a golden undershirt in the corner of the bar. he looks like he means buisness.")
                    pimp = 1
                    sleep(3)
        elif choice == 2 and pimp == -1:
            if drunk < 1:
                print("You try to socialize but the angry looks of the pimp's guards scare you...")
                sleep(2)
                print("\n\n...you don't feel so secure here...")
                sleep(2)
                print("\n*60")
            else:
                print("you try to make conversation with the people, but those you tried to speak to had better things on their mind than your depressed ass.")
                sleep(2)
                if drunk > 3:
                    print("\nYou're so drunk you're not really in controll of your actions. this could be dangerous...")
                    sleep(3)
                    roll1 = dice(3)
                    if roll1 == 1:
                        encounter(self, self.player,self.pimpGuard1,self.pimpGuard2)
            

            #PimpChat
        elif pimp == 1 and choice == 3:
            print("you aproatch the fat pimp.")
            sleep(2)
            print("his bodyguards look at you seriously as you get closer")
            sleep(2)
            print("TEMPORARY TEXT: Hello, i am a pimp and i gib u quest. take it?")
            choice2 = tryer(3,"(1)Yes\n(2)No\(3)No, you're fat.")
            if choice2 == 1:
                pimp = 2
                arskaTownQuest1 = 1
            if choice2 == 3:
                pimp = -1
                encounter(self, self.player, self.pimpGuard1, self.pimpGuard2)
        elif pimp == 2 and choice == 3:
            print("Why are you bothering me again? ON WITH YOU! find that idol!")
            sleep(2)
        elif pimp == 3 and choice == 3:
            print("Aah... you found it.\nI'll tell my people to let you continue eastwards.")
            sleep(2)
            arskaTownQuest1 = 3
        elif pimp == 4 and choice == 3:
            print("Get off my face. you have everyting you want.")
            #Add battle system here maybe.
        else:
            print("You leave the bar")
            sleep(2)
            return arskaTownQuest1



########
#Bridge# cordinates (1,2)
########
def bridge(self):
    justKilled = 0 #so troll status isn't displayed 2x
    if self.bridgeTroll.hp > 0:
        print("A troll appears from below the bridge\n")
        encounter(self, self.player, self.bridgeTroll)#line 265
        if self.bridgeTroll.hp <= 0:
            print("The troll growls painfully as it sinks down into the river.")
            justKilled = 1
            sleep(2)
        else:
            return
    if self.bridgeTroll.hp <= 0:
        if justKilled != 1:
            print("You see a dead troll by the bridge")
            sleep(2)
        print("\n" * 60)
        choice = tryer(2,"You crossed the bridge safely\n(1)Go west\n(2)Go east")
        if choice == 1:
            self.location = [1,1]
            return
        elif choice == 2:
            self.location = [1,3] # returns value to location
            return

############
#Sun temple# cordinates [2,0]
############
def sunTemple( player,boulder):
    print("After picking up the statue the ground starts shaking and you hear something huge coming towards you.")        #TODO battles, pussles and other activities
    print("You probably should start running towards the exit.")
    choice1 = tryer(2, "(1)Run\n(2)Stand still like a moron\n")
    if choice1 == 1:
       jumpDuckDodge(player,boulder)#line 287
    elif choice1 == 2:
        encounter(self, self.player, self.boulder)
        print("Good job you just got smashed by a boulder and died.")
        time(3)

###########
# INVENTORY
###########
#
def inventory(self):

    if len(self.var_inventory) != 0: #If inventory empty, can't drop
        choice = tryer(3, "(1)Use an item\n(2)Check inventory\n(3)Drop an item",1)
    else:
        choice = tryer(2, "(1)Use an item\n(2)Check inventory",1)
    for i in range(len(self.var_inventory)):
        print(i+1 ,self.var_inventory[i])
    if choice == 3:
        choice = tryer(len(self.var_inventory), "Which item to drop",1)
        self.var_inventory.pop(choice-1) #TODO: Can you drop multiples if more than one?
    elif choice == 1:
        choice = tryer(len(self.var_inventory), "Enter number of item to use",1)
        print(item_values[self.var_inventory[choice-1]])
        # ASSIGN VALUES TO WHERE THEY SHOULD GO


        # remove item once used
        self.var_inventory.pop(choice-1)
    elif choice == 2:
        input("Press enter to leave")
