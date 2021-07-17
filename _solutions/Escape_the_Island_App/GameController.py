from islandTiles.beach import tile as beach
from islandTiles.temple import tile as temple
from islandTiles.camp import tile as camp
from islandTiles.ravine import tile as ravine
from islandTiles.spring import tile as spring
import numpy as np

class GameController:

    #I've used a dictionary here to access the classes above by their names. This is called a map, and common in coding.
    island_map = {"temple": temple, 
                "spring": spring, 
                "beach": beach, 
                "ravine": ravine, 
                "camp": camp}

    def __init__(self):
        self.alive = True
        self.days = 0
        self.inventory = []

    def play(self):
        while(self.alive):
            if self.days == 0:
                print("You have washed up on a Deserted Island! You must search the island for Food and Water to survive until rescue...")
            print("Days on the deserted island: "+str(self.days))
            
            #Our code to search the Island goes here
            tile = self.island_map[input("Where would you like to search today? (temple, spring, beach, ravine, camp): ")]
            tile.enterTile()
            loot, encounter = tile.search()

            if encounter == "Crocodile":
                self.alive = False
                print("You are eaten by a Crocodile")
                continue
            elif encounter == "Crumbling Cliffs":
                self.alive = False
                print("The cliffs below you crumble and you fall to your death")
                continue
            
            if encounter == None:
                print("Your search yields nothing...")
            else:
                if loot != None:
                    print("You encounter "+str(encounter)+" and find "+str(loot))
                    self.inventory.append(loot)
                else:
                    print("You encounter "+str(encounter)+" but find nothing...")
                
            tile.leaveTile()
                
            #This is the start of our player input section. We'll modify this code to make the gameplay fun.
            decision = input("Keep searching the Deserted Island? (Y/N) ")
            if decision == 'quit':
                break
            elif decision == 'Y':
                print("Good choice, maybe you'll survive another day.")
            elif decision == 'N':
                print("Too bad! You're stuck here... Gotta keep searching.")
            else:
                print("I didn't understand. Maybe you've been stuck on this Island for too long...")
            self.days += 1
        else:
            print("Game over. You survived for "+str(self.days)+" days.")