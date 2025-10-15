#The Big House
#Andrew Waddington

import re
import json
import os
import inflect
import textwrap
from getch import getch
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


        if self.message:
            description.append(self.message)
        if self.objects:
            for object in self.objects:
                object = p.a(object)
                items.append(object)

            look = f"There is {p.join(items)} here."
            look = str(look)
            description.append(look) #this line altered
        if (player.maze == True and "torch" not in player.inventory):
            description.append("It is pitch black. You cannot see.")

        elif self.exits:
            count = len(self.exits)
            if (count == 1 and "up" not in self.exits and "down" not in self.exits):
                exit = f"You see an exit to the {p.join(self.exits)}."
                exit = str(exit)
                description.append(exit)
            elif (count == 1 and ("down" in self.exits or "up" in self.exits)):
                exit = f"You see an exit going {p.join(self.exits)}."
                exit = str(exit)
                description.append(exit)
            else:   #add an elif to give better grammar when up and down are not in self.exits
                exits = f"You see exits {p.join(self.exits)}."
                exits = str(exits)
                description.append(exits)


        print(text_wrapper("\n".join(description)))
# if the item in the get string is in self.objects, it needs to be added to an inventory list and deleted from self.objects

    def get(self, item):
        #print(f"len inventory{len(player.inventory)}")
        #print(f"max inventory{player.max_inventory}")
        if len(player.inventory) < player.max_inventory:
            if item in self.objects:
                item_data = self.objects.pop(item)   # remove from room and get item data
                player.inventory[item] = item_data   # add to player inventory
                print(f"You pick up the {item}.")
            else:
                print(f"There is no {item} here.")
        else:
            print(f"Your pockets are full.")

    def examine(self, item):

        if item in self.objects:
            print(text_wrapper(self.objects[item]))
        elif item in player.inventory:
            print(text_wrapper(player.inventory[item]))
        else:
            print(f"There is no {item} here.")

    def search(self, interact):  #input to this function actually comes from the variable "item" in the 'commands' function elif action block
        #remove items from interact's pockets and put them into room inventory
        # print message_action
        if interacts[interact].pockets:
            print (text_wrapper(interacts[interact].message_action))

            rooms[player.current_room].objects.update(interacts[interact].pockets)
            interacts[interact].pockets = {}

            objects = p.a(p.join(list(rooms[player.current_room].objects.keys())))
            print (f"There is now {objects} here.")

        else:
            print(f"You search the {interact}, yielding nothing.")

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
    def __init__(self, interact, location, keyword, item, item2, exits, pockets, talisman, message_talisman, message_attack, message_true, message_action, message_help_you, message_help_true, message_give_to_you, message_give_true, state = False, state_help_you = False):
        self.interact = interact
        self.location = location
        self.keyword = keyword
        self.item = item
        self.item2 = item2
        self.exits = exits
        self.pockets = pockets
        self.talisman = talisman
        self.message_talisman = message_talisman
        self.message_attack = message_attack
        self.message_true = message_true
        self.message_action = message_action
        self.message_help_you = message_help_you
        self.message_help_true = message_help_true
        self.message_give_to_you = message_give_to_you
        self.message_give_true = message_give_true
        self.state = state
        self.state_help_you = state_help_you



