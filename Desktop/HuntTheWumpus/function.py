import random

#--------------------Generating Map Randomly --------------------#
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

gameObjects = [0] * 6	#keeps track of where everything is using index
						#index 0 = player, 1 & 2 = pits, 3 & 4 = bats, 5 = wumpus

#put player in one room randomly
def initPlayerRoom():
	gameObjects[0] = random.choice(list1) #changed the name to "playerRoom" - we can reuse this
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

def getPlayerRoom():
	return gameObjects[0]

def getWumpusPos():
	return gameObjects[5]	

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
	print("      -->[", rooms[0], "]\n     |\n[", 
		 gameObjects[0], "]----->[", 
		 rooms[1], "]\n     |\n      -->[", 
		 rooms[2], "]\n",
		 sep='')

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

def move():
	choice = (input("\nWhat room would you like to move to? "))
	for item in MapCave:
		#Check if the entered room number is adjacent or not
		if item[0] == gameObjects[0] and item[1] == int(choice):
				gameObjects[0] = int(choice)

				#if you got in a room with a bat
				if gameObjects[0] == gameObjects[3] or gameObjects[0] == gameObjects[4]:
					print("\nOops, you moved in a room with a bat and it grabed you and took you to some other room at random.")
					currentPos = gameObjects[0]
					while currentPos == gameObjects[0]:
						gameObjects[0] = random.choice(list1)
				
				else:
					print("\nMoved to room ", getPlayerRoom(), '\n', sep=' ')
					return None

		#Check if the entered room number is adjacent or not
		elif item[1] == gameObjects[0] and item[0] == int(choice):
				gameObjects[0] = int(choice)

				#if you got in a room with a bat
				if gameObjects[0] == gameObjects[3] or gameObjects[0] == gameObjects[4]:
					print("\nOops, you moved in a room with a bat and it grabed you and took you to some other room at random.")
					currentPos = gameObjects[0]
					while currentPos == gameObjects[0]:
						gameObjects[0] = random.choice(list1)

				else:
					print("\nMoved to room ", getPlayerRoom(), '\n', sep=' ')
					return None

	#At this point if the function has not returned yet, you have made an invalid
	#move. Now you will be placed in a random number
	print("\nThat is not a room adjacent to you. Moving to a random room...")
	currentPos = gameObjects[0]
	while currentPos == gameObjects[0]:
		gameObjects[0] = random.choice(list1)
	print("\nMoved to room ", getPlayerRoom(), '\n', sep=' ')

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
	elif Arrows[0] == 0:
		Arrows[0] = 5
		print("It looks like you have ran out of arrows!... Better luck next time.\n")
		return 0
	else:
		return 1

def fire(room):
	Arrows[0] -= 1
	if int(room) == gameObjects[5]:
		print("\n\tYou shot the Wumpus!!!\n")
		return True
	else:
		gameObjects[5] = room
		print("\nUnfortunatly, you missed the Wumpus.\n")
		print("Your remaining arrows are now: ", Arrows, "\n")
		print("Hazard! Wumpus is in one of the adjacent room now!\n")

	return False

def shoot():
	roomList = []
	check_validity = True
	#Check validity, if the input is not an integer
	while check_validity:
		try:
			NOfRooms = int(input("Number of rooms (1-5)? "))
			check_validity = False	

		except ValueError:
				print("\nOops, invalid input, try again. \n")
	
	#Check the validity,if the input is not in range		
	if NOfRooms not in range (1, 6):	
		print("\nOops, invalid input, try again.\n")
	
	else:
		print("Room number (1-20)? ")
		enterRoomNo = True

		#store everything in the roomList
		while enterRoomNo:
			invalidity = False
			for room in range (0, NOfRooms):
				roomList.append(input("Room No? "))
		
			#Check whether the item is not a digit or out of range
			for item in roomList:
				if item. isdigit() == False or int(item) > 20 or int(item) < 1:
					invalidity = True
	
			if invalidity == True:
				print("\ninvalid input, try again! \n")
			else:	
				enterRoomNo = False
				roomList = [int(i) for i in roomList]
#-----------------------------End of Checking the Validity of the input------------------------------------

		#This is to check whether or not the shot is valid
		validShot = True
		roomList.insert(0, gameObjects[5])
		
		#check if the shot is valid
		for item in MapCave:
			if(len(roomList) != 1):
				if roomList[0] == item[0] and roomList[1] == item[1]:
						roomList.pop(0)			
				elif roomList[0] == item[1] and roomList[1] == item[0]:
						roomList.pop(0)

		#check if the shot is not valid
		if(len(roomList) > 1):
			validShot = False


		gameOver = False
		#if the shot is valid, fire to the correct room
		if validShot:
			gameOver = fire(roomList[0])
		else:
			# if the shot is not valid, wumpus will move to one of the adjacent room
			adjacentList = []
			for item in MapCave:
				if item[0] == gameObjects[0]:
					adjacentList.append(item[1])
				elif item[1] == gameObjects[0]:
					adjacentList.append(item[0])
			
			gameOver = fire(random.choice(adjacentList))

		#return game over = true if you shot the wumpus
		return gameOver

					
		
