import random

#Character building class
class character:
    def __init__(self,name,gender,age,race,classType,alignment,stats,health,maxHealth):
        self.name = name
        self.gender = gender
        self.age = age
        self.race = race
        self.classType = classType
        self.alignment = alignment
        self.stats = stats
        self.health = health
        self.maxHealth = maxHealth
    
    #Return character attributes
    def returnGender(self):
        return(self.gender)
    
    def returnAge(self):
        return(self.age)
    
    def returnRace(self):
        return(self.race)
    
    def returnClassType(self):
        return(self.classType)
    
    def returnClassName(self):
        return(self.classType.titleReturn())

    def returnAlignment(self):
        return(self.alignment)

    def returnStats(self):
        return(self.stats)
    
    def returnHealth(self):
        return(self.health)
    
    def returnMaxHealth(self):
        return(self.maxHealth)

    #Change health
    def damage(self, damage):
        self.health -= damage
        return(self.health)

    def heal(self, heal):
        while ((heal > 0) and (self.health < self.maxHealth)):
            self.health += 1
            heal -= 1
        return(self.health)

    #Determine vision type
    def vision(self):
        if (self.race == "half-elf"):
            return("infra")
        elif (self.race == "elf"):
            return("infra")
        elif (self.race == "dwarf"):
            return("low-light")
        else:
            return("regular")
    
    #Determine weapon bonuses from class and race
    def weaponBonus(self):
        #Weapon bonuses from class
        if (self.classType == "hunter"):
            crBonus = {"bow":2, "short sword":2}
        elif (self.classType == "paladin"):
            crBonus = {"hammer":2}
        elif (self.classType == "rogue"):
            crBonus = {"knife":2}
        elif (self.classType == "warrior"):
            crBonus = {"short swort":2, "axe":2}
        else:
            crBonus = {}
        
        #Weapon bonuses from race
        if (self.race == "elf"):
            if ("bow" in crBonus):
                crBonus["bow"] += 2
            else:
                crBonus.update({"bow":2})
        elif (self.race == "half-elf"):
            if ("short sword" in crBonus):
                crBonus["short sword"] += 2
            else:
                crBonus.update({"short sword":2})
        elif (self.race == "dwarf"):
            if ("hammer" in crBonus):
                crBonus["hammer"] += 2
            else:
                crBonus.update({"hammer":2})

        return(crBonus)
    
    #Chance to pick lock
    def pickLock(self):
        if ((self.stats["dexterity"] >= 16) and (self.classType == "rogue")):
            return(.90)
        elif ((self.stats["dexterity"] < 16) and (self.classType == "rogue")):
            return(.80)
        elif (self.stats["dexterity"] >= 17):
            return(.75)
        elif (self.stats["dexterity"] >= 15):
            return(.25)
        elif (self.stats["dexterity"] >= 12):
            return(.15)
        else:
            return(.05)
        
    #Chance to seduce character
    def seduce(self):
        if (self.stats["charisma"] >= 17):
            return(.75)
        elif (self.stats["charisma"] >= 15):
            return(.50)
        elif (self.stats["charisma"] >= 12):
            return(.35)
        else:
            return(.15)

    #Saving throws
    def saveVpoison(self):
        if (self.stats["constitution"] >= 17):
            return(.65)
        elif (self.stats["constitution"] >= 15):
            return(.45)
        elif (self.stats["constitution"] >= 12):
            return(.35)
        else:
            return(.15)

    def saveVstun(self):
        if (self.stats["dexterity"] >= 17):
            return(.65)
        elif (self.stats["dexterity"] >= 15):
            return(.45)
        elif (self.stats["dexterity"] >= 12):
            return(.35)
        else:
            return(.15)
        
    def saveVmagic(self):
        if (self.stats["wisdom"] >= 17):
            return(.65)
        elif (self.stats["wisdom"] >= 15):
            return(.45)
        elif (self.stats["wisdom"] >= 12):
            return(.35)
        else:
            return(.15)

    def saveVcrush(self):
        if (self.stats["strength"] >= 17):
            return(.65)
        elif (self.stats["strength"] >= 15):
            return(.45)
        elif (self.stats["strength"] >= 12):
            return(.35)
        else:
            return(.15)