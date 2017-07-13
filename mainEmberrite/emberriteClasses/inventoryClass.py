import random

#Inventory building class
class inventory:
    def __init__(self,hero,inv,armor,gold,weapon):
        self.hero = hero
        self.inv = inv
        self.armor = armor
        self.gold = gold
        self.weapon = weapon
    
    #Return inventory items
    def returnInv(self):
        return(self.inv[1:])
    
    def returnWeapon(self):
        return(self.weapon)
    
    def returnGold(self):
        return(self.gold)
    
    def returnArmor(self):
        return(self.armor)
    
    #Add or remove items from inventory
    def addItem(self,item):
        self.inv.append(item)
        return(self.inv[:1])

    def removeItem(self,item):
        self.inv.remove(item)
        return(self.inv[:1])

    #Determine AC
    def armorClass(self):
        if (self.armor == "plate-mail"):
            return(-2)
        elif (self.armor == "leather"):
            return(4)
        elif (self.armor == "chain-mail"):
            return(0)
        elif (self.armor == "cloth"):
            return(7)
    
    #Determine weapon damage range
    def weaponDamage(self):
        checkBonus = self.weapon.split(":")
        try:
            bonus = int(checkBonus[1][1:])
        except:
            bonus = 0
        if (self.weapon[:3] == "bow"):
            damageDeal = 4
        elif (self.weapon[:10] == "long sword"):
            damageDeal = 8
        elif (self.weapon[:11] == "short sword"):
            damageDeal = 6
        elif (self.weapon[:3] == "axe"):
            damageDeal = 6
        elif (self.weapon[:6] == "hammer"):
            damageDeal = 6
        elif (self.weapon[:5] == "knife"):
            damageDeal = 4
        return(damageDeal + bonus)

    #Equip weapon (limited by class)
    def equipWeapon(self,weapon):
        if ((weapon == "bow") and (self.hero.returnClassType() == "hunter")):
            self.weapon = "bow"
            return(self.weapon)
        elif ((weapon == "short sword") and ((self.hero.returnClassType() == "hunter") or (self.hero.returnClassType() == "rogue") or (self.hero.returnClassType() == "warrior"))):
            self.weapon = "short sword"
            return(self.weapon)
        elif ((weapon == "hammer") and (self.hero.returnClassType() == "paladin")):
            self.weapon = "hammer"
            return(self.weapon)
        elif ((weapon == "knife") and (self.hero.returnClassType() == "rogue")):
            self.weapon = "knife"
            return(self.weapon)
        elif ((weapon == "axe") and ((self.hero.returnClassType() == "warrior") or (self.hero.returnClassType() == "hunter"))):
            self.weapon = "axe"
            return(self.weapon)
        elif ((weapon == "long sword") and (self.hero.returnClassType() == "warrior")):
            self.weapon = "long sword"
            return(self.weapon)
        else:
            return("Weapon selected not compatible with class")

    #Equip armor (limited by class)
    def equipArmor(self,armor):
        if ((armor == "chain-mail") and ((self.hero.returnClassType() == "hunter") or (self.hero.returnClassType() == "warrior"))):
            self.armor = "chain-mail"
            return(self.armor)
        elif ((armor == "leather") and ((self.hero.returnClassType() == "hunter") or (self.hero.returnClassType() == "rogue") or (self.hero.returnClassType() == "warrior"))):
            self.armor = "leather"
            return(self.armor)
        elif ((armor == "plate-mail") and ((self.hero.returnClassType() == "paladin") or (self.hero.returnClassType() == "warrior"))):
            self.armor = "plate-mail"
            return(self.armor)
        elif (armor == "cloth"):
            self.armor = "cloth"
            return(self.armor)
        else:
            return("Armor selected not compatible with class")

    #Return True if torch on or False if off
    def torchStatus(self):
        if (self.inv[0] == "on"):
            return(True)
        else:
            return(False)
    
    #Turn torch on or off
    def changeTorch(self):
        if (self.inv[0] == "on"):
            self.inv[0] = "off"
            return("\n[*] Torch turned off")
        else:
            self.inv[0] = "on"
            return("\n[*] Torch turned on")
    
    #Gold management
    def addGold(self, gold):
        self.gold += gold
        return(self.gold)
    
    def spendGold(self, gold):
        self.gold -= gold
        return(self.gold)