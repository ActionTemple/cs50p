# version 29/6/25 incorpating regex with compass directions into main game
# 7/7/25 get and drop commands now work
# 7/7/25 objects should be dictionaries. Let's try this
# changed filenames to rooms2.json/edited json file to include dictionaries/edited json for loop loader to include {} - maybe this needs sorting out
# spent some time experimenting with UI in file "gameworking3.py" using "Rich" module /// ran into some difficulties and didn't like to way it was faking a terminal by redrawing the screen.
# 17/7/25 skip work on UI and focus on 'examine' function/// examine now works - let's go to Degusto for lunch
# 17/7/25 class/objects "interacts" for things that you manipulate to create a result, e.g. open door with key, kill guard
# 22/7/25 Function to load dictionary from JSON now appears to work
# 22/7/25 Regex group do_with for interaction with items like door
# 6/8/25 Wrapped text sorted and formatting with "\n"
# 6/8/25 player.move_tracker now works - descriptions no longer being repeated after each action
# 12/8/25 index_interacts_into_room - the loop now works - room number: list of interacts (key:val pair). Need to add this to Room class
# 17/8/25 Got one_word_commands look and help working, although at the moment 'help' is just a repetition of the instructions. Think I can do something better here
# 17/8/25 Fixed turns_in_room so that it resets when the player enters a new room
# 18/8/25 Message attack now works
# 3/9/25 Refactored to include main function for most of the intro code, main_loop for the main part of the game, globals for rooms and interacts, and a working reset function that sets it all back to factory settings and starts the game (arrest/death sequence).

import re
import json
import os
import inflect
import textwrap
p = inflect.engine()


class Room:

    def __init__(self, room_id, description, message, objects, exits, interacts=None):
        self.room_id = room_id
        self.description = description
        self.message = message
        self.objects = objects
        self.exits = exits
        if interacts != None:
            self.interacts = interacts #store interact name in room
        else:
            self.interacts = []

    def describe(self):
        #p = inflect.engine()
        items = []
        description = []
        #description.append(f"Room {self.room_id}: {self.description}")
        description.append(self.description)
        if self.objects:
            for object in self.objects:
                object = p.a(object)
                items.append(object)

            look = f"There is {p.join(items)} here."
            look = str(look)  #.strip("'()")
            description.append(look) #this line altered
        if self.message:
            description.append(self.message)
        if self.exits:
            count = len(self.exits)
            if count == 1:
                exit = f"You see an exit to the {p.join(self.exits)}."
                exit = str(exit)
                description.append(exit)
            else:   #add an elif to give better grammar when up and down are not in self.exits
                exits = f"You see exits {p.join(self.exits)}."
                exits = str(exits)
                description.append(exits)

        full_text = "\n".join(description)
        lines = full_text.split("\n")
        wrapped_lines = []
        for line in lines:
            if line.strip():
                wrapped_lines.extend(textwrap.wrap(line, width=80))
            else:
                wrapped_lines.append('')


        print ("\n".join(wrapped_lines))

# if the item in the get string is in self.objects, it needs to be added to an inventory list and deleted from self.objects

    def get(self, item):
        #print(self.objects)
        #print(item)
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
    def __init__(self, interact, location, keyword, item, exits, message_attack, message_true, message_action, state=False):
        self.interact = interact
        self.location = location
        self.keyword = keyword
        self.item = item
        self.exits = exits
        self.message_attack = message_attack
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
                item=details.get("item"),
                exits=details.get("exits", []),
                message_attack=details.get("message_attack"),
                message_true=details.get("message_true"),
                message_action=details.get("message_action"),
                #state=details.get("state")
                state=False
            )
        return interacts

def index_interacts_into_Room(filename):

    with open(filename, "r") as file:
        data = json.load(file)
        interacts = {}
        for interact, details in data.items():
            location = details["location"]
            if location in interacts:
                interacts[location].append(interact)
            else:
                interacts[location] = [interact]
        print (interacts)
        for location in interacts:
           rooms[location].interacts.append(interacts)



class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = {}
        self.move_history = {}
        self.turns_in_room = 0

    def drop(self, item):
        if item in self.inventory:
            item_data = self.inventory.pop(item)
            rooms[player.current_room].objects[item] = item_data
            print(f"You drop the {item}")
        else:
            print(f"You don't have {item}")

    def move_tracker(self, move_number, room_number):
        self.move_history[move_number] = room_number

rooms = load_rooms_from_json("rooms2.json")
interacts = load_interacts_from_json("interacts.json")
index_interacts_into_Room("interacts.json")
player = Player(250)

def reset():
    global rooms
    global interacts
    player.current_room = 250
    player.inventory = {}
    player.move_history = {}
    player.turns_in_room = 0

    rooms = {}
    rooms = load_rooms_from_json("rooms2.json")

    interacts = {}
    interacts = load_interacts_from_json("interacts.json")

    index_interacts_into_Room("interacts.json")




def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():


    clear_screen()
    print()
    while True:
        clear_screen()
        in_put = input("1: Start\n2: Instructions\n" )
        print(in_put)
        if in_put == "2":

            clear_screen()
            print()
            rooms[998].describe()
            in_put = input("Press space for main menu\n")
            if in_put =="":
                break

        elif in_put =="1":


            clear_screen()
            print()
            rooms[999].describe()
            #player = Player(250)
            break
        else:
            break

    main_loop()

