#!/usr/bin/env python3

import random

MapCave = []
list1 = [1, 2, 3,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
listSize = 20
Arrows = [5]

def cave():
	list1 = [1, 2, 3,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
	random.shuffle(list1)	
	MapCave.append((list1[0], list1[ listSize - 1 ]))

	for i in range(listSize -1):
		MapCave.append((list1[i], list1[i + 1]))

	for i in range(int (listSize / 2 )):
		MapCave.append((list1[i], list1[ i + int(listSize / 2)]))	

#----------------------------------End of the Map--------------------#

#Set up initial room and pick random numbers to put Bats, pits and Wumpus

caving = []

gameObjects = [0] * 6	#keeps track of where everything is using index
						#index 0 = player, 1 & 2 = pits, 3 & 4 = bats, 5 = wumpus

#

#put player in one room randomly

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

def printCave():
	print(MapCave)

def printLoopCave(MapCave):
	print(MapCave)

def printGameObject():
	print(gameObjects)

def printLoopGameObject(gameObjects):
	print(gameObjects)

def initWumpus():
	#put a wumpus in a room randomly
	gameObjects[5] = random.choice(list1)
	
def initCookie(cookie):
	cookie["Cave"] = repr(MapCave)
	cookie["GameObjects"] = repr(gameObjects)

def getPlayerRoom(gameObjects):
	return gameObjects[0]

def isAdjacent(room0, room1):
	for item in MapCave:
		if item[0] == room0 and item[1] == room1:
			return True
		elif item[0] == room1 and item[1] == room0:
			return True
	return False

def fire(gameObjects, room):
	if int(room) == gameObjects[0]:
		print("\n\tYou have shot yourself. Ouch.\n")
		return True
	elif int(room) == gameObjects[5]:
		print("\n\tYou shot the Wumpus!!!\n")
		return True
	else:
		print("\n\tUnfortunatly, you missed the Wumpus.\n")
	return False

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

def printLoopGUIMap(Map, Objects):
	rooms = [-1] * 3
	for item in Map:
		if item[0] == Objects[0]:
			for i in range(0, 3):
				if rooms[i] == -1:
					rooms[i] = item[1]
					break
		if item[1] == Objects[0]:
			for i in range(0, 3):
				if rooms[i] == -1:
					rooms[i] = item[0]
					break
	print("<p>----------->[", rooms[0], "]</p>")
	print("<p>[", Objects[0], "]----->[", rooms[1], "]</p>")
	print("<p>----------->[", rooms[2], "]</p>")

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

def printLoopWarning(MapCave, gameObjects):
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

def checkDeath():
	#check to see if the player has died. We do this by seeing if
	#the player's room is the same as either of the pits, or the 
	#wumpus.
	if gameObjects[0] == gameObjects[1] or gameObjects[0] == gameObjects[2]:
		print("You've fallen into a pit!... Better luck next time.\n")
		return 0
	elif gameObjects[0] == gameObjects[5]:
		print("Oh no! You've been caught by the Wumpus!... Better luck next time.\n")
		return 0
	else:
		return 1


def shoot(MapCave, gameObjects, roomList):
		#This is to check whether or not the shot is valid
		validShot = True
		roomList.insert(0, gameObjects[0])
		while len(roomList) > 1:
			if isAdjacent(roomList[0], roomList[1]):
				roomList.pop(0)
			else:
				validShot = False
				break

		gameOver = False
		if validShot:
			gameOver = fire(gameObjects, roomList[0]);
		else:
			randList = []
			for item in MapCave:
				if item[0] == roomList[0]:
					randList.append(item[1])
				elif item[1] == roomList[0]:
					randList.append(item[0])
			gameOver = fire(gameObjects, random.choice(randList))

		return gameOver

					
		
