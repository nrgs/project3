import random

#--------------------Generating Map Randomly --------------------#
#I have created 2 lists as shown below. And each time take a number randomly
#from list1 and list2 and if they are not already existed in the MapCave list will be put them
#in it otherwise the while loop gets repeated once more. And there is no need to be worry about taking repeated
#numbers since each time they are getting removed form list1 and list2 after apending. Also, Each time when the
#while loop is done which takes 10 pairs, list1 and list2 get reloaded. And for loop runs 3 times,
# Meaning having 3 * 10 pairs = 30 pairs.
MapCave = []
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(3):
	j = 1
	while (j <= 10):
		room = random.choice(list1)
		next_room = random.choice(list2)
		if((room, next_room) not in MapCave and (next_room, room) not in MapCave):
			MapCave.append((room, next_room))
			list1.remove(room)
			list2.remove(next_room)
			j +=1

		# else:
		# 	j = j

	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(MapCave)

#----------------------------------End of the Map--------------------#

#Set up initial room and pick random numbers to put Bats, pits and Wumpus
caveNumbers = list1 + list2 #caveNumbers = [1, 2,...., 20]

caving = []

gameObjects = [0] * 6	#keeps track of where everything is using index
						#index 0 = player, 1 & 2 = pits, 3 & 4 = bats, 5 = wumpus

#

#put player in one room randomly
def initPlayerRoom():
	print(MapCave)
	gameObjects[0] = random.choice(caveNumbers) #changed the name to "playerRoom" - we can reuse this
	#append to caving list
	caving.append(gameObjects[0])
	#remove from caveNumbers
	caveNumbers.remove(gameObjects[0])

def initPits():
	#put 2 pits in 2 rooms randomly
	gameObjects[1] = random.choice(caveNumbers)
	caveNumbers.remove(gameObjects[1])
	gameObjects[2] = random.choice(caveNumbers)
	caveNumbers.remove(gameObjects[2])

def initBats():
	#put 2 bats in 2 rooms randomly
	gameObjects[3] = random.choice(caveNumbers)
	caveNumbers.remove(gameObjects[3])
	gameObjects[4] = random.choice(caveNumbers)
	caveNumbers.remove(gameObjects[4])

def initWumpus():
	#put a wumpus in a room randomly
	gameObjects[5] = random.choice(caveNumbers)

def getPlayerRoom():
	return gameObjects[0]

def isAdjacent(room0, room1):
	for item in MapCave:
		if item[0] == room0 and item[1] == room1:
			return True
		elif item[0] == room1 and item[1] == room0:
			return True
	return False

def fire(room):
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
	#the move function
	choice = (input("\nWhat room would you like to move to? "))
	for item in MapCave:
		#Find where the current position of the player is by scanning through
		#each item in MapCave, and checking item[0] and item[1] indexes. Once
		#it finds a link to the players current room, it checks to see if the
		#other index in the MapCave is equal to the choice. If it is, you have
		#made a successful move. If not, it keeps scanning.
		if item[0] == gameObjects[0]:
			if item[1] == int(choice):
				gameObjects[0] = int(choice)

				#if you got in a room with a bat
				if gameObjects[0] == gameObjects[3] or gameObjects[0] == gameObjects[4]:
					print("\nOops, you moved in a room with a bat and it grabed you and took you to some other room at random.")
					currentPos = gameObjects[0]
					while currentPos == gameObjects[0]:
						gameObjects[0] = random.choice(caveNumbers)
				

				print("\nMoved to room ", getPlayerRoom(), '\n', sep=' ')
				return None

		elif item[1] == gameObjects[0]:
			if item[0] == int(choice):
				gameObjects[0] = int(choice)

				#if you got in a room with a bat
				if gameObjects[0] == gameObjects[3] or gameObjects[0] == gameObjects[4]:
					print("\nOops, you moved in a room with a bat and it grabed you and took you to some other room at random.")
					currentPos = gameObjects[0]
					while currentPos == gameObjects[0]:
						gameObjects[0] = random.choice(caveNumbers)

				print("\nMoved to room ", getPlayerRoom(), '\n', sep=' ')
				return None

	#At this point if the function has not returned yet, you have made an invalid
	#move. Now you will be placed in the first random room that is connected
	#to the player's room.
	print("\nThat is not a room adjacent to you. Moving to a random room...")
	for item in MapCave:
		if item[0] == gameObjects[0]:
			gameObjects[0] = item[1]
		elif item[1] == gameObjects[0]:
			gameObjects[0] = item[0]
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
	else:
		return 1


def shoot():

	check_validity = True
	#Check validity, if the input is not an integer
	while check_validity:
		try:
			NOfRooms = int(input("Number of rooms (1-5)? "))
			check_validity = False	

		except ValueError:
				print("Oops, invalid input, try again. \n")
	
	#Check the validity,if the input is not in range		
	if NOfRooms not in range (1, 6):	
		print("Oops, invalid input, try again.\n")
	
	else:
		print("Room number (1-20)? ")
		enterRoomNo = True

		while enterRoomNo:
			invalidity = False
			roomList = []
			for room in range (0, NOfRooms):
				roomList.append(input("Room No? "))
		
			#Check whter the item is not a digit or out of range
			for item in roomList:
				if item. isdigit() == False or int(item) > 20 or int(item) < 1:
					invalidity = True
	
			if invalidity == True:
				print("invalid input, try again! \n")
			else:	
				enterRoomNo = False
				roomList = [int(i) for i in roomList]

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
			gameOver = fire(roomList[0]);
		else:
			randList = []
			for item in MapCave:
				if item[0] == roomList[0]:
					randList.append(item[1])
				elif item[1] == roomList[0]:
					randList.append(item[0])
			gameOver = fire(random.choice(randList))

		return gameOver

					
		
