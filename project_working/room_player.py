
# 1/7/25
# Testing Room and Player classes

import json

class Room:
    def __init__(self, room_id, description, objects, exits):
        self.room_id = room_id
        self.description = description
        self.objects = objects
        self.exits = exits

    def describe(self):
        print(f"Room {self.room_id}: {self.description}")
        if self.objects:
            print("You see:", ", ".join(self.objects))
        print("Exits:", ", ".join(self.exits))

# if the item in the get string is in self.objects, it needs to be added to an inventory list and deleted from self.objects

    def get(self, item):
        if item in self.objects:
            self.objects.remove(item)
            player.inventory.append(item)

# Load rooms from JSON file
def load_rooms_from_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        rooms = {}
        for room_id, details in data.items():
            rooms[int(room_id)] = Room(
                room_id=int(room_id),
                description=details["description"],
                objects=details.get("objects", []),
                exits=details.get("exits", [])
            )
        return rooms

class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = []

    def drop(self):
        ...

    def add_inventory(self):
        ...








rooms = load_rooms_from_json("rooms.json")

player = Player(24)

current_room = rooms[24]
#current_room.describe()
current_room.get("torch")
current_room.describe()
print (player.inventory)

