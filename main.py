"""Hunt the Wumpus main program"""
from cave import Cave
from character import Enemy

cavern = Cave("Cavern")
grotto = Cave("Grotto")
dungeon = Cave("Dungeon")
dark_cave_1 = Cave("Dark cave 1")
dark_cave_2 = Cave("Dark cave 2")
dark_cave_3 = Cave("Dark cave 3")
kitchen = Cave("Kitchen")
corridor = Cave("Corridor")
throne_room = Cave("Throne room")
storeroom = Cave("Storeroom")
courtyard = Cave("Courtyard")
armoury = Cave("Armoury")
underground_passage = Cave("Underground passage")

cavern.set_description("A damp and dirty cave.")
grotto.set_description("A small cave with ancient markings.")
dungeon.set_description("A large cave with a rack.")
dark_cave_1.set_description("A pitch-black.")
dark_cave_2.set_description("A pitch-black.")
dark_cave_3.set_description("A pitch-black.")
kitchen.set_description("An old, run-down kitchen that has been ransacked.")
corridor.set_description("A long, bright corridor that has been undisturbed for a long time.")
throne_room.set_description("A grand throne room that has seen better days.")
storeroom.set_description("A small, dusty storeroom that has been ransacked.")
courtyard.set_description("An open courtyard with high walls, cracked tiles and many weeds.")
armoury.set_description("A small, dusty armoury with an old wooden chest.")
underground_passage.set_description("A cramped underground passage. Your way out to freedom!")

cavern.link_cave("south", dungeon)
grotto.link_cave("east", dungeon)
dungeon.link_cave("north", cavern)
dungeon.link_cave("east", dark_cave_1)
dungeon.link_cave("west", grotto)
dark_cave_1.link_cave("east", dark_cave_2)
dark_cave_1.link_cave("south", dark_cave_3)
dark_cave_1.link_cave("west", dungeon)
dark_cave_2.link_cave("west", dark_cave_1)
dark_cave_3.link_cave("north", dark_cave_1)
dark_cave_3.link_cave("south", throne_room)
kitchen.link_cave("east", corridor)
kitchen.link_cave("south", courtyard)
corridor.link_cave("east", throne_room)
corridor.link_cave("west", kitchen)
throne_room.link_cave("north", dark_cave_3)
throne_room.link_cave("east", storeroom)
throne_room.link_cave("west", corridor)
storeroom.link_cave("south", armoury)
storeroom.link_cave("west", throne_room)
courtyard.link_cave("north", kitchen)
courtyard.link_cave("south", underground_passage)
armoury.link_cave("north", storeroom)
underground_passage.link_cave("north", courtyard)

harry = Enemy("Harry", "A smelly wumpus")
harry.set_conversation("Come closer. I can't see you!")
harry.set_weakness("vegemite")
underground_passage.set_character(harry)

current_cave = cavern
DEAD = False
while DEAD is False:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.character
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            fight_with = input("What do you want to fight with? ")
            if inhabitant.fight(fight_with) is True:
                print("Bravo. You won the fight hero!")
            else:
                print("Scurry home. You lost the fight")
                current_cave.set_character(None)
                print ("That's the end of the game")
                DEAD = True
        else:
            print("There is no one here to fight")
    else:
        print("Invalid input. Try again")
