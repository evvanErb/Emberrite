import random
import items
import maps

#Class for dealing with battles
class battle:
    def __init__(self,hero,inv,npc):
        self.hero = hero
        self.inv = inv
        self.npc = npc
        self.heroBlock = 0
        self.npcBlock = 0
    
    #Battle manager manages turns until one side flees or dies
    def battleManager(self):
        battlingPlay = True
        battlingMons = True
        initiative = self.initiaitveDeterm()
        if (initiative):
            while(battlingPlay and battlingMons):
                battlingPlay = self.playerTurn()
                if (battlingPlay):
                    battlingMons = self.npcTurn()
                else:
                    return(True)
            return(False)
        else:
            while(battlingPlay and battlingMons):
                battlingMons = self.npcTurn()
                if (battlingMons):
                    battlingPlay = self.playerTurn()
                else:
                    return(False)
            return(True)
    
    #Determine if player or monster goes first (returns True if player 1st)
    def initiaitveDeterm(self):
        playerRole = random.randint(1,6)
        npcRole = random.randint(1,6)
        if (playerRole >= npcRole):
            print("\n[*] You have initiative.")
            return(True)
        else:
            print("\n[*] The monster has initiative.")
            return(False)

    #Players battle turn
    def playerTurn(self):
        #check for player death
        if (self.hero.returnHealth() <= 0):
            print("\n[!] You died!")
            exit()

        #determine if class/race bonus applies
        bonus = 0
        crBonus = self.hero.weaponBonus()
        weaponType = self.inv.returnWeapon()
        if (weaponType in crBonus):
            bonus += (crBonus[weaponType])

        #player action
        choice = raw_input("\n>>> ").lower()

        #if player choses to attack
        if (choice == "attack"):
            damageDeal = (self.inv.weaponDamage() + bonus)
            damageDeal = random.randint(1,damageDeal)
            print("\nYou dealt the monster " + str(damageDeal) + " points of damage.")
            #First take damage from monsters block value
            while ((self.npcBlock > 0) and (damageDeal > 0)):
                self.npcBlock -= 1
                damageDeal -= 1
            #Deal remaning damage to monster
            self.npc.damage(damageDeal)
            return(True)
        
        #if player choses to block
        elif (choice == "block"):
            ac = self.inv.armorClass()
            if (ac >= 5):
                self.heroBlock += 2
                return(True)
            elif (ac >= 0):
                self.heroBlock += 4
                return(True)
            else:
                self.heroBlock += 6
                return(True)
        
        #if player choses to flee
        elif (choice == "flee"):
            fleeChance = random.randint(1,5)
            if (fleeChance == 1):
                print("\n[*] You fled!")
                maps.rooms(self.inv,self.hero)
            else:
                print("\n[*] Flee atempt failed!")
                return(True)
        
        #if player wants to check their health
        elif (choice == "check health"):
            health = self.hero.returnHealth()
            print("\n[*] You have " + str(self.heroBlock) + " blocking points left")
            print("[*] You have " + str(health) + " hit points left")
            return(self.playerTurn())
        
        #If player wants to drink potion
        elif (choice == "drink health potion"):
            #iterate over inventory to check for health potion
            for i in range(len(self.inv.returnInv())):
                #if item is of type health potion
                if (isinstance(self.inv.returnInv()[i], items.healthPotion)):
                    #make sure its a regular health potion and not super one
                    if(self.inv.returnInv()[i].returnName().lower() == "health potion"):
                        #heal hero and delete item from inventory
                        self.inv.returnInv()[i].heal(self.hero)
                        self.inv.removeItem(self.inv.returnInv()[i])
                        print("\n[*] You now have " + str(self.hero.returnHealth()) + " hitpoints.")
                        return(True)
            #else return its not in inv
            print("\n[!] That is not in your inventory!")
            return(self.playerTurn())
            
        elif (choice == "drink super health potion"):
            #iterate over inventory to check for health potion
            for i in range(len(self.inv.returnInv())):
                #if item is of type health potion
                if (isinstance(self.inv.returnInv()[i], items.superHealthPotion)):
                    #heal hero and delete item from inventory
                    self.inv.returnInv()[i].heal(self.hero)
                    self.inv.removeItem(self.inv.returnInv()[i])
                    print("\n[*] You now have " + str(self.hero.returnHealth()) + " hitpoints.")
                    return(True)
                #else return its not in inv
            print("\n[!] That is not in your inventory!")
            return(self.playerTurn())

        else:
            print("\n[!] Unknown command...\nCommands are: attack, block, flee, check health")
            return(self.playerTurn())

    #Monsters battle turn
    def npcTurn(self):
        #Check for monster death
        if (self.npc.returnHealth() <= 0):
            print("\nYou killed the monster.")
            return(False)

        #Monster damage
        damageDeal = self.npc.returnDamageDeal()
        damageDeal = random.randint(1,damageDeal)

        #Monster block
        blockValue = random.randint(1, self.npc.returnArmor())

        #Monster decision making
        decidingFactor = random.randint(1,10)

        #Monster health >= 5
        #Attack
        if ((decidingFactor >= 4) and (self.npc.returnHealth >= 5)):
            print("\nThe monster dealt you " + str(damageDeal) + " points of damage.")
            #First take damage from hero block value
            while ((self.heroBlock > 0) and (damageDeal > 0)):
                self.heroBlock -= 1
                damageDeal -= 1
            #Deal remaning damage to hero
            self.hero.damage(damageDeal)
            return(True)
        #Block
        elif ((decidingFactor >= 2) and (self.npc.returnHealth >= 5)):
            print("\nThe monster chose to block.")
            self.npcBlock += blockValue
            return(True)
        #Flee
        elif ((decidingFactor == 1) and (self.npc.returnHealth >= 5)):
            print("\nThe monster fled")
            self.npc.damage(100000000)
            return(False)
        
        #Monster health < 5
        #Attack
        elif ((decidingFactor >= 7) and (self.npc.returnHealth < 5)):
            print("\nThe monster dealt you " + str(damageDeal) + " points of damage.")
            #First take damage from hero block value
            while ((self.heroBlock > 0) and (damageDeal > 0)):
                self.heroBlock -= 1
                damageDeal -= 1
            #Deal remaning damage to hero
            self.hero.damage(damageDeal)
            return(True)
        #Block
        elif ((decidingFactor >= 4) and (self.npc.returnHealth < 5)):
            print("\nThe monster chose to block.")
            self.npcBlock += blockValue
            return(True)
        #Flee
        elif ((decidingFactor >= 1) and (self.npc.returnHealth < 5)):
            print("\nThe monster fled")
            self.npc.damage(100000000)
            return(False)
