import random
from potionClass import potions

#Class for dealing with battles
class battle:
    def __init__(self,hero,inv,monster):
        self.hero = hero
        self.inv = inv
        self.monster = monster
        self.heroBlock = 0
        self.monsterBlock = 0
    
    #Battle manager manages turns until one side flees or dies
    def battleManager(self):
        battlingPlay = True
        battlingMons = True
        initiative = self.initiaitveDeterm()
        if (initiative):
            while(battlingPlay and battlingMons):
                battlingPlay = self.playerTurn()
                if (battlingPlay):
                    battlingMons = self.monsterTurn()
                else:
                    return(True)
            return(False)
        else:
            while(battlingPlay and battlingMons):
                battlingMons = self.monsterTurn()
                if (battlingMons):
                    battlingPlay = self.playerTurn()
                else:
                    return(False)
            return(True)
    
    #Determine if player or monster goes first (returns True if player 1st)
    def initiaitveDeterm(self):
        playerRole = random.randint(1,6)
        monsterRole = random.randint(1,6)
        if (playerRole >= monsterRole):
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
            while ((self.monsterBlock > 0) and (damageDeal > 0)):
                self.monsterBlock -= 1
                damageDeal -= 1
            #Deal remaning damage to monster
            self.monster.damage(damageDeal)
            return(True)
        
        #if player choses to block
        elif (choice == "block"):
            ac = self.inv.armorClass()
            if (ac >= 5):
                self.heroBlock += 2
                return(True)
            elif (ac >= 0):
                self.heroBlock += 2
                return(True)
            else:
                self.heroBlock += 2
                return(True)
        
        #if player choses to flee
        elif (choice == "flee"):
            fleeChance = random.randint(1,5)
            if (fleeChance == 1):
                print("\n[*] You fled!")
                rooms(self.inv,self.hero)
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
            if ("health potion" in self.inv.returnInv()):
                potions("health potion").healthPotion(self.hero)
                self.inv.removeItem("health potion")
                print("\n[*] You now have " + str(self.hero.returnHealth()) + " hitpoints.")
                return(True)
            else:
                print("\n[!] That is not in your inventory!")
                return(self.playerTurn())

        elif (choice == "drink super health potion"):
            if ("super health potion" in self.inv.returnInv()):
                potions("super health potion").superHealthPotion(self.hero)
                self.inv.removeItem("super health potion")
                print("\n[*] You now have " + str(self.hero.returnHealth()) + " hitpoints.")
                return(True)
            else:
                print("\n[!] That is not in your inventory!")
                return(self.playerTurn())

        else:
            print("\n[!] Unknown command...\nCommands are: attack, block, flee, check health")
            return(self.playerTurn())

    #Monsters battle turn
    def monsterTurn(self):
        #Check for monster death
        if (self.monster.returnHealth() <= 0):
            print("\nYou killed the monster.")
            return(False)

        #Monster damage
        damageDeal = self.monster.returnDamageDeal()
        damageDeal = random.randint(1,damageDeal)

        #Monster block
        blockValue = random.randint(1, self.monster.returnArmor())

        #Monster decision making
        decidingFactor = random.randint(1,10)

        #Monster health >= 5
        #Attack
        if ((decidingFactor >= 4) and (self.monster.returnHealth >= 5)):
            print("\nThe monster dealt you " + str(damageDeal) + " points of damage.")
            #First take damage from hero block value
            while ((self.heroBlock > 0) and (damageDeal > 0)):
                self.heroBlock -= 1
                damageDeal -= 1
            #Deal remaning damage to hero
            self.hero.damage(damageDeal)
            return(True)
        #Block
        elif ((decidingFactor >= 2) and (self.monster.returnHealth >= 5)):
            print("\nThe monster chose to block.")
            self.monsterBlock += blockValue
            return(True)
        #Flee
        elif ((decidingFactor == 1) and (self.monster.returnHealth >= 5)):
            print("\nThe monster fled")
            self.monster.damage(100000000)
            return(False)
        
        #Monster health < 5
        #Attack
        elif ((decidingFactor >= 7) and (self.monster.returnHealth < 5)):
            print("\nThe monster dealt you " + str(damageDeal) + " points of damage.")
            #First take damage from hero block value
            while ((self.heroBlock > 0) and (damageDeal > 0)):
                self.heroBlock -= 1
                damageDeal -= 1
            #Deal remaning damage to hero
            self.hero.damage(damageDeal)
            return(True)
        #Block
        elif ((decidingFactor >= 4) and (self.monster.returnHealth < 5)):
            print("\nThe monster chose to block.")
            self.monsterBlock += blockValue
            return(True)
        #Flee
        elif ((decidingFactor >= 1) and (self.monster.returnHealth < 5)):
            print("\nThe monster fled")
            self.monster.damage(100000000)
            return(False)
