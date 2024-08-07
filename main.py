from cave import Cave

cavern = Cave("Cavern")
grotto = Cave("Grotto")
dungeon = Cave("Dungeon")

cavern.set_description("A damp and dirty cave.")
grotto.set_description("A small cave with ancient markings.")
dungeon.set_description("A large cave with a rack.")

cavern.link_cave("south", dungeon)
dungeon.link_cave("north", cavern)
dungeon.link_cave("west", grotto)
grotto.link_cave("east", dungeon)

current_cave = cavern
while True:
    print("\n")
    current_cave.get_details()
    command = input("> ")
    current_cave = current_cave.move(command)
    