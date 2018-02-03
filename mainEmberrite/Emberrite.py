#!/usr/bin/python2

import random
import functions
import npcs
import battles
import people
import items

#Rooms
class rooms:
    def __init__(self,inv,hero):
        self.inv = inv
        self.hero = hero
        self.entrance()
    
    def entrance(self):
        #Description
        if (self.inv.torchStatus()):
            print("\nYou are in a small cellar.\nThere is a stairwell to the north.\nThere is a small crack in the wall to the south that you may be able to fit through.")
        else:
            print("\nYou are in a dark room.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.kitchen())
        elif ((choice == "s") or (choice == "south")):
            return(self.caveway())
        elif ((choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.entrance())
        elif (choice == "look"):
            return(self.entrance())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.entrance())

    def caveway(self):
        #Description
        if (self.inv.torchStatus()):
            print("\nYou are in a small winding rocky corridor.\nThere is a small opening to the north.\nThe corridor continues south.")
        else:
            print("\nYou are in a dark room.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.entrance())
        elif ((choice == "s") or (choice == "south")):
            return(self.cave())
        elif ((choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.caveway())
        elif (choice == "look"):
            return(self.caveway())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.caveway())

    def cave(self):
        #Check if monster still alive if so start battle
        global caveBugbear
        if (caveBugbear.returnHealth() > 0):
            print("\nYou've encountered a bugbear!")
            battles.battle(self.hero,self.inv,caveBugbear).battleManager()

        #Description
        if (self.inv.torchStatus()):
            print("\nYou are in a small cave.\nThere is a waterfall filling a pool of water to the south.\nThere is a small crack in the wall to the north that you may be able to fit through.")
        else:
            print("\nYou are in a dark room.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.caveway())
        elif ((choice == "s") or (choice == "south") or (choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.cave())
        elif (choice == "look"):
            return(self.cave())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.cave())

    def kitchen(self):
        global kitchenCupboard
        #Description
        print("\nYou are in a small kitchen.\nThere is a table with three chairs in front of you.\nIn the northwest corner of the room there is an oven.\nIn the northeast corner there is a cupboard.\nThere are doors to the north, east, and west.\nTo the south is a staricase descending down.")
        if (kitchenCupboard[0]):
            try:
                for i in kitchenCupboard[1:]:
                    print("There is "+ i + " in the cupboard")
            except:
                print("The cupboard is empty.")
        #Player choice
        #Directions
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.diningRoom())
        elif ((choice == "s") or (choice == "south")):
            return(self.entrance())
        elif ((choice == "w") or (choice == "west")):
            return(self.familyRoom())
        elif((choice == "e") or (choice == "east")):
            return(self.backyard())
        #Open cupboard
        elif (choice == "open cupboard"):
            print("\n[*] Cupboard opened")
            kitchenCupboard[0] = True
            return(self.kitchen())
        elif (choice == "close cupboard"):
            print("\n[*] Cupboard closed")
            kitchenCupboard[0] = False
            return(self.kitchen())
        #Take
        elif ((choice == "take salt") and (kitchenCupboard[0])):
            if ("salt" in kitchenCupboard):
                kitchenCupboard.remove("salt")
                self.inv.addItem("salt")
                print("\n[*] Salt taken.")
                return(self.kitchen())
            else:
                print("\n[!] Salt already taken.")
                return(self.kitchen())
        elif ((choice == "take garlic") and (kitchenCupboard[0])):
            if ("garlic" in kitchenCupboard):
                kitchenCupboard.remove("garlic")
                self.inv.addItem("garlic")
                print("\n[*] Garlic taken.")
                return(self.kitchen())
            else:
                print("\n[!] Garlic already taken.")
                return(self.kitchen())
        elif ((choice == "take health potion") and (kitchenCupboard[0])):
            if ("health potion" in kitchenCupboard):
                kitchenCupboard.remove("health potion")
                self.inv.addItem("health potion")
                print("\n[*] Health potion taken.")
                return(self.kitchen())
            else:
                print("\n[!] Health potion already taken.")
                return(self.kitchen())

        elif (choice == "look"):
            return(self.kitchen())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.kitchen())
        
    def backyard(self):
        #Description
        print("\nYou are in the backyard of an old log house.\nThere is an old battered door on the side of the house to your west.\nThere are paths into the woods to the east and north.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.walkway())
        elif ((choice == "w") or (choice == "west")):
            return(self.kitchen())
        elif ((choice == "e") or (choice == "east")):
            return(self.forest())
        elif ((choice == "s") or (choice == "south")):
            print("\n[!] You can not go that way!")
            return(self.backyard())
        elif (choice == "look"):
            return(self.backyard())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.backyard())
    
    def diningRoom(self):
        #Description
        print("\nYou are in a rectangular room.\nThere is a long table that appears to have hosted many meals in the center of the room.\nThere is cake on the table.\nOutside of the table and doors to the south and west there is not much here.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "s") or (choice == "south")):
            return(self.kitchen())
        elif ((choice == "w") or (choice == "west")):
            return(self.bedRoom())
        elif ((choice == "n") or (choice == "north") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.diningRoom())

        elif (choice == "look"):
            return(self.diningRoom())
        elif (choice == "take cake"):
            print("\n[!] The cake is a lie!")
            return(self.diningRoom())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.diningRoom())

    def familyRoom(self):
        #Description
        print("\nYou are in a small cozy room.\nThere is a fireplace that does not appear to have been used in quite some time.\nThere are two lounge charis in the center of the room.\nThere are doors to the north, east, and west.\nThe west wall has two boarded up windows on either side of the door.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.bedRoom())
        elif ((choice == "w") or (choice == "west")):
            return(self.frontPorch())
        elif ((choice == "e") or (choice == "east")):
            return(self.kitchen())
        elif ((choice == "s") or (choice == "south")):
            print("\n[!] You can not go that way!")
            return(self.familyRoom())
        elif (choice == "look"):
            return(self.familyRoom())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.familyRoom())

    def bedRoom(self):
        #Description
        print("\nYou are in a tiny room.\nThere is a disheveled bed in the corner of the room.\nThere are doors to the south and east.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "s") or (choice == "south")):
            return(self.familyRoom())
        elif ((choice == "e") or (choice == "east")):
            return(self.diningRoom())
        elif ((choice == "w") or (choice == "west") or (choice == "n") or (choice == "north")):
            print("\n[!] You can not go that way!")
            return(self.bedRoom())
        elif (choice == "look"):
            return(self.bedRoom())
        elif (choice == "sleep"):
            self.hero.heal(5)
            print("\n[*] You slept and now have " + str(self.hero.returnHealth()) + " hitpoints.")
            return(self.bedRoom())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.bedRoom())

    def frontPorch(self):
        global mailbox
        #Description
        print("\nYou are on the porch of an old wooden house.\nThe house has a door to the east.\nOn either side of the door are boarded up windows.\nThere is a mail box infront of the door.\nThere is a garden path to the north and a road leading south.")
        if (mailbox[0]):
            try:
                for i in mailbox[1:]:
                    print("There is "+ i + " in the mailbox")
            except:
                print("The mailbox is empty.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.walkway())
        elif ((choice == "e") or (choice == "east")):
            return(self.familyRoom())
        elif ((choice == "s") or (choice == "south")):
            return(self.road())
        elif ((choice == "w") or (choice == "west")):
            print("\n[!] You can not go that way!")
            return(self.frontPorch())
        elif (choice == "look"):
            return(self.frontPorch())
        #Take
        elif ((choice == "take letter") and (mailbox[0])):
            if ("letter" in mailbox):
                mailbox.remove("letter")
                self.inv.addItem("letter")
                print("\n[*] Letter taken.")
                return(self.frontPorch())
            else:
                print("\n[!] Letter already taken.")
                return(self.frontPorch())
        #Open mailbox
        elif (choice == "open mailbox"):
            print("\n[*] Mailbox opened")
            mailbox[0] = True
            return(self.frontPorch())
        elif (choice == "close mailbox"):
            print("\n[*] Mailbox closed")
            mailbox[0] = False
            return(self.frontPorch())
        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.frontPorch())

    def walkway(self):
        #Description
        print("\nYou are on a wooded pathway.\nThe path continues to the east and west.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "w") or (choice == "west")):
            return(self.frontPorch())
        elif ((choice == "e") or (choice == "east")):
            return(self.backyard())
        elif ((choice == "n") or (choice == "north") or (choice == "s") or (choice == "south")):
            print("\n[!] You can not go that way!")
            return(self.walkway())
        elif (choice == "look"):
            return(self.walkway())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.walkway())
    
    def forest(self):
        global forestCaveEntrance
        #Description
        print("\nYou are in the middle of a forest.")
        if (forestCaveEntrance):
            print("There is a cave entrance to the north.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if (((choice == "n") or (choice == "north")) and (forestCaveEntrance)):
            return(self.forestCave())
        elif ((choice == "w") or (choice == "west")):
            return(self.backyard())
        elif ((choice == "e") or (choice == "east")):
            return(self.clearing())
        elif ((choice == "s") or (choice == "south") or (choice == "n") or (choice == "north")):
            print("\n[!] You can not go that way!")
            return(self.forest())

        elif (choice == "look"):
            return(self.forest())
        elif (choice == "search"):
            searchVal = random.randint(1,6)
            if (searchVal <= 2):
                forestCaveEntrance = True
                print("\n[*] You found a secret cave entrance to the north!")
                return(self.forest())
            else:
                print("\n[!] You found nothing!")
                return(self.forest())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.forest())

    def forestCave(self):
        #Description
        if (self.inv.torchStatus()):
            print("\nYou are in an overgrown abandoned cave.\nThere is a small opening to the north.\nThere is light to the south.")
        else:
            print("\nYou are in a dark room.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.forestCaveway())
        elif ((choice == "s") or (choice == "south")):
            return(self.forest())
        elif ((choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.forestCave())
        elif (choice == "look"):
            return(self.forestCave())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.forestCave())
    
    def clearing(self):
        global unicorn
        #Description
        print("\nYou are in a clearing in the woods.\nThere are paths leading east and west.")
        if (unicorn):
            print("There is a unicorn in the middle of the clearing watching you carefully.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "w") or (choice == "west")):
            unicorn = False
            return(self.forest())
        elif ((choice == "e") or (choice == "east")):
            unicorn = False
            return(self.darkForest())
        elif ((choice == "n") or (choice == "north") or (choice == "s") or (choice == "south")):
            print("\n[!] You can not go that way!")
            return(self.clearing())
        elif (choice == "look"):
            return(self.clearing())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.clearing())
    
    def road(self):
        #Description
        print("\nYou are on a road.\nIt goes north and south.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.frontPorch())
        elif ((choice == "s") or (choice == "south")):
            return(self.town())
        elif ((choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.road())
        elif (choice == "look"):
            return(self.road())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.road())
    
    def forestCaveway(self):
        #Description
        if (self.inv.torchStatus()):
            print("\nYou are in a small dank passageway that leads north and south.")
        else:
            print("\nYou are in a dark room.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.waterfall())
        elif ((choice == "s") or (choice == "south")):
            return(self.forestCave())
        elif ((choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.forestCaveway())
        elif (choice == "look"):
            return(self.forestCaveway())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.forestCaveway())
    
    def darkForest(self):
        #Description
        if (self.inv.torchStatus()):
            print("\nYou are in a seemingly endless forest.\nThe smell of death is prevelant in the air.\nThe undergrowth seems to creep up on you everytime you look away.")
        else:
            print("\nYou are in a dark room.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.darkway())
        elif ((choice == "s") or (choice == "south")):
            return(self.bearCave())
        elif ((choice == "w") or (choice == "west")):
            return(self.clearing())
        elif ((choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.darkForest())
        elif (choice == "look"):
            return(self.darkForest())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.darkForest())

    def town(self):
        #Description
        print("\nYou are in small bustling town.\nPeople are hurrying around you on their days errands.\nThe Goldshire Inn is to the west.\nThere is a black smith to the east.\nThere are roads out of town to the north and south.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.road())
        elif ((choice == "s") or (choice == "south")):
            return(self.marshyPath())
        elif ((choice == "w") or (choice == "west")):
            return(self.inn())
        elif((choice == "e") or (choice == "east")):
            return(self.blackSmith())
        elif (choice == "look"):
            return(self.town())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.town())

    def waterfall(self):
        global waterfallCaveEntrance
        #Description
        print("\nYou are at the base of a giant waterfall in a ravene.\nThe shore runs to the east and to the south.")
        if (waterfallCaveEntrance):
            print("You notice a cave entrance behind the waterfall.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if (((choice == "n") or (choice == "north")) and (waterfallCaveEntrance)):
            return(self.waterfallCave())
        elif ((choice == "s") or (choice == "south")):
            return(self.forestCaveway())
        elif((choice == "e") or (choice == "east")):
            return(self.beach())
        elif ((choice == "w") or (choice == "west") or (choice == "n") or (choice == "north")):
            print("\n[!] You can not go that way!")
            return(self.waterfall())

        elif (choice == "look"):
            return(self.waterfall())
        elif (choice == "search"):
            searchVal = random.randint(1,6)
            if (searchVal <= 2):
                waterfallCaveEntrance = True
                print("\n[*] You found a secret cave entrance to the north!")
                return(self.waterfall())
            else:
                print("\n[!] You found nothing!")
                return(self.waterfall())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.waterfall())

    def bearCave(self):
        #Check if monster still alive if so start battle
        global bear,bearCaveSkeleton
        if (bear.returnHealth() > 0):
            print("\nYou've encountered a bear!")
            battles.battle(self.hero,self.inv,bear).battleManager()

        #Description
        if (self.inv.torchStatus()):
            print("\nYou are in a roomy cave.\nWater drips from the rocks overhead.\nThe smell of rotting corpses is prevelant.\nThere are skeletons in the corner of the room.")
        else:
            print("\nYou are in a dark room.")

        if ((len(bearCaveSkeleton) == 3) and (self.inv.torchStatus())):
            print("On one of the skeletons lies an axe and 50 gold pieces")
        elif ((bearCaveSkeleton[0] == "axe") and (self.inv.torchStatus())):
            print("On one of the skeletons lies an axe")
        elif ((bearCaveSkeleton[0] == "gold") and (self.inv.torchStatus())):
            print("On one of the skeletons lies 50 gold pieces")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.darkForest())
        elif ((choice == "s") or (choice == "south") or (choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.bearCave())
        elif (choice == "look"):
            return(self.bearCave())
        #Take
        elif (choice == "take gold"):
            if ("gold" in bearCaveSkeleton):
                bearCaveSkeleton.remove("gold")
                self.inv.addGold(50)
                print("\n[*] Gold taken.")
                return(self.bearCave())
            else:
                print("\n[!] Gold already taken.")
                return(self.bearCave())
        elif (choice == "take axe"):
            if ("axe" in bearCaveSkeleton):
                bearCaveSkeleton.remove("axe")
                self.inv.addItem("axe")
                print("\n[*] Axe taken.")
                return(self.bearCave())
            else:
                print("\n[!] Axe already taken.")
                return(self.bearCave())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.bearCave())

    def darkway(self):
        #Description
        if (self.inv.torchStatus()):
            print("\nYou are on a small path in the middle of a horrid forest.\nThe path seems to wind endlessly to the west and to the south.")
        else:
            print("\nYou are in a dark room.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "s") or (choice == "south")):
            return(self.darkForest())
        elif ((choice == "w") or (choice == "west")):
            return(self.ravene())
        elif ((choice == "e") or (choice == "east") or (choice == "n") or (choice == "north")):
            print("\n[!] You can not go that way!")
            return(self.darkway())
        elif (choice == "look"):
            return(self.darkway())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.darkway())
    
    def inn(self):
        #Description
        print("\nYou are in a well lit inn.\nThere are jovial people singing and dancing around you.\nThe barmaid is walking around looking for someone to talk to.\nThe entrance to the inn from the town is to the east.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "e") or (choice == "east")):
            return(self.town())
        elif ((choice == "w") or (choice == "west") or (choice == "s") or (choice == "south") or (choice == "n") or (choice == "north")):
            print("\n[!] You can not go that way!")
            return(self.inn())
        elif (choice == "look"):
            return(self.inn())
        
        #Barmaid
        elif ((choice == "talk to barmaid") or (choice == "talk to the barmaid")):
            barmaidService = True
            while (barmaidService):
                purchase = raw_input("\n'ello love what can I get for you?\n>>> ")
                if (purchase == "room"):
                    if (self.inv.returnGold() >= 20):
                        print("\nThat'll be 20 gold pieces. Thanks!")
                        self.hero.heal(20)
                        self.inv.spendGold(20)
                    else:
                        print("\nSorry love you don't have enough gold!")
                elif (purchase == "drink"):
                    if (self.inv.returnGold() >= 5):
                        print("\nThat'll be 5 gold pieces. Thanks!")
                        self.inv.spendGold(5)
                    else:
                        print("\nSorry love you don't have enough gold!")
                elif ((purchase == "stop") or (purchase == "leave")):
                    barmaidService = False
                else:
                    print("\nSorry love we don't have that!")
            return(self.inn())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.inn())
    
    def blackSmith(self):
        global smithInv
        #Description
        print("\nYou are in a blacksmith's shop.\nThe blacksmith is working at the forge.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "w") or (choice == "west")):
            return(self.town())
        elif ((choice == "e") or (choice == "east") or (choice == "s") or (choice == "south") or (choice == "n") or (choice == "north")):
            print("\n[!] You can not go that way!")
            return(self.blackSmith())
        elif (choice == "look"):
            return(self.blackSmith())
        
        #Blacksmith
        elif ((choice == "talk to blacksmith") or (choice == "talk to the blacksmith")):
            service = True
            while (service):
                for i in smithInv:
                    print("\nI have a " + i + " in-stock.")
                purchase = raw_input("\nWhat can I get for you?\n>>> ")
                if (purchase[:3] == "buy"):
                    buyingItem = raw_input("\nWhat would you like to buy?\n>>> ")
                    if (buyingItem in smithInv):
                        if (self.inv.returnGold() >= smithInv[buyingItem]):
                            print("\nThat'll be " + str(smithInv[buyingItem]) + " gold pieces. Thanks!")
                            self.inv.spendGold(smithInv[buyingItem])
                            self.inv.addItem(buyingItem)
                            del smithInv[buyingItem]
                        else:
                            print("\nYou don't have enough gold for that!")
                    else:
                        print("\nI don't have that!")
                elif ((purchase == "stop") or (purchase == "leave")):
                    service = False
                else:
                    print("\nI can't do that!")
            return(self.blackSmith())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.blackSmith())
    
    def marshyPath(self):
        #Description
        print("\nYou are on an old decaying pathway that leads north and south.\nVines sprawl across the path making it hard to walk.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.town())
        elif ((choice == "s") or (choice == "south")):
            return(self.marsh())
        elif ((choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.marshyPath())
        elif (choice == "look"):
            return(self.marshyPath())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.marshyPath())
    
    def ravene(self):
        #Description
        print("\nYou are at the top of a giant ravene.\nThere is a waterfall gushing down from the otherside of the chasm.\nThe path continues west and east.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "w") or (choice == "west")):
            return(self.lake())
        elif ((choice == "e") or (choice == "east")):
            return(self.darkway())
        elif ((choice == "n") or (choice == "north") or (choice == "s") or (choice == "south")):
            print("\n[!] You can not go that way!")
            return(self.ravene())
        elif (choice == "look"):
            return(self.ravene())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.ravene())

    def marsh(self):
        #Check if monster still alive if so start battle
        global waterElemental
        if (waterElemental.returnHealth() > 0):
            print("\nYou've encountered a beast with three heads looming from the marsh!\nOne head of a dragon, one of a griffon, and one of a chimera.")
            battles.battle(self.hero,self.inv,waterElemental).battleManager()

        #Description
        print("\nYou are in a smelly decaying marsh.\nThere are pathes to the north and to the east.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.marshyPath())
        elif ((choice == "e") or (choice == "east")):
            return(self.mountainPath())
        elif ((choice == "s") or (choice == "south") or (choice == "w") or (choice == "west")):
            print("\n[!] You can not go that way!")
            return(self.marsh())
        elif (choice == "look"):
            return(self.marsh())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.marsh())

    def waterfallCave(self):
        global waterfallTresure
        #Description
        if (self.inv.torchStatus()):
            print("\nYou are in a small wet cave.\nThe sound of rushing water can be heard to the south.")
        else:
            print("\nYou are in a dark room.")
        
        if ((len(waterfallTresure) == 3) and (self.inv.torchStatus())):
            print("Scattered through out the room is 756 gold pieces and a super health potion.")
        elif ((waterfallTresure[0] == "super health potion") and (self.inv.torchStatus())):
            print("There is a super health potion in the corner of the room")
        elif ((waterfallTresure[0] == "gold") and (self.inv.torchStatus())):
            print("Scattered about the room are tresures which sum to 756 gold pieces.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "s") or (choice == "south")):
            return(self.waterfall())
        elif ((choice == "n") or (choice == "north") or (choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.waterfallCave())
        elif (choice == "look"):
            return(self.waterfallCave())
        #Take
        elif (choice == "take gold"):
            if ("gold" in waterfallTresure):
                waterfallTresure.remove("gold")
                self.inv.addGold(756)
                print("\n[*] Gold taken.")
                return(self.waterfallCave())
            else:
                print("\n[!] Gold already taken.")
                return(self.waterfallCave())
        elif (choice == "take super health potion"):
            if ("super health potion" in waterfallTresure):
                waterfallTresure.remove("super health potion")
                self.inv.addItem("super health potion")
                print("\n[*] Super health potion taken.")
                return(self.waterfallCave())
            else:
                print("\n[!] Super health potion already taken.")
                return(self.waterfallCave())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.waterfallCave())

    def lake(self):
        #Description
        print("\nYou are on the shore of a giant lake.\nTo your east there is a path leading into a forest.\nTo your west there is a run down old hut.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "w") or (choice == "west")):
            return(self.witchesHut())
        elif ((choice == "e") or (choice == "east")):
            return(self.ravene())
        elif ((choice == "n") or (choice == "north") or (choice == "s") or (choice == "south")):
            print("\n[!] You can not go that way!")
            return(self.lake())
        elif (choice == "look"):
            return(self.lake())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.lake())
    
    def beach(self):
        #Description
        print("\nYou are on the shore of a beach.\nThe sand is wet and cold.\nThere is a path leading into a forest to your west.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "w") or (choice == "west")):
            return(self.waterfall())
        elif ((choice == "n") or (choice == "north") or (choice == "s") or (choice == "south") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.beach())
        elif (choice == "look"):
            return(self.beach())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.beach())
        
    def mountainPath(self):
        global mountainCaveEntrance
        #Description
        print("\nYou are on a mountain path.\nThere is a cave to the north.\nThe path runs north and south.")
        if (mountainCaveEntrance):
            print("There is another cave to the south.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if (((choice == "s") or (choice == "south")) and (mountainCaveEntrance)):
            return(self.mountainCave())
        elif ((choice == "w") or (choice == "west")):
            return(self.marsh())
        elif ((choice == "e") or (choice == "east")):
            return(self.graveyard())
        elif ((choice == "n") or (choice == "north")):
            return(self.dwellingCave())
        elif ((choice == "s") or (choice == "south")):
            print("\n[!] You can not go that way!")
            return(self.mountainPath())
        elif (choice == "look"):
            return(self.mountainPath())
        #Search
        elif (choice == "search"):
            searchVal = random.randint(1,6)
            if (searchVal <= 2):
                mountainCaveEntrance = True
                print("\n[*] You found a secret cave entrance to the north!")
                return(self.mountainPath())
            else:
                print("\n[!] You found nothing!")
                return(self.mountainPath())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.mountainPath())
        
    def witchesHut(self):
        #Check if monster still alive if so start battle
        global witch,witchesCellarDoor
        if (witch.returnHealth() > 0):
            print("\nYou've encountered a witch!")
            battles.battle(self.hero,self.inv,witch).battleManager()

        #Description
        print("\nYou are in a small dark hut.\nThere is a door to the east.")
        if (witchesCellarDoor):
            print("There is a trap door leading down.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "e") or (choice == "east")):
            return(self.lake())
        elif ((choice == "down") and (witchesCellarDoor)):
            return(self.witchesCellar())
        elif ((choice == "s") or (choice == "south") or (choice == "w") or (choice == "west") or (choice == "n") or (choice == "north")):
            print("\n[!] You can not go that way!")
            return(self.witchesHut())
        elif (choice == "look"):
            return(self.witchesHut())
        #Search
        elif (choice == "search"):
            searchVal = random.randint(1,6)
            if (searchVal <= 2):
                witchesCellarDoor = True
                print("\n[*] You found a secret trapdoor!")
                return(self.witchesHut())
            else:
                print("\n[!] You found nothing!")
                return(self.witchesHut())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.witchesHut())

    def witchesCellar(self):
        global witchesCellarInv
        #Description
        if (self.inv.torchStatus()):
            print("\nYou are in a roomy cave.\nWater drips from the rocks overhead.\nThere is a trap door leading up.")
        else:
            print("\nYou are in a dark room.")

        if ((len(witchesCellarInv) == 3) and (self.inv.torchStatus())):
            print("There is a super health potion and a health potion.")
        elif ((witchesCellarInv[0] == "super health potion") and (self.inv.torchStatus())):
            print("There is a health potion.")
        elif ((witchesCellarInv[0] == "health potion") and (self.inv.torchStatus())):
            print("There is a super health potion.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if (choice == "up"):
            return(self.witchesHut())
        elif ((choice == "n") or (choice == "north") or (choice == "s") or (choice == "south") or (choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.witchesCellar())
        elif (choice == "look"):
            return(self.witchesCellar())
        #Take
        elif (choice == "take super health potion"):
            if ("super health potion" in witchesCellarInv):
                witchesCellarInv.remove("super health potion")
                self.inv.addItem("super health potion")
                print("\n[*] Super health potion taken.")
                return(self.witchesCellar())
            else:
                print("\n[!] Super health potion already taken.")
                return(self.witchesCellar())
        elif (choice == "take health potion"):
            if ("health potion" in witchesCellarInv):
                witchesCellarInv.remove("health potion")
                self.inv.addItem("health potion")
                print("\n[*] Health potion taken.")
                return(self.witchesCellar())
            else:
                print("\n[!] Health potion already taken.")
                return(self.witchesCellar())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.witchesCellar())
    
    def dwellingCave(self):
        #Check if monster still alive if so start battle
        global lion,dwellingCaveSkeleton
        if (lion.returnHealth() > 0):
            print("\nYou've encountered a mountain lion!")
            battles.battle(self.hero,self.inv,lion).battleManager()

        #Description
        if (self.inv.torchStatus()):
            print("\nYou are in a roomy cave.\nWater drips from the rocks overhead.\nThe smell of rotting corpses is prevelant.\nThere are skeletons in the corner of the room.")
        else:
            print("\nYou are in a dark room.")

        if ((len(dwellingCaveSkeleton) == 3) and (self.inv.torchStatus())):
            print("On one of the skeletons lies a short sword and 256 gold pieces")
        elif ((dwellingCaveSkeleton[0] == "short sword") and (self.inv.torchStatus())):
            print("On one of the skeletons lies a short sword")
        elif ((dwellingCaveSkeleton[0] == "gold") and (self.inv.torchStatus())):
            print("On one of the skeletons lies 256 gold pieces")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "s") or (choice == "south")):
            return(self.mountainPath())
        elif ((choice == "n") or (choice == "north") or (choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.dwellingCave())
        elif (choice == "look"):
            return(self.dwellingCave())
        #Take
        elif (choice == "take gold"):
            if ("gold" in dwellingCaveSkeleton):
                dwellingCaveSkeleton.remove("gold")
                self.inv.addGold(256)
                print("\n[*] Gold taken.")
                return(self.dwellingCave())
            else:
                print("\n[!] Gold already taken.")
                return(self.dwellingCave())
        elif (choice == "take short sword"):
            if ("short sword" in dwellingCaveSkeleton):
                dwellingCaveSkeleton.remove("short sword")
                self.inv.addItem("short sword")
                print("\n[*] Short sword taken.")
                return(self.dwellingCave())
            else:
                print("\n[!] Short sword already taken.")
                return(self.dwellingCave())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.dwellingCave())

    def mountainCave(self):
        #Check if monster still alive if so start battle
        global troll,mountainCaveSkeletons
        if (troll.returnHealth() > 0):
            print("\nYou've encountered a troll!")
            battles.battle(self.hero,self.inv,troll).battleManager()

        #Description
        if (self.inv.torchStatus()):
            print("\nYou are in a roomy cave.\nWater drips from the rocks overhead.\nThe smell of rotting corpses is prevelant.\nThere are skeletons in the corner of the room.")
        else:
            print("\nYou are in a dark room.")

        if ((len(dwellingCaveSkeleton) == 3) and (self.inv.torchStatus())):
            print("On one of the skeletons lies an amulet and 567 gold pieces")
        elif ((dwellingCaveSkeleton[0] == "amulet") and (self.inv.torchStatus())):
            print("On one of the skeletons lies an amulet")
        elif ((dwellingCaveSkeleton[0] == "gold") and (self.inv.torchStatus())):
            print("On one of the skeletons lies 567 gold pieces")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "n") or (choice == "north")):
            return(self.mountainPath())
        elif ((choice == "s") or (choice == "south") or (choice == "w") or (choice == "west") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.mountainCave())
        elif (choice == "look"):
            return(self.mountainCave())
        #Take
        elif (choice == "take gold"):
            if ("gold" in mountainCaveSkeletons):
                mountainCaveSkeletons.remove("gold")
                self.inv.addGold(567)
                print("\n[*] Gold taken.")
                return(self.mountainCave())
            else:
                print("\n[!] Gold already taken.")
                return(self.mountainCave())
        elif (choice == "take amulet"):
            if ("amulet" in dwellingCaveSkeleton):
                dwellingCaveSkeleton.remove("amulet")
                self.inv.addItem("amulet")
                print("\n[*] Amulet taken.")
                return(self.mountainCave())
            else:
                print("\n[!] Amulet already taken.")
                return(self.mountainCave())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.mountainCave())
    
    def graveyard(self):
        #Check if monster still alive if so start battle
        global skeleton
        if (skeleton.returnHealth() > 0):
            print("\nYou've encountered a skeleton!")
            battles.battle(self.hero,self.inv,skeleton).battleManager()

        #Description
        print("\nYou are in a graveyard.\nThere is a path leadin west.\nTo the east is a giant castle looming over the small graveyard.")

        #Player choice
        choice = raw_input("\n>>> ").lower()
        if ((choice == "w") or (choice == "west")):
            return(self.mountainPath())
        elif ((choice == "s") or (choice == "south") or (choice == "n") or (choice == "north") or (choice == "e") or (choice == "east")):
            print("\n[!] You can not go that way!")
            return(self.graveyard())
        elif (choice == "look"):
            return(self.graveyard())

        #Check for standard option
        else:
            print(functions.standardOptions(choice,self.hero,self.inv))
            return(self.graveyard())

#Variables that trigger events and monsters
caveBugbear = npcs.npc("bugbear",10,2,4)
kitchenCupboard = [False,"salt","garlic","health potion"]
mailbox = [False,"letter"]
forestCaveEntrance = False
unicorn = True
waterfallCaveEntrance = False
bear = npcs.npc("bear",25,4,10)
bearCaveSkeleton = ["axe","gold",""]
smithInv = {"long sword":50,"plate-mail":120}
waterElemental = npcs.npc("water elemental",40,1,12)
waterfallTresure = ["super health potion","gold",""]
mountainCaveEntrance = False
witch = npcs.npc("witch",25,1,12)
witchesCellarDoor = False
witchesCellarInv = ["super health potion","health potion",""]
lion = npcs.npc("mountain lion",20,2,8)
dwellingCaveSkeleton = ["short sword","gold",""]
troll = npcs.npc("troll",50,3,10)
mountainCaveSkeletons = ["amulet","gold",""]
skeleton = npcs.npc("skeleton",10,1,5)

#********MAIN********
#title()
hero = functions.characterCreation()
inv = functions.inventoryCreation(hero)
print("\n[*] Character created!")
rooms(inv,hero)