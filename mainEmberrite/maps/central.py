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
	
	rooms.room(4, [7,-1,10,3], "\nYou are in the backyard of an old log house.\nThere is an old battered door on the side of the house to your west.\nThere are paths into the woods to the east and north.", False, [], {}, [], False, []),
	
	rooms.room(5, [-1,3,-1,8], "\nYou are in a rectangular room.\nThere is a long table that appears to have hosted many meals in the center of the room.\nThere is cake on the table.\nOutside of the table and doors to the south and west there is not much here.", False, [], {}, [], False, []),
	
	rooms.room(6, [8,-1,3,9], "\nYou are in a small cozy room.\nThere is a fireplace that does not appear to have been used in quite some time.\nThere are two lounge charis in the center of the room.\nThere are doors to the north, east, and west.\nThe west wall has two boarded up windows on either side of the door.", False, [], {}, [], False, []),
	
	rooms.room(7, [-1,-1,4,9], "\nYou are on a wooded pathway.\nThe path continues to the east and west.", False, [], {}, [], False, []),
	
	rooms.room(8, [-1,6,5,-1], "\nYou are in a tiny room.\nThere is a disheveled bed in the corner of the room.\nThere are doors to the south and east.", False, [], {}, [], True, []),
	
	rooms.room(9, [7,12,6,-1], "\nYou are on the porch of an old wooden house.\nThe house has a door to the east.\nOn either side of the door are boarded up windows.\nThere is a mail box infront of the door.\nThere is a garden path to the north and a road leading south.", False, [], {"mailbox":[False,items.item("letter")]}, [], True, []),
]