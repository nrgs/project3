#By Seth and Narges

from random import *    #for random numbers.
from string import *    #for string functions.
from sys import *       #for exit function.
import function
import random
from random import choice


def main():

   #------------------------------Instruction------------------------------------##
   print ('\n\n\nWelcome to "Hunt the Wumpus"\n')
   # print ("The wumpus lives in a cave of 20 rooms. Each room has 3 tunnels to\n")
   # print ("Hazards:")
   # print (" Bottomless pits - Two rooms have bottomless pits in them. If you go")
   # print ("   there, you fall into the pit (& lose)!")
   # print (" Super bats - Two other rooms have super bats. If you go there, a")
   # print ("   bat grabs you and takes you to some other room at random\n")
   # print ("Wumpus:")
   # print ("   The wumpus is not bothered by hazards. (He has sucker feet and is")
   # print ("   too big for a bat to lift.)  Usually he is asleep. Two things")
   # print ("   wake him up: your shooting an arrow, or your entering his room.")
   # print ("   If the wumpus wakes, he moves to one room or stays still")
   # print ("   After that, if he is where you are, he eats you up and")
   # print ("   you lose!\n")
   # print ("You:")
   # print ("   Each turn you may move or shoot a crooked arrow.")
   # print ("   Moving:  You can move one room (through one tunnel).")
   # print ("   Arrows:  You have 5 arrows.  You lose when you run out.  Each")
   # print ("   arrow can go from 1 to 5 rooms.  You aim by telling the")
   # print ("   computer the rooms to which you want the arrow to go.  If the")
   # print ("   arrow can't go that way (if no tunnel) it moves at random to")
   # print ("   the next room.")
   # print ("   If the arrow hits the wumpus, you win.")
   # print ("   If the arrow hits you, you lose.\n")
   # print ("Warnings:")
   # print ("   When you are one room away from a wumpus or hazard, the computer")
   # print ("   says:")
   # print ('   Wumpus:  "I smell a wumpus!"')
   # print ('   Bat   :  "Bats nearby!"')
   # print ('   Pit   :  "I feel a draft!"\n')

   #-----------------------------End of the Instruction--------------------------#
   
if __name__=='__main__': 
   main()

   gameObjects = [0] * 6   #keeps track of where everything is using index
                           #index 0 = player, 1 & 2 = pits, 3 & 4 = bats, 5 = wumpus

   

start = True
while start:

   function.initPlayerRoom()
   function.initPits()
   function.initBats()
   function.initWumpus()
   function.cave()

   print ("you are in room number: ", function.getPlayerRoom(), '\n', sep='')
   
   game = True
   while game:
      #Do not allow the user to proceed without giving valid input.
      function.printGUIMap()
      function.printWarning()

      choice = ' '

      while choice != "s" and choice != "m" and choice != "q":
         if function.checkDeath() == 0: #return 0 if you are not standing on wumpus or in a pit
            game = False
            break

         choice = (input("Shoot, move, or quit (s/m/q)? "))
        

         if choice == "m":
            function.move()

         elif choice == "s":  #Shoot an arrow
            if (function.shoot() == True):
               game = False
               break

         elif choice == "q":    #Quit
            game = False
            break

         else:
            print("Invalid input, please try again!")

   if(game != True):

      while choice != "y" and choice != "n":
         choice = (input("Play again? (y/n)? "))
         if choice == "y":
            game = True
            break
         else:
            start = False
            break

  
