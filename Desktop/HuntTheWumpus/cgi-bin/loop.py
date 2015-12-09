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
import os

def move(room):
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	#the move function
	for item in MapCave:
		#Find where the current position of the player is by scanning through
		#each item in MapCave, and checking item[0] and item[1] indexes. Once
		#it finds a link to the players current room, it checks to see if the
		#other index in the MapCave is equal to the choice. If it is, you have
		#made a successful move. If not, it keeps scanning.
		if int(item[0]) == gameObjects[0]:
			print(item[1], " ", room, "\n")
			if int(item[1]) == int(room):
				gameObjects[0] = int(room)

				#if you got in a room with a bat
				if gameObjects[0] == gameObjects[3] or gameObjects[0] == gameObjects[4]:
					print("\nOops, you moved in a room with a bat and it grabed you and took you to some other room at random.")
					currentPos = gameObjects[0]
					while currentPos == gameObjects[0]:
						gameObjects[0] = random.choice(list1)
				

				print("\nMoved to room ", gameObjects[0], '\n', sep=' ')
				return None

		elif int(item[1]) == gameObjects[0]:
			if int(item[0]) == int(room):
				gameObjects[0] = int(room)

				#if you got in a room with a bat
				if gameObjects[0] == gameObjects[3] or gameObjects[0] == gameObjects[4]:
					print("\nOops, you moved in a room with a bat and it grabed you and took you to some other room at random.")
					currentPos = gameObjects[0]
					while currentPos == gameObjects[0]:
						gameObjects[0] = random.choice(list1)

				print("\nMoved to room ", gameObjects[0], '\n', sep=' ')
				return None

	#At this point if the function has not returned yet, you have made an invalid
	#move. Now you will be placed in the first random room that is connected
	#to the player's room.
	print("\nThat is not a room adjacent to you. Moving to a random room...")
	currentPos = gameObjects[0]
	while currentPos == gameObjects[0]:
		gameObjects[0] = random.choice(list1)
	print("\nMoved to room ", gameObjects[0], '\n', sep=' ')

cookie_string = os.environ.get('HTTP_COOKIE')
form = cgi.FieldStorage()
gameObjects = []
MapCave = []
selection = form.getvalue('Selection')

if cookie_string == '':
    output = "I don't see a cookie."
else:
    cookie = http.cookies.SimpleCookie()
    cookie.load(cookie_string)
    MapCave = eval(cookie['Cave'].value)
    gameObjects = eval(cookie['GameObjects'].value)
    gameObjects = [int(i) for i in gameObjects]

print('Content-Type: text/html')
print()
print('<html><body>')

if (selection == "m"):
	room = int(form.getvalue('Rooms'))
	print("room:", room)
	print()
	move(room)
if (selection == "s"):
	roomList = []
	roomNumbers = form.getvalue('Rooms')
	for item in roomNumbers.split():
		roomList.append(int(item))
		function.shoot(MapCave, gameObjects, roomList)

function.printLoopGUIMap(MapCave, gameObjects)
function.printLoopWarning(MapCave, gameObjects)
cookie["Cave"] = repr(MapCave)
cookie["GameObjects"] = repr(gameObjects)
print(gameObjects)

print("""
   <br/>
   <form method="get" action="/cgi-bin/loop.py">
	What would you like to do? (m/s): <input type="text" name="Selection">
		<br/>Enter the room to move to, or list of rooms to shoot to. <input type="text" name = "Rooms"> 
		<input type="submit" value="Go!">
    </form> 
""")
print('</body></html>')
