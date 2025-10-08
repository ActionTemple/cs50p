


# version 29/6/25 incorpating regex with compass directions into main game
# 7/7/25 get and drop commands now work
# 7/7/25 objects should be dictionaries. Let's try this
# changed filenames to rooms2.json/edited json file to include dictionaries/edited json for loop loader to include {} - maybe this needs sorting out
# spent some time experimenting with UI in file "gameworking3.py" using "Rich" module /// ran into some difficulties and didn't like to way it was faking a terminal by redrawing the screen.
# 17/7/25 skip work on UI and focus on 'examine' function/// examine now works - let's go to Degusto for lunch
# 17/7/25 class/objects "interacts" for things that you manipulate to create a result, e.g. open door with key, kill guard
# 22/7/25 Function to load dictionary from JSON now appears to work
# 22/7/25 Regex group do_with for interaction with items like door


import re
import json
import os
import textwrap

class Room:
    def __init__(self, room_id, description, message, objects, exits):
        self.room_id = room_id
        self.description = description
        self.message = message
        self.objects = objects
        self.exits = exits

    def describe(self):
        description = []
        description.append(f"Room {self.room_id}: {self.description}")

        if self.objects:
            description.append("You see:", ", ".join(self.objects))
        if self.message:
            print(self.message)
        description.append("Exits:", ", ".join(self.exits))

        wrapped_lines = []
        for line in description:
            wrapped_lines.extend(textwrap.wrap(line, width=80))

        return "\n".join(wrapped_lines)

# if the item in the get string is in self.objects, it needs to be added to an inventory list and deleted from self.objects

    def get(self, item):
        print(self.objects)
        print(item)
        if item in self.objects:
            item_data = self.objects.pop(item)   # remove from room and get item data
            player.inventory[item] = item_data   # add to player inventory
        else:
            print(f"There is no {item} here")

    def examine(self, item):
        if item in self.objects:
            print(self.objects[item])
        elif item in player.inventory:
            print(player.inventory[item])

    def search(self):
        #remove items from interact's pockets and put them into room inventory
        ...

# Load rooms from JSON file
def load_rooms_from_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        rooms = {}
        for room_id, details in data.items():
            rooms[int(room_id)] = Room(
                room_id=int(room_id),
                description=details["description"], #mandatory
                message=details.get("message"), #optional
                objects=details.get("objects", {}),
                exits=details.get("exits", [])
            )
        return rooms

class Interacts:
    def __init__(self, interact, location, keyword, item, exits, message_false, message_true, message_action, state):
        self.interact = interact
        self.location = location
        self.keyword = keyword
        self.item = item
        self.exits = exits
        self.message_false = message_false
        self.message_true = message_true
        self.message_action = message_action
        self.state = state



def load_interacts_from_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        interacts = {}
        for interact, details in data.items():
            interacts[interact] = Interacts(
                interact=interact,
                location=details["location"],
                keyword=details["keyword"],
                item=details["item"],
                exits=details.get("exits", []),
                message_false=details["message_false"],
                message_true=details["message_true"],
                message_action=details["message_action"],
                state=details["state"] == "False"
            )
        return interacts


class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = {}

    def drop(self, item):
        if item in self.inventory:
            item_data = self.inventory.pop(item)
            rooms[player.current_room].objects[item] = item_data
            print(f"You drop the {item}")
        else:
            print(f"You don't have {item}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

rooms = load_rooms_from_json("rooms2.json")
interacts = load_interacts_from_json("interacts.json")

clear_screen()
print()
in_put = input("1: Start\n2: Instructions\n" )
print(in_put)
if in_put == "2":
    clear_screen()
    print()
    rooms[998].describe()
else:
    pass

clear_screen()
print()
rooms[999].describe()
player = Player(24)

def main():

    while True:
        current_room = rooms[player.current_room]
        current_room.describe()
        commands(input("What's next: ")), player.current_room


def commands(b):

    compass = re.search(r'^(go )?(north ?east\b|north ?west\b|south ?east\b|south ?west\b|north\b|south\b|east\b|west\b|ne\b|nw\b|se\b|sw\b|n\b|s\b|e\b|w\b)$', b)
    action = re.search(r'^(get|drop|examine)()?(.+)?$', b)
    do_with = re.search(r'^(kill|open)()?(.+)?(with)()?(.+)?$', b)


    if compass: #some problems in this block
        go, direction = compass.groups()

        print ((f"GO {direction}").upper())
        print(direction)

        if direction in ("n", "north"):
            direction = "n"
            print("1")
        elif direction in ("s", "south"):
            direction = "s"
            print("2")
        elif direction in ("e", "east"):
            direction = "e"
        elif direction in ("w", "west"):
            direction = "w"
        elif direction in ("nw", "northwest", "north west"):
            direction = "nw"
        elif direction in ("sw", "southwest", "south west"):
            direction = "sw"
        elif direction in ("ne", "northeast", "north east"):
            direction = "ne"
        else:
            if direction in ("se", "southeast", "south east"):
                direction = "se"
        if direction in rooms[player.current_room].exits: # some problems here
            player.current_room = room_handler(direction, player.current_room)
            print(f"Check updated room number: {player.current_room}")
        else:
            print(rooms[player.current_room].exits)
            print("You can't go that way")

    elif action:
        keyword, space, item = action.groups()
        if keyword == "get":
            rooms[player.current_room].get(item.lstrip())
            print(f"You pick up the {item}")
            print(player.inventory)
        elif keyword == "drop":
            player.drop(item.lstrip())
        elif keyword == "examine":
            rooms[player.current_room].examine(item.lstrip())

    elif do_with:
        keyword, space, interact, space2, using, item = do_with.groups()
        #print (keyword, space, interact, space2, using, item)
        #print(player.inventory[item])
        if (interact.strip() in interacts and keyword == interacts[interact.strip()].keyword and item.strip() == interacts[interact.strip()].item and item.strip() in player.inventory and interacts[interact.strip()].location == player.current_room) and interacts[interact.strip()].state == "False":
            #print("Bonza")
            #print(rooms[player.current_room].exits)
            #update exits list in rooms from interacts
            rooms[player.current_room].exits.extend(interacts[interact.strip()].exits)
            rooms[player.current_room].message = interacts[interact.strip()].message_true
            interacts[interact.strip()].state = "True"
            print(interacts[interact.strip()].message_action)

        else:
            print("You can't do that")

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
