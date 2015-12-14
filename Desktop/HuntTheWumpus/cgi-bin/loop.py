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

def printLoopGUIMap():
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

def move(room, output):
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	#the move function
	for item in MapCave:
		#print("Item 0:", item[0], "Item 1:", item[1], "GameObject: ", gameObjects[0])
		#Find where the current position of the player is by scanning through
		#each item in MapCave, and checking item[0] and item[1] indexes. Once
		#it finds a link to the players current room, it checks to see if the
		#other index in the MapCave is equal to the choice. If it is, you have
		#made a successful move. If not, it keeps scanning.
		if int(item[0]) == gameObjects[0]:
			if int(item[1]) == int(room):
				gameObjects[0] = int(room)

				#if you got in a room with a bat
				if gameObjects[0] == gameObjects[3] or gameObjects[0] == gameObjects[4]:
					output += "\nOops, you moved in a room with a bat and it grabed you and took you to some other room at random."
					currentPos = gameObjects[0]
					while currentPos == gameObjects[0]:
						gameObjects[0] = random.choice(list1)
				

				output += "\nMoved to room " + str(gameObjects[0]) + "\n"
				return output

		elif int(item[1]) == gameObjects[0]:
			if int(item[0]) == int(room):
				gameObjects[0] = int(room)

				#if you got in a room with a bat
				if gameObjects[0] == gameObjects[3] or gameObjects[0] == gameObjects[4]:
					output += "\nOops, you moved in a room with a bat and it grabed you and took you to some other room at random."
					currentPos = gameObjects[0]
					while currentPos == gameObjects[0]:
						gameObjects[0] = random.choice(list1)

				output += "\nMoved to room " + str(gameObjects[0]) + "\n"
				return output

	#At this point if the function has not returned yet, you have made an invalid
	#move. Now you will be placed in the first random room that is connected
	#to the player's room.
	output += "\nThat is not a room adjacent to you. Moving to a random room..."
	currentPos = gameObjects[0]
	while currentPos == gameObjects[0]:
		gameObjects[0] = random.choice(list1)
	output += "\nMoved to room " + str(gameObjects[0]) + "\n"
	return output

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

print(cookie)
output = ""
if (selection == "m"):
	room = int(form.getvalue('Rooms'))
	output = move(room, output)
if (selection == "s"):
	roomList = []
	roomNumbers = form.getvalue('Rooms')
	for item in roomNumbers.split():
		roomList.append(int(item))
		function.shoot(MapCave, gameObjects, roomList)

cookie["Cave"] = repr(MapCave)
cookie["GameObjects"] = repr(gameObjects)
print(cookie)
print('Content-Type: text/html')
print()
print('<html><body>')
print(output)
printLoopGUIMap()
function.printLoopWarning(MapCave, gameObjects)
print("""
   <br/>
   <form method="get" action="/cgi-bin/loop.py">
	What would you like to do? (m/s): <input type="text" name="Selection">
		<br/>Enter the room to move to, or list of rooms to shoot to. <input type="text" name = "Rooms"> 
		<input type="submit" value="Go!">
    </form> 
""")
print('</body></html>')
