"""
module
"""
class Room:
    """
    class Room
    """
    def __init__(self, name):
        """
        this func get objects
        """
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_name(self, name):
        """
        this func sets a name
        """
        self.name = name

    def get_name(self):
        """
        this func gets a name
        """
        return self.name

    def set_description(self, description):
        """
        this func sets description
        """
        self.description = description

    def get_description(self):
        """
        this func gets description
        """
        return self.description

    def link_room(self, next_room, direction):
        """
        this func links a room
        """
        self.linked_rooms[direction] = next_room

    def move(self, direction):
        """
        this func makes a move
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def get_details(self):
        """
        this func gets details
        """
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print(f"The {room.get_name()} is {direction}")
        return None

    def get_character(self):
        """
        this func gets a character
        """
        return self.character

    def set_character(self, character):
        """
        this func sets a characyer
        """
        self.character = character

    def get_item(self):
        """
        this func gets item
        """
        return self.item

    def set_item(self, item):
        """
        this func sets item
        """
        self.item = item


class Enemy:
    """
    class Enemy
    """
    def __init__(self, name, description, defeated =[]):
        """
        this func get objects
        """
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None
        self.defeated = defeated

    def set_conversation(self, conversation):
        """
        this func sets conversation
        """
        self.conversation = conversation

    def set_weakness(self, weakness):
        """
        this func sets a weakness
        """
        self.weakness = weakness

    def get_weakness(self):
        """
        this func gets the weakness
        """
        return self.weakness

    def get_name(self):
        """
        this func gets the name
        """
        return self.weakness

    def describe(self):
        """
        this func describes
        """
        print(f"[{self.name}] is here!")
        print(self.description)

    def talk(self):
        """
        this func reveals talk
        """
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")

    def fight(self, item):
        """
        this func fights
        """
        if item == self.weakness:
            print(f"You fend {self.name} off with the {item}")
            self.defeated.append(1)
            return True
        return False

    def get_defeated(self):
        """
        this func defeat
        """
        return len(self.defeated)

class Item:
    """
    class Item
    """
    def __init__(self, name):
        """
        this func get objects
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        this func sets description
        """
        self.description = description

    def get_description(self):
        """
        this func gets description
        """
        return self.description

    def set_name(self, name):
        """
        this func sets a name
        """
        self.name = name

    def get_name(self):
        """
        this func gets a name
        """
        return self.name

    def describe(self):
        """
        this func describes
        """
        print(f"The [{self.name}] is here - {self.description}")