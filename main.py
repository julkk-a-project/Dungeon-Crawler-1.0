# -*- coding: utf-8 -*-

from time import sleep, time
from random import randint
from random import choice as ranchoice
import PlayerClass as PC
import logic as logic

class game:
    def __init__(self):
        self.main()


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
                        print(dottedLine[i])
                    else:
                        print(defaultLine[i])
                sleep(0.25)
                print("\n"*60)


        ################# CLASS CHOICE
        self.player = "???"
        print()
        self.name = eval(input("What is your name!\n"))
        try1 = 1
        try2 = 2
        while try2 != 1:
            print(("\n"*60))
            print ("___________")
            print()
            print ("XXX D C XXX")
            print ("XXX 1.0 XXX")
            print ("___________")
            while try1 == 1:
                klass = eval(input('CHOOSE YOUR CLASS!!\n(1)WARRIOR\n(2)MAGE\n(3)ROUGE\n(?)ROUGE LIKE\n'))
                if klass == "1" or klass == "WARRIOR" or klass == "warrior":
                    self.player = PC.warrior()
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
                    print("\n"*60)
                    print("BUG")
                    sleep(1)
                    print("\n"*60)
                    try1 = 1

            print("\n"*60)
            print("____________________________")
            print()
            print("Your name is ", self.name)
            print("Your class is", self.player.klass)
            print("____________________________")
            print()
            print("THESE ARE YOUR EPIC STATS!!!")
            print("____________________________")
            print()
            print("Health    Points:",self.player.hp)
            print("Streingth Points:",self.player.st)
            print("Magic     Points:",self.player.mp)
            print("Agility   Points:",self.player.ag)
            print("____________________________")
            print()
            try2 = eval(input("enter (1) if you are happy!\nAND (2) IF YOU WANT TO CHOOSE AGAAAIN!!!\n"))
            try1 = 1




        ###########
        #World Map#
        ###########


        self.location = [0,0]
        arskaTownAgro = 0 #0 -> agro no. 1 -> agro yes.
        self.arskaTownQuest1 = 0 #0 -> fetchquest not taken yet. 1 -> fetchquest taken. 2 -> fetchquest finnished(allow crossing to bridge)
        self.darkTowerBoss = 1 #1 -> boss alive. 0 -> boss killed and loot collected
        self.evil_wizard = self.evil_wizard()
        self.goblin = self.goblin()
        self.door = self.large_door() #in DarkTower
        self.arskaTown_guard = self.arskaTown_guard()
        self.bridgeTroll = self.bridgeTroll()
        self.boulder = self.boulder()
        while self.player.hp > 0:
            print("\n"*60)
            print(" _________")
            print("/         \\")
            print("|OVERWORLD|")
            print("\_________/")

            if self.location == [0,0]: #NoobCave
                print("You see a cave!")
                yesno1 = self.tryer(2,"Do you want to enter?\n(1)Yes\n(2)No")
                if yesno1 == 1:
                    self.cave()
                else:
                    print("\n"*60)
                    print("-----------------------------------")
                    print("North of you there is a Dark tower.\nIn all other directions there are mountains.")
                    print("-----------------------------------")
                    testmove1 = 2
                    testmove1 = self.tryer(2,"Move North?\n(1)Yes\n(2)No.\n")
                    if testmove1 == 1:
                        self.location = [0,1]

            elif self.location == [0,1]: #Dark Tower
                print("You see a DARK TOWER!!!")
                yesno2 = self.tryer(2,"Do you want to enter?\n(1)Yes\n(2)No")
                if yesno2 == 1:
                    self.noob_tower()
                elif yesno2 == 2:
                    print("\n"*60)
                    yesno2_2 = self.tryer(4,"(1)in the north you see TOBEADDED\n(2)in the east you see a friendly looking village\n(3)in the south you see a cave in the mountains\n(4)i think i want to stay here.")
                    if yesno2_2 == 1:
                        self.location = [2,0]
                    elif yesno2_2 == 2:
                        self.location = [1,1]
                    elif yesno2_2 == 3:
                        self.location = [0,0]

            elif self.location == [1,1]: #ArskaTown
                print("\n"*60)
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
                print("You have arrived to a bridge") #update later, self.tryer() line 265
                print("There is an old warning sign next to the bridge. it looks menacing.")
                sleep(4)
                print("\n"*60)
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
                print("You see a temple") #Improve lore
                print("You feel something strong coming from the temple, you can't resit the urge to enter.")  #TODO where to next?, what if no pickup statue?
                sleep(3)
                print("\n" * 20)
                print("after walking for a couple minutes you arrive at a pedestal where you see a idol, you feel a strong presence from it.")
                choice = self.tryer(2, "Take the statue?\n(1)Yes\n(2)No\n")#line 261
                if choice == 1:
                    self.sunTemple(self.player,self.boulder)#line 597

            else:
                print("ERROR ERROR MISSING LOCATION!!!!")
                self.location = [0,0]
                sleep(3)
        # Location that can make Agro == 0


        print("add stuff here")


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
