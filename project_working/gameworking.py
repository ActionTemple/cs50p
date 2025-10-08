

# version 29/6/25 incorpating regex with compass directions into main game
# 7/7/25 get and drop commands now work
import re
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
        print(self.objects)
        print(item)
        if item in self.objects:
            self.objects.remove(item)
            player.inventory.append(item)
        else:
            print(f"There is no {item} here")

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

    def drop(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            rooms[player.current_room].objects.append(item)
            #print(rooms[player.current_room])









rooms = load_rooms_from_json("rooms.json")
player = Player(24)

def main():

    #room = 24


    while True:

        #print(player.current_room)

        current_room = rooms[player.current_room]
        current_room.describe()
        command = commands(input("What's next: ")), player.current_room
        #print (command)
        #print(f"You are in room {player.current_room}")

def commands(b):

    match = re.search(r'^(go )?(north ?east\b|north ?west\b|south ?east\b|south ?west\b|north\b|south\b|east\b|west\b|ne\b|nw\b|se\b|sw\b|n\b|s\b|e\b|w\b)$', b)
    match1 = re.search(r'^(get|drop|examine)()?(.+)?$', b)



    if match:
        go, direction = match.groups()
        print (go)
        print (direction)
        player.current_room = room_handler(direction, player.current_room)

    elif match1:
        keyword, space, item = match1.groups()
        if keyword == "get":
            rooms[player.current_room].get(item.lstrip())
            print(f"You pick up the {item}")
            print(player.inventory)
        elif keyword == "drop":
            player.drop(item.lstrip())

    else:
        print("I don't understand")

def room_handler(a, room):

    if a == "n":
        room += 10
        return room
    elif a == "ne":
        room += 11
        return room
    elif a == "e":
        room += 1
        return room
    elif a == "se":
        room -= 9
        return room
    elif a == "s":
        room -= 10
        return room
    elif a == "sw":
        room -= 11
        return room
    elif a == "w":
        room -= 1
        return room
    else:
        if a == "nw":
            room += 9
            return room

if __name__ == "__main__":
    main()

