import random

#Potions
class potions:
    def __init__(self,name):
        self.name = name
    
    #Return values
    def returnName(self):
        return(self.name)
    
    #Healing potion
    def healthPotion(self,character):
        character.heal(5)
        return("\n[*] You have been healed 5 hit points")
    
    def superHealthPotion(self,character):
        charatcer.heal(15)
        return("\n[*] You have been healed 5 hit points")