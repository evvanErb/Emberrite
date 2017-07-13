import random
from emberriteClasses.characterClass import character
from emberriteClasses.monsterClass import monster
from emberriteClasses.battleClass import battle
from emberriteClasses.inventoryClass import inventory
from emberriteClasses.potionClass import potions

#Dealing with standard options
def standardOptions(choice,hero,inv):
    #Check inventory
    if (choice == "inventory"):
        return(inv.returnInv())
    
    #Clear screen
    elif (choice == "clear"):
        return("\n"*50)

    #Manage torch
    elif (choice == "check torch"):
        if (inv.torchStatus()):
            return("\n[*] Torch is on")
        else:
            return("\n[*] Torch is off")
    elif (choice == "change torch"):
        return(inv.changeTorch())
    elif (choice == "light torch"):
        if (not inv.torchStatus()):
            return(inv.changeTorch())
        else:
            return("\n[!] Torch is already on")
    
    #Manage weapon
    elif (choice == "change weapon"):
        weaponChoice = raw_input("\nEnter the weapon you would like to equip\n>>> ")
        if (weaponChoice in inv.returnInv()):
            temp = inv.returnWeapon()
            inv.equipWeapon(weaponChoice)
            inv.addItem(temp)
            inv.removeItem(weaponChoice)
            return("\n[*] Weapon changed to " + weaponChoice)
        else:
            return("\n[!] That weapon is not in your inventory")
    elif (choice == "check weapon"):
        return(inv.returnWeapon())

    #Manage armor
    elif (choice == "change armor"):
        armorChoice = raw_input("\nEnter the armor you would like to equip\n>>> ")
        if (armorChoice in inv.returnInv()):
            temp = inv.returnArmor()
            inv.equipArmor(armorChoice)
            inv.addItem(temp)
            inv.removeItem(armorChoice)
            return("\n[*] Armor changed to " + armorChoice)
        else:
            return("\n[!] That armor is not in your inventory")
    elif (choice == "check armor"):
        return(inv.returnArmor())
    
    #Manage gold
    elif (choice == "check gold"):
        return(inv.returnGold())

    #Manage health
    elif (choice == "check health"):
        return(hero.returnHealth())
    
    #Potions
    elif (choice == "drink health potion"):
        if ("health potion" in inv.returnInv()):
            potions("health potion").healthPotion(hero)
            inv.removeItem("health potion")
            return("\n[*] You now have " + str(hero.returnHealth()) + " hitpoints.")
        else:
            return("\n[!] That is not in your inventory!")

    elif (choice == "drink super health potion"):
        if ("super health potion" in inv.returnInv()):
            potions("super health potion").superHealthPotion(hero)
            inv.removeItem("super health potion")
            return("\n[*] You now have " + str(hero.returnHealth()) + " hitpoints.")
        else:
            return("\n[!] That is not in your inventory!")
    
    #Items that can not be taken/opened/closed
    elif (choice[:4] == "take"):
        return("\n[!] That can not be taken!")
    elif (choice[:4] == "open"):
        return("\n[!] That can not be opened!")
    elif (choice[:5] == "close"):
        return("\n[!] That can not be closed!")
    
    #If there is nothing to search for
    elif (choice == "search"):
        return("\n[!] You found nothing!")
    
    #The letter from the mailbox
    elif ((choice == "read letter") and ("letter" in inv.returnInv())):
        return("\nWelcome to Emberrite!")
    
    #Exit game
    elif (choice =="exit"):
        exit()
    
    #Unknown commands
    else:
        return("\n[!] Unknown command...")

#Welcome text
def title():
    #Print icon
    infile = open("Icon.txt", "r")
    icon = infile.read()
    infile.close
    print(icon)
    #Print welcome
    print("\nWelcome to Emberrite!!!")
    print("Created by Evvan Erb. Powered by Python.")

#Creating player character
def characterCreation():
    races = ["human","elf","dwarf","half-elf"]
    alignments = ["chaotic good","neutral good","lawful good","chaotic neutral","neutral","lawful neutral","chaotic evil","neutral evil","lawful evil"]
    classes = ["rogue","hunter","paladin","warrior"]

    name = raw_input("\nWhat is your name?\n>>> ")
    gender = raw_input("\nAre you a boy or a girl? (m or f)\n>>> ").lower()
    age = raw_input("\nHow old are you?\n>>> ")

    race = raw_input("\nWhat race are you?\n>>> ").lower()
    while (race not in races):
        print("\n[!] Non-playable race! Please enter one of the following:")
        print(races)
        race = raw_input("\nWhat race are you?\n>>> ").lower()

    classType = raw_input("\nWhat class are you?\n>>> ").lower()
    while (classType not in classes):
        print("\n[!] Non-playable class! Please enter one of the following:")
        print(classes)
        classType = raw_input("\nWhat class are you?\n>>> ").lower()
    
    if (classType == "paladin"):
        alignment = "lawful good"
    else:
        alignment = raw_input("\nWhat alignment are you?\n>>> ").lower()
        while (alignment not in alignments):
            print("\n[!] Non-playable alignment! Please enter one of the following:")
            print(alignments)
            alignment = raw_input("\nWhat alignment are you?\n>>> ").lower()

    #Randomly generate stats
    stats = {"strength":0,"dexterity":0,"charisma":0,"intelligence":0,"wisdom":0,"constitution":0}
    for stat in stats:
        stats[stat] = random.randint(10,18)
    
    #Determine health based on class
    if (classType == "rogue"):
        health = 15
    elif (classType == "hunter"):
        health = 30
    elif (classType == "paladin"):
        health = 45
    elif (classType == "warrior"):
        health = 35

    return(character(name,gender,age,race,classType,alignment,stats,health,health))

#Creating player inventory
def inventoryCreation(hero):
    if (hero.returnClassType() == "rogue"):
        return(inventory(hero,["off"],"leather",25,"knife"))

    elif (hero.returnClassType() == "hunter"):
        return(inventory(hero,["off"],"chain-mail",20,"bow"))

    elif (hero.returnClassType() == "paladin"):
        return(inventory(hero,["off"],"plate-mail",10,"hammer"))

    elif (hero.returnClassType() == "warrior"):
        return(inventory(hero,["off"],"chain-mail",20,"short sword"))
