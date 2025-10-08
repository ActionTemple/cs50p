




# version 29/6/25 incorpating regex with compass directions into main game
# 7/7/25 get and drop commands now work
# 7/7/25 objects should be dictionaries. Let's try this
# changed filenames to rooms2.json/edited json file to include dictionaries/edited json for loop loader to include {} - maybe this needs sorting out
# 11/7/25 Let's try and get the UI working

import re
import json
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text

console = Console()
layout = Layout()




class Room:
    def __init__(self, room_id, description, objects, exits):
        self.room_id = room_id
        self.description = description
        self.objects = objects
        self.exits = exits

    def describe(self):
        description =[]
        #description.append(self.description) - final (don't really want the room number)
        description.append(f"Room {self.room_id}: {self.description}") # just for the working
        if self.objects:
            description.append("You see: " + ", ".join(self.objects))
        description.append("Exits: " + ", ".join(self.exits))
        return "\n".join(description)



# if the item in the get string is in self.objects, it needs to be added to an inventory list and deleted from self.objects

    def get(self, item):
        print(self.objects)
        print(item)
        if item in self.objects:
            item_data = self.objects.pop(item)   # remove from room and get item data
            player.inventory[item] = item_data   # add to player inventory
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
                objects=details.get("objects", {}),
                exits=details.get("exits", [])
            )
        return rooms

class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = {}

    def drop(self, item):
        if item in self.inventory:
            item_data = self.inventory.pop(item)
            rooms[player.current_room].objects[item] = item_data
            print(f"You drop the {item}")




rooms = load_rooms_from_json("rooms2.json")
player = Player(24)

def main():

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3)
    )

    layout["header"].update(Panel("The Big House", style="bold white on blue"))
    layout["footer"].update(Panel("Inventory: torch", style="white on black"))

    # This will hold all the "in-game" output
    current_room = rooms[player.current_room]
    user_input = current_room.describe()
    main_text = Text("Welcome!\n", style="white on black")
    main_text.append(f"> {user_input}\n", style="bold green")

    while True:

        console.clear()
        layout["main"].update(Panel(main_text, style="white on black"))
        console.print(layout)
        #current_room = rooms[player.current_room]
        #user_input = current_room.describe()
        commands(input("What's next: ")), player.current_room
        # Append input and placeholder response to main text
        main_text.append(f"> {user_input}\n", style="bold green")
        main_text.append("You typed something...\n", style="white")


def commands(b):

    match = re.search(r'^(go )?(north ?east\b|north ?west\b|south ?east\b|south ?west\b|north\b|south\b|east\b|west\b|ne\b|nw\b|se\b|sw\b|n\b|s\b|e\b|w\b)$', b)
    match1 = re.search(r'^(get|drop|examine)()?(.+)?$', b)



    if match: #some problems in this block
        go, direction = match.groups()

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
