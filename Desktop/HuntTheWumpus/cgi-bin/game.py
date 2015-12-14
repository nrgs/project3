#!/usr/bin/env python3
#By Seth and Narges

import http.cookies
import cgi
import pickle
from random import *    #for random numbers.
from string import *    #for string functions.
from sys import *       #for exit function.
import function
import random
from random import choice

caving = []
MapCave = []
Arrows = [5]
listSize = 20
list1 = [1, 2, 3,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
gameObjects = [0] * 6	#keeps track of where everything is using index
						#index 0 = player, 1 & 2 = pits, 3 & 4 = bats, 5 = wumpus 

def printGUIMap():
	rooms = [-1] * 3
	for item in MapCave:
		if item[0] == gameObjects[0]:
			for i in range(0, 3):
				if rooms[i] == -1:
					rooms[i] = item[1]
					break
		if item[1] == gameObjects[0]:
			for i in range(0, 3):
				if rooms[i] == -1:
					rooms[i] = item[0]
					break
	print("<p>----------->[", rooms[0], "]</p>")
	print("<p>[", gameObjects[0], "]----->[", rooms[1], "]</p>")
	print("<p>----------->[", rooms[2], "]</p>")

def cave():
	list1 = [1, 2, 3,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
	random.shuffle(list1)	
	MapCave.append((list1[0], list1[ listSize - 1 ]))

	for i in range(listSize -1):
		MapCave.append((list1[i], list1[i + 1]))

	for i in range(int (listSize / 2 )):
		MapCave.append((list1[i], list1[ i + int(listSize / 2)]))

def initPlayerRoom():
	#print(MapCave)
	gameObjects[0] = random.choice(list1) #changed the name to "playerRoom" - we can reuse this
	#append to caving list
	caving.append(gameObjects[0])
	#remove from list1
	list1.remove(gameObjects[0])

def initPits():
	#put 2 pits in 2 rooms randomly
	gameObjects[1] = random.choice(list1)
	list1.remove(gameObjects[1])
	gameObjects[2] = random.choice(list1)
	list1.remove(gameObjects[2])

def initBats():
	#put 2 bats in 2 rooms randomly
	gameObjects[3] = random.choice(list1)
	list1.remove(gameObjects[3])
	gameObjects[4] = random.choice(list1)
	list1.remove(gameObjects[4])

def initWumpus():
	#put a wumpus in a room randomly
	gameObjects[5] = random.choice(list1)

def printWarning():
	for item in MapCave:
		if item[0] == gameObjects[0]:
			if item[1] == gameObjects[1] or item[1] == gameObjects[2]:
				print("I feel a draft!\n")
			elif item[1] == gameObjects[3] or item[1] == gameObjects[4]:
				print("Bats nearby!\n")
			elif item[1] == gameObjects[5]:
				print("I smell a wumpus!\n")
		if item[1] == gameObjects[0]:
			if item[0] == gameObjects[1] or item[0] == gameObjects[2]:
				print("I feel a draft!\n")
			elif item[0] == gameObjects[3] or item[0] == gameObjects[4]:
				print("Bats nearby!\n")
			elif item[0] == gameObjects[5]:
				print("I smell a wumpus!\n")


cookie = http.cookies.SimpleCookie()

cave()                       
initPlayerRoom()
initPits()
initBats()
initWumpus()
cookie['Cave'] = repr(MapCave)
cookie['GameObjects'] = repr(gameObjects)
cookie['Arrows'] = repr(Arrows)
print(cookie)
print('Content-Type: text/html')
print() 
print('<html><body>')
#print(gameObjects[0])
#print(cookie['GameObjects'])
print("<br />")
printGUIMap()
printWarning()
#function.printGameObject()
#function.printCave()
print("""
   <br/>
   <form method="get" action="/cgi-bin/loop.py">
	What would you like to do? (m/s): <input type="text" name="Selection">
		<br/>Enter the room to move to, or list of rooms to shoot to. <input type="text" name = "Rooms"> 
		<input type="submit" value="Go!">
    </form> 
""")
print('</body></html>')