def main_loop():
    # I want to avoid printing the room description twice
    # need to find a way of comparing current room between moves

    rooms[997].describe()

    count = 1
    last_move = 1
    game_on = True
    while game_on == True:


        current_room = rooms[player.current_room]
        #print (f"This move: {count}")
        #print (f"Last move: {last_move}")
        player.move_tracker(count, player.current_room)

        #print (player.move_history[count])
        #print (player.current_room)
        if count == 1:
            current_room.describe()
            print(f"Turns in room:{player.turns_in_room}")

        elif player.move_history[last_move] != player.current_room:
            current_room.describe()
            player.turns_in_room = 0
            print(f"Turns in room: {player.turns_in_room}")
        else:
            player.turns_in_room +=1
            print (f"Turns in room: {player.turns_in_room}")

# This block needs sorting out
        if player.turns_in_room > 0:       # gives a chance for the player to see if there is something dangerous, but not take a second move in the room
            #print(player.current_room)
            #print(rooms[player.current_room].interacts)
            for room in rooms[player.current_room].interacts:
                if player.current_room in room:   #if the current room has an interact in it
                    #print(room[player.current_room])
                    this_room = int(player.current_room)
                    #print (f"This room: {this_room}")
                    int_data = room[player.current_room]
                    #print (f"int_data: {int_data[0]}")
                    interact = int_data[0]
                    #print(int_data[0][349][0]) # hard coded 349 just for a test - variable should be this_room
                    print (interacts[interact].state)
                    if interacts[interact].message_attack:
                        if interacts[interact].state == False:
                            print(interacts[interact.strip()].message_attack)
                            interacts[interact.strip()].state = True
                            game_on = False
                            break
                        # we need a death sequence here which includes a reset
                        # state = True
        if game_on == True:
            commands(input("What's next? ")), player.current_room
            count += 1
            last_move = count -1
        else:
            reset()

            count = 1
            last_move = 1
            rooms[997].describe()
        game_on = True
        continue





def commands(b):

    compass = re.search(r'^(go )?(north ?east\b|north ?west\b|south ?east\b|south ?west\b|north\b|south\b|east\b|west\b|down\b|up\b|ne\b|nw\b|se\b|sw\b|n\b|s\b|e\b|w\b|u\b|d\b)$', b)
    action = re.search(r'^(get|drop|examine)()?(.+)?$', b)
    do_with = re.search(r'^(kill|open)()?(.+)?(with)()?(.+)?$', b)
    one_word_commands = re.search(r'^look|help|inventory|inv$', b)



    if compass: #some problems in this block
        go, direction = compass.groups()

        #print ((f"GO {direction}").upper())
        #print(direction)

        if direction in ("n", "north"):
            direction = "north"
        elif direction in ("s", "south"):
            direction = "south"
        elif direction in ("e", "east"):
            direction = "east"
        elif direction in ("w", "west"):
            direction = "west"
        elif direction in ("nw", "northwest", "north west"):
            direction = "north west"
        elif direction in ("sw", "southwest", "south west"):
            direction = "south west"
        elif direction in ("ne", "northeast", "north east"):
            direction = "north east"
        elif direction in ("se", "southeast", "south east"):
            direction = "south east"
        elif direction in ("up", "u"):
            direction = "up"
        else:
            if direction in ("down", "d"):
                direction = "down"
        if direction in rooms[player.current_room].exits: # some problems here
            player.current_room = room_handler(direction, player.current_room)
            #print(f"Check updated room number: {player.current_room}")
        else:
            #print(rooms[player.current_room].exits)
            print("You can't go that way")

    elif action:
        keyword, space, item = action.groups()
        if keyword == "get":
            rooms[player.current_room].get(item.lstrip())
            print(f"You pick up the {item}")
            #print(player.inventory)
        elif keyword == "drop":
            player.drop(item.lstrip())
        elif keyword == "examine":
            rooms[player.current_room].examine(item.lstrip())

    elif do_with:
        keyword, space, interact, space2, using, item = do_with.groups()
        #print (keyword, space, interact, space2, using, item)
        #print(player.inventory[item])
        if (interact.strip() in interacts and keyword == interacts[interact.strip()].keyword and item.strip() == interacts[interact.strip()].item and item.strip() in player.inventory and interacts[interact.strip()].location == player.current_room):
            #print("Bonza")
            #print(rooms[player.current_room].exits)
            #update exits list in rooms from interacts
            rooms[player.current_room].exits.extend(interacts[interact.strip()].exits)
            rooms[player.current_room].message = interacts[interact.strip()].message_true
            #interacts[interact.strip()].state = "True"
            print(interacts[interact.strip()].message_action)
            interacts[interact.strip()].state = True
        else:
            print("You can't do that")

    elif one_word_commands:
        keyword = one_word_commands.group()

        if keyword == "look":
            rooms[player.current_room].describe()
        elif keyword == "help":
            rooms[998].describe()
        elif keyword == "inv" or keyword == "inventory":
            if player.inventory:
                inv = p.a(p.join(list(player.inventory.keys())))

                #inv = p.a(inv)
                print(f"You are carrying {inv}.")
            else:
                print("You aren't carrying anything.")




    else:
        print("I don't understand")

def room_handler(a, room):

    if a == "north":
        room += 100
        return room
    elif a == "north east":
        room += 101
        return room
    elif a == "east":
        room += 1
        return room
    elif a == "south east":
        room -= 99
        return room
    elif a == "south":
        room -= 100
        return room
    elif a == "south west":
        room -= 101
        return room
    elif a == "west":
        room -= 1
        return room
    elif a == "north west":
        room += 99
        return room
    elif a == "up":
        room += 1000
        return room
    else:
        if a == "down":
            room -= 1000
            return room

if __name__ == "__main__":
    main()
