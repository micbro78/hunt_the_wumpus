"""Class to create caves and other rooms"""
class Cave:
    """Defines Cave class objects"""
    def __init__(self, cave_name):
        """Defines Cave class attributes"""
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None

    def set_name(self,cave_name):
        """Sets the name of Cave objects"""
        self.name = cave_name

    def get_name(self):
        """Returns the name attribute of a Cave object"""
        return self.name

    def set_description(self, cave_description):
        """Sets the description attributs for Cave objects"""
        self.description = cave_description

    def get_description(self):
        """Returns the description attribute of a Cave object"""
        return self.description

    #def describe(self):
        #"""Test"""
        #print(self.description)

    def link_cave(self, direction, cave_to_link):
        """Manages linking of caves for navigation"""
        self.linked_caves[direction] = cave_to_link
        #print(self.name + " linked caves: " + repr(self.linked_caves))

    def get_details(self):
        """Returns the name of the cave, its description and linked caves"""
        print(self.name)
        print("----------")
        print(self.description)
        for direction, cave in self.linked_caves.items():
            print("The " + cave.get_name() + " is " + direction)

    def move(self, direction):
        """Manages movement between caves"""
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You cannot go that way")
            return self

    def set_character(self, new_character):
        """Manages adding a Character object to a Cave object"""
        self.character = new_character

    def get_character(self):
        """Returns the presence of a Character object in the Cave object"""
        return self.character
