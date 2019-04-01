# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 19:36:01 2018

@author: david


"""
types=("Mage","Medic","Archer","Spy","Warrior") #this is a tuple which is a list which is fixed (cannot be changed)

class enemy:
    def gen_new(self):
        self.enemy_type=enemy_types[randint(1,num)]
class character:

#mage and medic get extra stats but less weapon pro

    def new_mage(self):
        self.char_type=types[0]
        self.level=1
        self.stats={"attack":1,"defence":1,"magic":3,"stealth":1,"medicine":2}   #a type of list which uses keyword instead of index (called a dictionary)
        self.weapon_pro={"sword":1,"spear":1,"dagger":2,"board_sword":0,"axe":0,"bow":1,"crossbow":1}
        self.char_data={"class":self.char_type,"level":self.level,"stats":self.stats,"weapon proficentcy":self.weapon_pro}
        self.invintory=[]
        self.carry_weight=1
        

    def new_medic(self):
        self.char_type=types[1]
        self.level=1
        self.stats={"attack":1,"defence":1,"magic":2,"stealth":1,"medicine":3}
        self.weapon_pro={"sword":1,"spear":1,"dagger":2,"board_sword":0,"axe":0,"bow":1,"crossbow":1}
        self.char_data={"class":self.char_type,"level":self.level,"stats":self.stats,"weapon proficentcy":self.weapon_pro}
        self.invintory=[]
        self.carry_weight=1
        
        

    def new_archer(self):
        self.char_type=types[2]
        self.level=1
        self.stats={"attack":2,"defence":1,"magic":1,"stealth":2,"medicine":1}
        self.weapon_pro={"sword":1,"spear":1,"dagger":2,"board_sword":0,"axe":0,"bow":3,"crossbow":3}
        self.char_data={"class":self.char_type,"level":self.level,"stats":self.stats,"weapon proficentcy":self.weapon_pro}
        self.invintory=[]
        self.carry_weight=2
        
        

    def new_spy(self):
        self.char_type=types[1]
        self.level=1
        self.stats={"attack":1,"defence":1,"magic":1,"stealth":3,"medicine":1}
        self.weapon_pro={"sword":1,"spear":1,"dagger":3,"board_sword":0,"axe":0,"bow":1,"crossbow":1}
        self.char_data={"class":self.char_type,"level":self.level,"stats":self.stats,"weapon proficentcy":self.weapon_pro}
        self.invintory=[]
        self.carry_weight=2


    def new_warrior(self):
        self.char_type=types[1]
        self.level=1
        self.stats={"attack":3,"defence":3,"magic":0,"stealth":0,"medicine":0}
        self.weapon_pro={"sword":2,"spear":2,"dagger":1,"board_sword":2,"axe":2,"bow":0,"crossbow":0}
        self.char_data={"class":self.char_type,"level":self.level,"stats":self.stats,"weapon proficentcy":self.weapon_pro}
        self.invintory=[]
        self.carry_weight=3


class weapon:

#not fully set up yet
    def new_sword(self,name,damage,weight,skill_needed,elemental_effect,durability_left):
        self.name=name
        self.two_handed=0
        self.damage=damage
        self.weigth=weight
        self.skill_needed=skill_needed
        self.elemental_effect=elemental_effect
        self.durability_left=durability_left
        self.type="sword"

    # reiterate for other weapon types
        #pass to this function based on if it's random generated or custom/crafted

#class mission:

class arena:
    weather=("sunny","rainy","dry","muddy","damp","thunderstrom")
    location=("cave","feild","forest","moutains","urban","indoors","hilly")
    #extras verticality, ruggedness, usableness (limit randomness based on local) all on a 1-5 scale

        #if cave spawn certain list of usable evirmonet


david=character()
david.new_archer()
print(david.char_data)

gandolf= character()
gandolf.new_mage()
print (gandolf.char_data)
print (gandolf.stats["magic"])

'''
future plans ....
make a sample battle 
make an enemy generator based on your level on the location
    also they will have attacks screen will pop up with slash left e.t.c 
make uI (what does the users screen look like ) text based to start
(have accepted words list and interpret to see if the survice)
make story
make map which players will explore



'''

