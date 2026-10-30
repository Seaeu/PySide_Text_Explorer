import random

## Locations
class locations:
    def __init__(self):
        pass

    def shop():
        pass

    def abandoned_cabin(self):
        pass

    def dungeon(self):
        pass

def crossroads(A,B,C=None,D=None): #Illusion of Choice
        Location = "???"
        Choices = [A,B,C,D]
        while Location not in Choices:
            if C==None and D==None:
                print("You come to a bend in the road",end=", ")
                Location=input(f"go to {A} or {B} ? ")
            elif C==None or D==None:
                print("You come to a junction in the road",end=", ")
                Location=input(f"go to {A}, {B}, or {C or D}? ")
            else:
                print("You come to a crossroads",end=", ")
                Location=input(f"go to {A}, {B}, {C}, or {D}? ")
        destination = getattr(locations,Location,None)
        destination()
