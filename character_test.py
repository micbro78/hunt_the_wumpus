"""docstring"""
from character import Enemy
harry = Enemy("Harry", "A smelly Wumpus")
harry.describe()
harry.set_conversation("Come closer. I cannot see you!")
harry.talk()
harry.set_weakness("vegemite")

print("What will you fight with?")
fight_with = input("> ")
harry.fight(fight_with)
