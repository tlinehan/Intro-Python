# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        # super().__init__
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        
    def getRoomDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "e":
            return self.e_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
        else:
            return None
    def __str__(self):
        return f"{self.name}"
    def __repr__(self):
        return f"{self.name}"
    def addItem(self, currentItem):
        self.items.append(currentItem)
    def removeItem(self, currentItem):
        self.items.remove(currentItem)
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