def load_interacts_from_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        interacts = {}
        for interact, details in data.items():
            interacts[interact] = Interacts(
                interact=interact,
                location = details["location"],
                keyword = details.get("keyword"),
                item = details.get("item"),
                item2 = details.get("item2"),
                exits = details.get("exits", []),
                pockets = details.get("pockets", {}),
                talisman = details.get("talisman"),
                message_talisman = details.get("message_talisman"),
                message_attack = details.get("message_attack"),
                message_true = details.get("message_true"),
                message_action = details.get("message_action"),
                message_help_you = details.get("message_help_you"),
                message_help_true = details.get("message_help_true"),
                message_give_to_you = details.get("message_give_to_you"),
                message_give_true = details.get("message_give_true"),
                
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
        #print (interacts)
        for location in interacts:
           rooms[location].interacts.append(interacts)



class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = {}
        self.max_inventory = 2   #set the number of items a player can carry
        self.move_history = {}
        self.turns_in_room = 0
        self.phone_can_be_charged = False
        self.phone_charged = False
        self.phone_updated = False
        self.phone_signal = False
        self.maze = False
        self.you_are_fckd = False
        self.car_waiting = False
        self.how_many_calls = 0

    def drop(self, item):
        if (item in self.inventory and item == "rucksack"):
            if len(self.inventory) > 2:
                print("You need to drop something else first.")
            else:
                rooms[player.current_room].objects[item] = self.inventory.pop(item)
                print(f"You drop the {item}.")
                player.max_inventory = 2
        elif (item in self.inventory):
            rooms[player.current_room].objects[item] = self.inventory.pop(item)
            print(f"You drop the {item}.")
        else:
            print(f"You don't have the {item}.")

    def move_tracker(self, move_number, room_number):
        self.move_history[move_number] = room_number

rooms = load_rooms_from_json("rooms.json")
interacts = load_interacts_from_json("interacts.json")
index_interacts_into_Room("interacts.json")
player = Player(250)

def reset():
    global rooms
    global interacts
    player.phone_can_be_charged = False
    player.phone_charged = False
    player.phone_updated = False
    player.phone_signal = False
    player.current_room = 250
    player.inventory = {}
    player.max_inventory = 2
    player.move_history = {}
    player.turns_in_room = 0
    player.maze = False
    player.you_are_fckd = False
    player.car_waiting = False
    player.how_many_calls = 0

    rooms = {}
    rooms = load_rooms_from_json("rooms.json")

    interacts = {}
    interacts = load_interacts_from_json("interacts.json")
    #better reset all flags too
    index_interacts_into_Room("interacts.json")

def text_wrapper(description):
    full_text = description
    lines = full_text.split("\n")
    wrapped_lines = []
    for line in lines:
        if line.strip():
            wrapped_lines.extend(textwrap.wrap(line, width=80))
        else:
            wrapped_lines.append('')


    return ("\n".join(wrapped_lines))

def talisman(attacker):
    #print ("Talisman")
    if interacts[attacker].talisman in player.inventory:
        if interacts[attacker].state == False:
            print(text_wrapper(interacts[attacker].message_talisman))
        #print(interacts[attacker].message_true)
        if interacts[attacker].message_true:
            print(text_wrapper(interacts[attacker].message_true))
        interacts[attacker].state = True
    else:
        return

def rucksack():
    player.max_inventory = 9      #This is one point of departure from it being an "engine" to a game. If the player finds the rucksack, his carrying capacity increases to the integer specified here.
    #print(f"Rucksack: {player.max_inventory}")

def interact_in_current_room():
    for room in rooms[player.current_room].interacts:
        if player.current_room in room:   #if the current room has an interact in it
            int_data = room[player.current_room]
            interact = int_data[0]
            #print (interact)
            return interact


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():


    clear_screen()
    print()
    input_list = ["1", "2", "3", "4"]
    while True:
        clear_screen()
        print("1: Start\n2: Instructions\n3: About\n4: Exit")
        input = getch()

        if input == "2":

            clear_screen()
            print()
            rooms[998].describe()
            print("Press any key for main menu")
            input = getch()
            if input =="":
                break

        elif input =="1":


            clear_screen()
            print()
            rooms[999].describe()

            break
        elif input =="3":
            clear_screen()
            print()
            print("Coded in Python by Andrew Waddington, 2025")
            print("Press any key for main menu")
            input = getch()
            if input =="":
                break
        elif input =="4":
            clear_screen()
            print()
            print("Bye")
            exit()
        elif input not in input_list:
            continue
        else:
            break

    main_loop()

def main_loop():

    rooms[997].describe()

    count = 1
    last_move = 1
    game_on = True
    fckdflag = False
    fckdcounter = 0
    global moves_possible
    moves_possible = True
    while game_on == True:


        current_room = rooms[player.current_room]
        #print (f"This move: {count}")
        #print (f"Last move: {last_move}")
        player.move_tracker(count, player.current_room)

        #print (player.move_history[count])
        #print (f"current room object{current_room}")
        #print (player.current_room)

        if count == 1:
            current_room.describe()
            #print(f"Turns in room:{player.turns_in_room}")

        elif player.move_history[last_move] != player.current_room:
            current_room.describe()
            player.turns_in_room = 0
            #print(f"Turns in room: {player.turns_in_room}")
        else:
            player.turns_in_room +=1
            #print (f"Turns in room: {player.turns_in_room}")

        if (player.you_are_fckd == True and fckdflag == False):
            fckdcounter = count
            fckdflag = True
            #print("You're fucked")
        if (fckdcounter == count - 1 and fckdflag == True):
            print("You are being followed.")
        if (fckdcounter == count -3 and fckdflag == True): #SOME PROBLEMS HERE
            if player.maze == True:
                print(text_wrapper("Swimming around in the pitch blackness, drowning in the liquified excrement of death row inmates is not the way you had expected to die.\nLuckily for you however, prison guards have been on your trail for the past half hour or so.\nYou feel a hand on your shoulder. A sharp crack to the head knocks you out cold."))
                game_on = False
            else:
                print(text_wrapper("Three guards appear. Despite being outnumbered, you put up a good fight in return for a merciless kicking."))
                game_on = False
#not tested last block
        if player.turns_in_room == 0:
            for room in rooms[player.current_room].interacts:
                if player.current_room in room:   #if the current room has an interact in it
                    int_data = room[player.current_room]
                    interact = int_data[0]
                    if (interacts[interact].message_attack and interacts[interact].state ==False):
                        moves_possible = False
        if (player.current_room == -939 and "wallet" in player.inventory):
            rooms[991].describe()
            print("\n\n******** You have completed 'The Big House' ********\n\n******************** GAME OVER *********************\n\nPress space to return to the main menu")
            while True:
                in_put = getch()
                if in_put ==" ":
                    print(in_put)
                    reset()
                    main()
                else:
                    continue

        if (player.current_room == -1143 and "torch" not in player.inventory):
            player.you_are_fckd = True

        elif (player.maze == True and "crowbar" not in player.inventory):
            player.you_are_fckd = True

        elif (player.current_room == -939 and "wallet" not in player.inventory):
            rooms[990].describe()
            game_on = False

        if player.turns_in_room > 0:       # gives a chance for the player to see if there is something dangerous, but not take a second move in the room
            for room in rooms[player.current_room].interacts:
                if player.current_room in room:
                    #if the current room has an interact in it
                    int_data = room[player.current_room]
                    interact = int_data[0]
                    if interacts[interact].talisman:
                        talisman(interact)
                    #print (f"The {interact}'s state is {interacts[interact].state}")
                    if interacts[interact].message_attack:
                        if interacts[interact].state == False:
                            print(text_wrapper(interacts[interact.strip()].message_attack))
                            interacts[interact.strip()].state = True
                            game_on = False

                            break

                        # we need a death sequence here which includes a reset
                        # state = True
        if game_on == True:
            #print(f"objects in rooms{rooms[player.current_room].objects.keys()}")
            if "rucksack" in player.inventory:
                rucksack()
            if ("phone" in player.inventory and player.phone_can_be_charged == True and player.current_room == -551) or ("phone" in rooms[player.current_room].objects.keys() and player.phone_can_be_charged == True and player.current_room == -551):
                player.phone_charged = True
                print(text_wrapper("Ivan charges your phone. Now your Nokia's battery is at 100%."))
                player.phone_can_be_charged = False
                if (player.phone_charged == True and player.phone_updated == False):
                     #update phone description
                    player.phone_updated = True
                    if "phone" in player.inventory:
                        #print(f"player.inventory[phone]{player.inventory["phone"]}")
                        player.inventory["phone"] = "\n  ***WELCOME TO NOKIA***\n\n||||||||||        BATTERY  100%\n..........        SIGNAL     0%\n\nCONTACTS:\nChemical Chris\nFast Eric\nBig Bev\nFat Bob\n"
                    else:
                        rooms[player.current_room].objects["phone"] = "\n  ***WELCOME TO NOKIA***\n\n||||||||||        BATTERY  100%\n..........        SIGNAL     0%\n\nCONTACTS:\nChemical Chris\nFast Eric\nBig Bev\nFat Bob\n"
            if (player.phone_updated == True and player.current_room == 2651):
                player.phone_signal = True
                #print (f"Phone signal{player.phone_signal}")
                if "phone" in player.inventory:
                    player.inventory["phone"] = "\n  ***WELCOME TO NOKIA***\n\n||||||||||        BATTERY  100%\n||||||||||        SIGNAL   100%\n\nCONTACTS:\nChemical Chris\nFast Eric\nBig Bev\nFat Bob\n"
            elif (player.phone_updated == True and player.current_room != 2651):
                player.phone_signal = False
                #print (f"Phone signal{player.phone_signal}")
                if "phone" in player.inventory:
                    player.inventory["phone"] = "\n  ***WELCOME TO NOKIA***\n\n||||||||||        BATTERY  100%\n..........        SIGNAL     0%\n\nCONTACTS:\nChemical Chris\nFast Eric\nBig Bev\nFat Bob\n"

            if (player.current_room == -349 or player.current_room == -939):
                player.maze = False
                #print("Bonza!")
            elif player.current_room == -1349:
                player.maze = True
                #print("Baboonza!")
            #print(f"Max inv: {player.max_inventory}")
            #print (f"moves_possible = {moves_possible}")
            #print(f"room{player.current_room}")
            #print(f"Phone can be charged: {player.phone_can_be_charged}")
            #print(f"Phone actually charged:{player.phone_charged}")
            #print(f"In maze?: {player.maze}")
            #print(f"You're fckd?: {player.you_are_fckd}, Car waiting?: {player.car_waiting}")
            commands(input("What's next? ").lower()), player.current_room
            count += 1
            last_move = count -1
            moves_possible = True
        else:
            reset()
            moves_possible = True
            count = 1
            last_move = 1
            rooms[996].describe()
            rooms[997].describe()
        game_on = True
        continue





def commands(b):

    compass = re.search(r'^ *(go *)?(north ?east\b|north ?west\b|south ?east\b|south ?west\b|north\b|south\b|east\b|west\b|down\b|up\b|ne\b|nw\b|se\b|sw\b|n\b|s\b|e\b|w\b|u\b|d\b) *$', b)
    action = re.search(r'^ *(get|drop|examine|search|teleport)( *)(.+) *$', b)
    do_with = re.search(r'^ *(kill|open)( +)(.+)(with)( +)(.+)$', b)
    one_word_commands = re.search(r'look|help|inventory|inv|quit$', b)
    give_to = re.search(r'^ *(give)( +)(.+)(to)( +)(.+)$', b)
    call = re.search(r'^ *(call) *(chemical *chris\b|chris\b|fast *eric\b|eric\b|big *bev\b|bev\b|fat *bob\b|bob\b) *$', b)



    if compass: #some problems in this block
        go, direction = compass.groups()
        direction = direction.strip()
        if moves_possible == True:
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
                direction = "northwest"
            elif direction in ("sw", "southwest", "south west"):
                direction = "southwest"
            elif direction in ("ne", "northeast", "north east"):
                direction = "northeast"
            elif direction in ("se", "southeast", "south east"):
                direction = "southeast"
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
        else:
            pass

    elif action:
        keyword, space, item = action.groups()
        #if interact and message_attack and player.turns_in_room > 0 and interact's state = False
        #pass
        #else
        item = item.strip()
        keyword = keyword.strip()
        if (keyword and space and item):
            if moves_possible == True:
                if keyword == "get":
                    rooms[player.current_room].get(item.lstrip())
                    #print(f"You pick up the {item}")
                    #print(player.inventory)
                elif keyword == "drop":
                    player.drop(item.lstrip())
                elif keyword == "examine":
                    rooms[player.current_room].examine(item.lstrip())
                elif keyword == "search":   #This mess to sort out

                    #print(f"Interact in room: {rooms[250].interacts}")
                    if item.strip() == interact_in_current_room():
                        rooms[player.current_room].search(item.lstrip()) #in this case "item" refers to an interact
                    else:
                        print(f"The {item.strip()} must be somewhere else.")
                elif keyword == "teleport":     #cheat mode that I added to help test the later stages of the game - "item" is the room number e.g. 250
                    try:
                        player.current_room = rooms[int(item.strip())]
                        player.current_room = int(item.strip())
                    except ValueError:
                        print("Enter a valid room number.")
                    except KeyError:
                        print(f"Room {item} does not exist.")

        else:
            print("I don't understand.")

    elif do_with:
        keyword, space, interact, space2, using, item = do_with.groups()
        if (keyword and space and interact and space2 and using and item):
            #print (keyword, space, interact, space2, using, item)
            #print(player.inventory[item])
            if (interact.strip() in interacts and keyword == interacts[interact.strip()].keyword and item.strip() == interacts[interact.strip()].item and item.strip() in player.inventory and interacts[interact.strip()].location == player.current_room and interacts[interact.strip()].state == False):

                #print("Bonza")
                #print(rooms[player.current_room].exits)
                #update exits list in rooms from interacts
                rooms[player.current_room].exits.extend(interacts[interact.strip()].exits)
                rooms[player.current_room].message = interacts[interact.strip()].message_true
                #interacts[interact.strip()].state = "True"
                print(text_wrapper(interacts[interact.strip()].message_action))
                #print(text_wrapper(interacts[interact.strip()].message_true))
                interacts[interact.strip()].state = True
                if keyword == "kill":
                    #print ("Bonza!")
                    interacts[interact.strip()].keyword = "search"
                    interacts[interact.strip()].message_action = f"You search the {interact.strip()}'s pockets."
            else:
                print("You can't do that.")
        #case when you don't have the item
    elif give_to:
        keyword, space, item, space2, to, interact = give_to.groups()
        if (keyword and space and item and space2 and to and interact):
        #print(keyword, space, item, space2, to, interact)
            if (interact.strip() in interacts and keyword == interacts[interact.strip()].keyword and item.strip() == interacts[interact.strip()].item and item.strip() in player.inventory and interacts[interact.strip()].location == player.current_room and interacts[interact.strip()].state == False):
                player.inventory.pop(item.strip())
                print(text_wrapper(interacts[interact.strip()].message_help_you))
                rooms[player.current_room].exits.extend(interacts[interact.strip()].exits)
                rooms[player.current_room].message = interacts[interact.strip()].message_help_true
                player.phone_can_be_charged = True
                interacts[interact.strip()].state_help_you =True
            elif (interact.strip() in interacts and keyword == interacts[interact.strip()].keyword and item.strip() == interacts[interact.strip()].item2 and item.strip() in player.inventory and interacts[interact.strip()].location == player.current_room and interacts[interact.strip()].state_help_you == True):
                player.inventory.pop(item.strip())
                print(text_wrapper(interacts[interact.strip()].message_give_to_you))
                rooms[player.current_room].exits.extend(interacts[interact.strip()].exits)
                rooms[player.current_room].message = interacts[interact.strip()].message_give_true
                rooms[player.current_room].objects.update(interacts[interact.strip()].pockets)
                #print (p.a(rooms[player.current_room].objects.keys()))
                interacts[interact.strip()].pockets = {}
            else:
                print("You can't do that.")
    elif call:
        call, nickname = call.groups()

        if player.how_many_calls == 0:
            if ("phone" in player.inventory and player.phone_charged == False and player.phone_signal == False):
                print("You need to charge your phone first.")
            elif ("phone" in player.inventory and player.phone_charged == True and player.phone_signal == False):
                print("No mobile signal here.")
            elif ("phone" in player.inventory and player.phone_charged == True and player.phone_signal == True):
                #print(call, nickname)
                if (nickname == "chris".strip() or nickname == "chemical chris".strip()):
                    rooms[992].describe()
                    player.you_are_fckd = True
                    player.how_many_calls += 1
                elif (nickname == "eric".strip() or nickname == "fast eric".strip()):
                    rooms[993].describe()
                    player.car_waiting = True
                    player.how_many_calls += 1
                    rooms[player.current_room].message = "Looking down and to the northeast, you see that the visitors' car park has an old brown Ford Cortina waiting in it."
                    rooms[-939].description = "You are in the visitors' car park.\nFast Eric is there waiting in his rusty brown sedan."
                    print(text_wrapper(rooms[player.current_room].message))
                elif (nickname == "bev".strip() or nickname == "big bev".strip()):
                    rooms[994].describe()
                    player.you_are_fckd = True
                    player.how_many_calls += 1
                elif (nickname == "bob".strip() or nickname == "fat bob".strip()):
                    rooms[995].describe()
                    player.you_are_fckd = True
                    player.how_many_calls += 1
            else:
                print("Maybe find your phone?")
        elif player.how_many_calls > 0:
            print(text_wrapper("You are out of credit. You can top up your balance by calling Vodafone on 0333 3040 191. Calls cost 39p a minute."))


    elif one_word_commands:
        keyword = one_word_commands.group()
        #print(f"Is it {keyword}?")
        if moves_possible == True:

            if keyword == "look":
                rooms[player.current_room].describe()
                #print("look test")
            elif keyword == "help":
                rooms[989].describe()
            elif keyword == "quit":
                reset()
                main()
            elif keyword == "inv" or keyword == "inventory":
                if player.inventory:
                    inv = p.a(p.join(list(player.inventory.keys())))

                    #inv = p.a(inv)
                    print(f"You are carrying {inv}.")
                else:
                    print("You aren't carrying anything.")
        else:
            pass




    else:
        print("I don't understand.")

def room_handler(a, room):

    if a == "north":
        room += 100
        return room
    elif a == "northeast":
        room += 101
        return room
    elif a == "east":
        room += 1
        return room
    elif a == "southeast":
        room -= 99
        return room
    elif a == "south":
        room -= 100
        return room
    elif a == "southwest":
        room -= 101
        return room
    elif a == "west":
        room -= 1
        return room
    elif a == "northwest":
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
