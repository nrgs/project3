import random

#--------------------Generating Map Randomly --------------------#
#I have created 2 lists as shown below. And each time take a number randomly
#from list1 and list2 and if they are not already existed in the MapCave list will be put them
#in it otherwise the while loop gets repeated once more. And there is no need to be worry about taking repeated
#numbers since each time they are getting removed form list1 and list2 after apending. Also, Each time when the
#while loop is done which takes 10 pairs, list1 and list2 get reloaded. And for loop runs 3 times,
# Meaning having 3 * 10 pairs = 30 pairs.

MapCave = []
list1 = [1, 2, 3, 4, 5, 6, 7,8, 9,10]
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

		else:
			j = j

	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
	list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(MapCave)
#----------------------------------End of the Map--------------------#



