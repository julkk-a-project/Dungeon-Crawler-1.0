from time import sleep, time
from PlayerClass.entitys import *
from logic.logic import *

def eulersMinigame(self, shortmanAnnoyed):
    eulerMan = eulersMonster()
    print("\n"*60)
    print("short man: So, you've come this far? have you any idea what lies byond?")
    try1 = tryer(2,"(1)lol no.\n(2)Yes, i know exactly what lies byond!")
    if try1 == 1:
        print("short man: Euler was a man, a GERMAN man. since he was german, he was a man of logic.")
        try2 = tryer(2,"(1)ur just a nazi.\n(2)Top kek. i like Germans.")
        if try2 == 1:
            shortmanAnnoyed += 1
            print("short man: wtf r u a sjw")
            sleep(2)
        print("shotr man: Men of logic are known for spending thier time on illogical things.")
        try3 = tryer(2,"(1)Ik all bout dat logik, toock a course of it myself...\n(2)lol wat is a logical?")
        if try3 == 2:
            shortmanAnnoyed += 1
            print("short man: wow ur rly trying my nerves")
            sleep(2)
        print("short man: Euler spent his days on the most worthless of tasks, that is crossing bridges in his own home town.")
        try4 = tryer(2,"(1)Ik the feelin'\n(2)lol he was just dumb")
        if try4 == 2:
            shortmanAnnoyed += 1
            print("...")
            sleep(2)
        

    return shortmanAnnoyed