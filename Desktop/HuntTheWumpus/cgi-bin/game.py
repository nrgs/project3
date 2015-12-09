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

cookie = http.cookies.SimpleCookie()

function.cave()                       
function.initPlayerRoom()
function.initPits()
function.initBats()
function.initWumpus()
function.initCookie(cookie)

print('Content-Type: text/html')
print() 
print('<html><body>')
#print(cookie)
function.printGUIMap()
function.printWarning()
#function.printCave()
#function.printGameObject()
print(cookie)
print("""
   <br/>
   <form method="get" action="/cgi-bin/loop.py">
	What would you like to do? (m/s): <input type="text" name="Selection">
		<br/>Enter the room to move to, or list of rooms to shoot to. <input type="text" name = "Rooms"> 
		<input type="submit" value="Go!">
    </form> 
""")
print('</body></html>')
