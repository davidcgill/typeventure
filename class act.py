"""
Created on Fri Aug 17 18:20:21 2018

@author: david

making classes practice

This program creates a multi sided die

use MSdie() to make a die, and pass the number of sides you want
the die not only has properites (it's number) but also fucntions (roll)
"""

import random

class MSdie:
    #this makes a class, which allows us to store various data and fucntions for each intance (each die we make)


    class stats:
        def __init__(self):
            self.attack
            #class in a class to double dot method see bellow  to see it applied (doesn't make sense in the context)

     #always pass self to be able to access that intances infomation
    # the first variable always takes the purpose of self.. don't need to call it self but probably should
    def __init__(self,sides):
        #setting up instance varaibles... varibles that each instance will have
        self.sides=sides
        self.stats.attack=1 #gives an intial vlaue always.. this just demonstartes one way you can create a piece of infomation with more info inside it
        self.value=1

 #let's make some methods (actions to do to the object)
    def roll(self):
        self.value=random.randint(1,self.sides)
        return self.value

    #not really needed because it can be accessed with dot notation
    def getVal(self):
        return self.value


    #programing convetion says you shouldnt look for object values from outside it because then we are no longer blackboxing proberly? only use methods
    #this helps because we can change inside without breaking things which call it now


die1= MSdie(6)
#assigns self as die1 from now on
print(  die1.stats.attack  ) # these two directly access the data from die1
print ( die1.value )

#these two class functions of die1
print ( die1.roll() )
print (  die1.getVal()  )

die1.roll ()
print  ( die1.value )
print ( f"the die has {die1.sides} sides" )


