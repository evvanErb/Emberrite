#!/usr/bin/python

import rooms
import items
import people
import npcs
import weapons
import armors

castleRooms=[
	#(location, adjacent rooms[n,s,e,w], description, dark, inventory, containers, monsters, bed, people, secret passageways[n,s,e,w])
	rooms.room(34, [36,37,35,32], "\n34", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(35, [47,48,-1,34], "\n35", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(36, [-1,-1,38,34], "\n36", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(37, [-1,39,38,34], "\n37", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(38, [36,37,40,-1], "\n38", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(39, [37,41,42,-1], "\n39", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(40, [-1,-1,43,38], "\n40", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(41, [39,-1,-1,-1], "\n41", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(42, [-1,44,-1,39], "\n42", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(43, [-1,-1,46,40], "\n43", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(44, [42,-1,45,-1], "\n44", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(45, [-1,49,-1,44], "\n45", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(46, [-1,-1,-1,43], "\n46", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(47, [-1,35,-1,-1], "\n47", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(48, [35,-1,-1,-1], "\n48", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(49, [45,50,-1,-1], "\n49", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(50, [-1,51,-1,49], "\n50", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(51, [50,-1,-1,-1], "\n51", False, [], {}, [], False, [], [False, False, False, False]),

]