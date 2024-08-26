"""Character class for Hunt the Wumpus game"""
class Character():
    """Defines the Character class"""
    def __init__(self, char_name, char_description):
        """Defines the Character class attributes"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Outputs description of the character"""
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """what the character says when talked to"""
        self.conversation = conversation

    def talk(self):
        """Manages talking to characters"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self):
        """Manages fighting with characters"""
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    """Defines the Enemy subclass of the Character class"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        """Sets the weakness item of an Enemy Character object"""
        self.weakness = item_weakness

    def get_weakness(self):
        """Returns the weakness of an Enemy Character object"""
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " swallows you, little wimp!")
            return False
