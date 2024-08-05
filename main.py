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

dungeon.get_details()
cavern.get_details()
grotto.get_details()
                       
