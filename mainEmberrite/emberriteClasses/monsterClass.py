import random

#Monster building class
class monster:
    def __init__(self,name,health,armor,damageDeal):
        self.name = name
        self.health = health
        self.armor = armor
        self.damageDeal = damageDeal
    
    #Return monster attributes
    def returnName(self):
        return(self.name)
    
    def returnHealth(self):
        return(self.health)
    
    def returnArmor(self):
        return(self.armor)
    
    def returnDamageDeal(self):
        return(self.damageDeal)

    #Change health
    def damage(self, damage):
        self.health -= damage
        return(self.health)

    def heal(self, heal):
        while ((heal > 0) and (self.health < self.maxHealth)):
            self.health += 1
            heal -= 1
        return(self.health)