class Street:
    """
    class Street
    """
    def __init__(self, name):
        """
        reveal objects
        """
        self.name = name
        self.description = None
        self.turning = {}
        self.character = None
        self.item = None

    def set_name(self, name):
        """
        set name
        """
        self.name = name

    def get_name(self):
        """
        get name
        """
        return self.name

    def set_description(self, description):
        """
        set description
        """
        self.description = description

    def get_description(self):
        """
        get description
        """
        return self.description

    def get_turn(self, next_street, direction):
        """
        turn
        """
        self.turning[direction] = next_street

    def move(self, direction):
        """
        make a move
        """
        if direction in self.turning:
            return self.turning[direction]
        else:
            print("Ти не можеш піти туди, адже тоді ти не дойдеш до парку, де ти будеш чілити на гамачку")
            return self

    def get_details(self):
        """
        reveal details
        """
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction, street in self.turning.items():
            print(f"Вулиця {street.get_name()} у напрямку {direction}")
        return None

    def get_character(self):
        """
        get character
        """
        return self.character

    def set_character(self, character):
        """
        set character
        """
        self.character = character

    def get_item(self):
        """
        get item
        """
        return self.item

    def set_item(self, item):
        """
        set item
        """
        self.item = item

class Character:
    """
    class Character
    """
    def __init__(self, name, description, phrase, conversation, weakness):
        """
        reveal objects
        """
        self.name = name
        self.description = description
        self.phrase = phrase
        self.conversation = conversation
        self.weakness = weakness

    def describe(self):
        """
        reveal who you have met
        """
        print(f"Ого, оце удача! Ти зустрів/ла [{self.name}]")
        return None

    def description_(self):
        """
        describe who you have met
        """
        print(self.description)

    def base_phrase(self):
        """
        reveal base phrase of a person who you have met
        """
        print(self.phrase)

    def set_conversation(self, conversation):
        """
        make a corversation
        """
        self.conversation = conversation

    def set_weakness(self, weakness):
        """
        set weakness of a person that you have met
        """
        self.weakness = weakness

    def talk(self):
        """
        start a talk with your person
        """
        if self.conversation is not None:
            print(f"[{self.name} каже]: {self.conversation}")
        else:
            print(f"{self.name} не хоче говорити з тобою")

    def try_yourself(self, item):
        """
        get your item from a weakness of your enemy
        """
        return item == self.weakness


class Friend(Character):
    """
    class Friend
    """
    def __init__(self, name, description, phrase, conversation, weakness):
        """
        reveal objects
        """
        super().__init__(name, description, phrase, conversation, weakness)

    def get_conversation(self):
        """
        get a conversation
        """
        return self.conversation


class Enemy(Character):
    """
    class Enemy
    """
    def __init__(self, name, description, phrase, conversation, weakness):
        """
        reveal objects
        """
        super().__init__(name, description, phrase, conversation, weakness)
        self.opportunities = 0

    def set_weakness(self, weakness):
        """
        set a weakness
        """
        self.weakness = weakness

    def get_weakness(self):
        """
        get a weakness
        """
        return self.weakness

    def get_opportunities(self):
        """
        reveal your opportunities
        """
        return self.opportunities

    def try_yourself(self, item: str):
        """
        reveal consiquences of your fight
        """
        if item == self.weakness:
            self.opportunities += 1
            if self.opportunities == 5:
                return True
            else:
                return False
        else:
            print(f"{self.name} crushes you, puny adventurer")
            return True

class Item:
    """
    class Item
    """
    def __init__(self, name):
        """
        reveal objects
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        set a description of your weapon
        """
        self.description = description

    def get_description(self):
        """
        get a description of your weapon
        """
        return self.description

    def set_name(self, name):
        """
        set a name of your weapon
        """
        self.name = name

    def get_name(self):
        """
        get a name of your weapon
        """
        return self.name

    def describe(self):
        """
        reveal description of your weapon
        """
        print(f"[{self.name}] знаходиться тут - {self.description}")