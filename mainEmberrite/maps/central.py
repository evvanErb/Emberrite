#python

import rooms
import items
import people
import npcs

centralRooms=[
   #(location, adjacent rooms[n,s,e,w], description, dark, inventory, containers, monsters, bed, people)
    rooms.room(0, [3,1,-1,-1], "\nYou are in a small cellar.\nThere is a stairwell to the north.\nThere is a small crack in the wall to the south that you may be able to fit through.", True, [], {}, [], False, []),

	rooms.room(1, [0,2,-1,-1], "\nYou are in a small winding rocky corridor.\nThere is a small opening to the north.\nThe corridor continues south.", True, [], {}, [], False, []),
	
	rooms.room(2, [1,-1,-1,-1], "\nYou are in a small cave.\nThere is a waterfall filling a pool of water to the south.\nThere is a small crack in the wall to the north that you may be able to fit through.", True, [items.item("gem")], {}, [npcs.npc("bugbear",10,2,4)], False, []),
	
	rooms.room(3, [5,0,4,6], "\nYou are in a small kitchen.\nThere is a table with three chairs in front of you.\nIn the northwest corner of the room there is an oven.\nIn the northeast corner there is a cupboard.\nThere are doors to the north, east, and west.\nTo the south is a staricase descending down.", False, [], {"cupboard":[False,items.item("garlic"),items.item("salt"),items.healthPotion()]}, [], False, []),
]