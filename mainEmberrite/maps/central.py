#python

import rooms
import items
import people
import npcs
import weapons
import armors

centralRooms=[
	#(location, adjacent rooms[n,s,e,w], description, dark, inventory, containers, monsters, bed, people, secret passageways[n,s,e,w])
    rooms.room(0, [3,1,-1,-1], "\nYou are in a small cellar.\nThere is a stairwell to the north.\nThere is a small crack in the wall to the south that you may be able to fit through.", True, [], {}, [], False, [], [False, False, False, False]),

	rooms.room(1, [0,2,-1,-1], "\nYou are in a small winding rocky corridor.\nThere is a small opening to the north.\nThe corridor continues south.", True, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(2, [1,-1,-1,-1], "\nYou are in a small cave.\nThere is a waterfall filling a pool of water to the south.\nThere is a small crack in the wall to the north that you may be able to fit through.", True, [items.item("gem")], {}, [npcs.npc("bugbear",10,2,4)], False, [], [False, False, False, False]),
	
	rooms.room(3, [5,0,4,6], "\nYou are in a small kitchen.\nThere is a table with three chairs in front of you.\nIn the northwest corner of the room there is an oven.\nIn the northeast corner there is a cupboard.\nThere are doors to the north, east, and west.\nTo the south is a staricase descending down.", False, [], {"cupboard":[False,items.item("garlic"),items.item("salt"),items.healthPotion()]}, [], False, [], [False, False, False, False]),
	
	rooms.room(4, [7,-1,10,3], "\nYou are in the backyard of an old log house.\nThere is an old battered door on the side of the house to your west.\nThere are paths into the woods to the east and north.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(5, [-1,3,-1,8], "\nYou are in a rectangular room.\nThere is a long table that appears to have hosted many meals in the center of the room.\nThere is cake on the table.\nOutside of the table and doors to the south and west there is not much here.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(6, [8,-1,3,9], "\nYou are in a small cozy room.\nThere is a fireplace that does not appear to have been used in quite some time.\nThere are two lounge charis in the center of the room.\nThere are doors to the north, east, and west.\nThe west wall has two boarded up windows on either side of the door.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(7, [-1,-1,4,9], "\nYou are on a wooded pathway.\nThe path continues to the east and west.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(8, [-1,6,5,-1], "\nYou are in a tiny room.\nThere is a disheveled bed in the corner of the room.\nThere are doors to the south and east.", False, [], {}, [], True, [], [False, False, False, False]),
	
	rooms.room(9, [7,12,6,-1], "\nYou are on the porch of an old wooden house.\nThe house has a door to the east.\nOn either side of the door are boarded up windows.\nThere is a mail box infront of the door.\nThere is a garden path to the north and a road leading south.", False, [], {"mailbox":[False,items.item("letter")]}, [], True, [], [False, False, False, False]),

	rooms.room(10, [15,-1,11,4], "\nYou are in the middle of a forest.", False, [], {}, [], False, [], [True, False, False, False]),

	rooms.room(11, [-1,-1,14,10], "\nYou are in a clearing in the woods.\nThere are paths leading east and west.\nThere is a unicorn in the middle of the clearing watching you carefully.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(12, [9,13,-1,-1], "\nYou are on a road.\nIt goes north and south.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(13, [12,18,17,16], "\nYou are in small bustling town.\nPeople are hurrying around you on their days errands.\nThe Goldshire Inn is to the west.\nThere is a blacksmith to the east.\nThere are roads out of town to the north and south.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(14, [20,19,-1,11], "\nYou are in a seemingly endless forest.\nThe smell of death is prevelant in the air.\nThe undergrowth seems to creep up on you everytime you look away.", True, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(15, [23,10,-1,-1], "\nYou are in an overgrown abandoned cave.\nThere is a small opening to the north.\nThere is light to the south.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(16, [-1,-1,13,-1], "\nYou are in a well lit inn.\nThere are jovial people singing and dancing around you.\nThe barmaid is walking around looking for someone to talk to.\nThe entrance to the inn from the town is to the east.", False, [], {}, [], False, [npcs.barmaid("barmaid", 2, 1, 1, {"room":20,"beer":5,"ale":5,"drink":5})], [False, False, False, False]),
	
	rooms.room(17, [-1,-1,-1,13], "\nYou are in a blacksmith's shop.\nThe blacksmith is working at the forge.", False, [], {}, [], False, [npcs.vendor("blacksmith", 5, 2, 2, {weapons.weapon("long sword",8,5,0,2):50,armors.armor("plate-mail",-2,"Whole Body"):120})], [False, False, False, False]),
	
	rooms.room(18, [13,29,-1,-1], "\nYou are on an old decaying pathway that leads north and south.\nVines sprawl across the path making it hard to walk.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(19, [14,-1,-1,-1], "\nYou are in a roomy cave.\nWater drips from the rocks overhead.\nThe smell of rotting corpses is prevelant.\nThere are skeletons in the corner of the room.", True, [], {}, [npcs.npc("bear",25,4,10)], False, [], [False, False, False, False]),
	
	rooms.room(20, [-1,14,-1,21], "\nYou are on a small path in the middle of a horrid forest.\nThe path seems to wind endlessly to the west and to the south.", True, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(21, [-1,-1,20,22], "\nYou are at the top of a giant ravene.\nThere is a waterfall gushing down from the otherside of the chasm.\nThe path continues west and east.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(22, [-1,-1,21,25], "\nYou are on the shore of a giant lake.\nTo your east there is a path leading into a forest.\nTo your west there is a run down old hut.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(23, [24,15,-1,-1], "\nYou are in a small dank passageway that leads north and south.", True, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(24, [27,23,28,-1], "\nYou are at the base of a giant waterfall in a ravene.\nThe shore runs to the east and to the south.", False, [], {}, [], False, [], [True, False, False, False]),
	
	rooms.room(25, [-1,-1,22,26], "\nYou are in a small dark hut.\nThere is a door to the east.", False, [], {}, [npcs.npc("witch",25,1,12)], False, [], [False, False, False, True]),
	
	rooms.room(26, [-1,-1,25,-1], "\nYou are in a roomy cave.\nWater drips from the rocks overhead.\nThere is a trap door leading up.", True, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(27, [-1,24,-1,-1], "\nYou are in a small wet cave.\nThe sound of rushing water can be heard to the south.", True, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(28, [-1,-1,-1,24], "\nYou are on the shore of a beach.\nThe sand is wet and cold.\nThere is a path leading into a forest to your west.", False, [], {}, [], False, [], [False, False, False, False]),
	
	rooms.room(29, [18,-1,30,-1], "\nYou are in a smelly decaying marsh.\nThere are pathes to the north and to the east.", False, [], {}, [npcs.npc("water elemental",40,1,12)], False, [], [False, False, False, False]),
	
	rooms.room(30, [31,33,32,29], "\nYou are on a mountain path.\nThere is a cave to the north.\nThe path runs east and west.", False, [], {}, [], False, [], [False, True, False, False]),
	
	rooms.room(31, [-1,30,-1,-1], "\nYou are in a roomy cave.\nWater drips from the rocks overhead.\nThe smell of rotting corpses is prevelant.\nThere are skeletons in the corner of the room.", True, [], {}, [npcs.npc("mountain lion",20,2,8)], False, [], [False, False, False, False]),
	
	rooms.room(32, [-1,-1,-1,30], "\nYou are in a graveyard.\nThere is a path leading west.\nTo the east is a giant castle looming over the small graveyard.", False, [], {}, [npcs.npc("skeleton",10,1,5)], False, [], [False, False, False, False]),
	
	rooms.room(33, [30,-1,-1,-1], "\nYou are in a roomy cave.\nWater drips from the rocks overhead.\nThe smell of rotting corpses is prevelant.\nThere are skeletons in the corner of the room.", True, [], {}, [npcs.npc("troll",50,3,10)], False, [], [False, False, False, False]),
	
]