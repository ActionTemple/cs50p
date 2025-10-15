# The Big House
### Video Demo:  https://youtu.be/hfWx1SkJ-mA
### Description:
The Big House is a text adventure in the style of Zork and Colossal Cave Adventure. The object of the game is to navigate the environment, in this case a prison, opening up areas of the map, until the player reaches their goal, which is to escape. In order to achieve this, the user inputs commands such as _**GO NORTH**_, or _**KILL GUARD WITH AXE**_.

### Contents
[Introduction](#introduction)\
[Menu](#menu---main)\
[The Main Game Loop](#the-main-game-loop---main_loop)\
[Command Parsing](#command-parsing---commands)\
[Room Handling](#room-handling---room_handler)\
[Classes and Objects](#classes-and-objects)\
[Auxiliary Functions](#auxiliary-functions)\
[Loading Data from JSON Files](#loading-data-from-json-files)\
[Limitations](#limitations)

### Introduction
The core of the program consists of a menu of options found in the main function, a main gameplay loop, and a command-parsing mechanism which employs several regular expressions. The main content of the game is supported by three classes; `Room`, which holds the content for each location and several functions related to the location; `Interacts`, which defines NPC (non-player character) and interactive objects, and `Player`, which holds variables associated with the player and two class functions related to the player.\
Additionally, there are a number of supporting functions used for such purposes as clearing the screen, wrapping the text to 80 columns, increasing the number of items the player can carry, and resetting the game.

Input to classes `Room` and `Interacts` is driven by _**for**_ loops in the functions `load_rooms_from_json()`, and `load_interacts_from_json()`. The corresponding JSON files comprise nested dictionaries and lists nested in dictionaries which are iterated over in order to instantiate and populate class objects. These JSON files store the overwhelming majority of the content of the game; room descriptions, items and their corresponding descriptions, enemy descriptions and enemy behaviour, behaviour and messages related to interactive objects, available exits from rooms, and also miscellaneous messages associated with the game such as help, instructions, the introduction, and the arrest/reset sequence.
###### [back](#contents)
### Menu - `main()`
This is the starting point of the program from the point of view of the user. It is found in the `main()` function. The screen is cleared by calling the `clear_sceen()` function, and one spare line is printed. A list stores four input options, 1 to 4, which are captured later in the _**while True**_ loop by the getch module. This module allows a single key input without the need for the user to press return. Conditionals control the action depending on the input. Either a message is printed using the `rooms[room number].describe` class method, the `exit()` function is called, and/or the loop is broken. In the case of option 1, the screen is cleared, one empty line is printed, and `rooms[999].describe`, which prints the introduction to the game, is called. The _**while True**_ loop is then broken out of, leading to the function `main_loop()` being called.
###### [back](#contents)
### The main game loop - `main_loop()`
This forms the backbone of the game, being the point from which most of the other functions are called.\
`rooms[997].describe()` - Rooms objects numbered 989 to 999 serve solely as messages and do not make use of other variables, such as message, objects, or exits. Room 997 is the second message given to start the game, and is repeated after the player is arrested and thrown back to the beginning.

The following variables are initialised:\
`count = 1`
This counts the number of moves the player has made and is incremented by 1 for every iteration of the main loop.

`last_move = 1`\
This is set to `count – 1` at the end of each loop.

`game_on = True`\
This is the condition that keeps the _**while**_ loop running. At first it was a simple _**while True**_ loop, but this development allows conditionals to switch it off and reset the game.

`fckdflag = False`\
This is set to `True` in the case where the game becomes unwinnable, not because of an attack by an NPC, but because the player has made a wrong choice, such as calling the wrong person when he only has one call available, or entering the maze without the torch.

`fckdcounter = 0`\
This counter references `count`, but starts from the move where `fckdflag = True`.

`global moves_possible`\
`moves_possible = True`\
This flag is set to `False` in the case where the only possible next option is for an enemy to attack the player, regardless of what he tries to do on the next move. I chose to make it global because it is used in the `commands()` function. A better design choice might have been to make it a class variable – `player.moves_possible`.

`while game_on == True:`\
The main game loop starts.

`player.current_room` is an instance variable of Player. It stores the current room number as a string.
Here it is used as a key to the dictionary rooms which maps room IDs to `Room` instances created from the _**rooms.json**_ file.
`current_room = rooms[player.current_room]` retrieves that object and assigns it to the local variable current_room. This allows the program to call methods of the `Room` class, such as `describe()`.

`player.move_tracker(count, player.current_room)`
`move_tracker` is a method of the class `Player`. It takes two arguments; `move_number` and `room_number`. Here `count` corresponds to `move_number`, and `player.current_room` corresponds to `room_number`. Inside the method it updates the dictionary `move_history` mapping the key `move_number` to the value `room_number`.

_**e.g. {1:250, 2:350, 3:351, 4:351}**_

This was implemented in order to keep track of the number of turns the player has made in the current room. In our example above, we can see that moves three and four were both made in room 351. The description of room 351 was not printed a second time in the case when the player’s move was an action and not a change of room on the compass grid. Secondly, as we will see later, it is used to trigger or not trigger the behaviour of enemies (interacts). In this game, if the player enters the room with the guard, they get one chance to see that there is an enemy, and if on the next move they attempt to do something other than kill the enemy, the enemy attacks them.

<pre>if count == 1:
    current_room.describe()</pre>


If this is the player’s first turn in the room, the `describe()` method is called, thus printing a description of the room.

<pre>elif player.move_history[last_move] != player.current_room:
    current_room.describe()
    player.turns_in_room = 0</pre>

Otherwise, if the room the player was in on the last move is not the same as the current room, i.e. if the room has changed, print a description of the new room and set the number of moves in the new room to zero.

<pre>else:
    player.turns_in_room +=1</pre>
In neither case the number of moves (turns) in the current room is incremented by 1.

<pre>if (player.you_are_fckd == True and fckdflag == False):
    fckdcounter = count
    fckdflag = True</pre>

The `player.you_are_fckd` flag is set to `True` in cases where the game becomes impossible to complete such as when you make a call on the phone to an unhelpful contact, thus wasting your single call, or when you enter the maze without the torch. `fckdcounter` is set to the same move as `count`, but doesn’t increment further, serving as a reference. `fckdflag` is set to `True`, preventing this conditional from being triggered again.

<pre>if (fckdcounter == count - 1 and fckdflag == True):
    print("You are being followed.")</pre>

One turn after `fckdcounter` being initialised and `fckdflag` being set to `True` the player gets a warning that they are being followed. This is to prepare them for the inevitable arrest/game reset.

<pre>if (fckdcounter == count -3 and fckdflag == True):
    if player.maze == True:
	    print(text_wrapper("Message A"))
	    game_on = False
else:
	print(text_wrapper("Message B"))
 	game_on = False</pre>

Two moves later the `game_on` flag is set to `False`. This stops the flow of the program from passing back through the `while game_on = True` loop before the `reset()` function has been called. If the player is in the maze he gets message A, otherwise he gets message B. In the actual program, both messages are quite long and thus are filtered through the `text_wrapper()` function in order to limit them to 80 columns of wrapped text without breaks on words.

<pre>if player.turns_in_room == 0:
	for room in rooms[player.current_room].interacts:
        if player.current_room in room:
            int_data = room[player.current_room]
            interact = int_data[0]
            if (interacts[interact].message_attack and interacts[interact].state==False):
                moves_possible = False</pre>
If it is the player’s first turn in the room, the _**for**_ loop iterates through dictionaries inside a list of interacts which have been mapped to the `rooms` dictionary by the `index_interacts_into_Room()` function. If the current room is in the dictionary keys of rooms which have an interact in them, the list of interact IDs for that room is put into the `int_data` variable, from which the first interact is put into a second variable, `interact`, from its position `[0]`. If this interact has a `message_attack`, making it an enemy, and if its state is `False`, meaning that it hasn’t been triggered, the flag `moves_possible` is set to `False`. This is used to limit the type of action the player can perform when he is about to be attacked on the next move.

<pre>if (player.current_room == -939 and "wallet" in player.inventory):
    rooms[991].describe()
    print("COMPLETED GAME MESSAGE")
    while True:
        in_put = getch()
            if in_put ==" ":
                print(in_put)
                reset()
                main()
            else:
                continue</pre>

If the player is in room -939, regardless of how they got there, and they are carrying the wallet item in the `player.inventory` variable, that means they have completed the game and get the game’s ending stored in the object `rooms[991]`, plus an appropriate message clarifying the fact the game is over and they have successfully completed it. We have another _**while True**_ loop similar to the one in the main menu prompting the user to press space. Getch takes the input as before, ignoring all other characters until the space bar is pressed. `reset()` is called, resetting all the global and class variables and also reloading the JSON data into clean `Room` and `Interact` objects. Next, `main()` is called, taking the user back to the main menu in case they want to play again, read the instructions, see who wrote it, or most likely, exit the program.

<pre>if (player.current_room == -1143 and "torch" not in player.inventory):
    player.you_are_fckd = True</pre>

If the player is in room -1143 and doesn’t have the torch the game is unwinnable and the flag `player.you_are_fckd = True` is set. The arrest and reset sequence is initiated later when the main loop checks this flag. This is the same for the following _**elif**_ block. The `player.maze = True` flag gets triggered when the player enters a particular room, and can be flipped to `False` if he leaves the maze at either of the two possible exits

<pre>elif (player.maze == True and "crowbar" not in player.inventory):
    player.you_are_fckd = True</pre>

If the player finds himself in the final room without the wallet, he is given an appropriate message. `game_on = False` breaks the loop, leading to the arrest/reset sequence.

<pre>elif (player.current_room == -939 and "wallet" not in player.inventory):
    rooms[990].describe()
    game_on = False</pre>

<pre>if player.turns_in_room > 0:
        for room in rooms[player.current_room].interacts:
            if player.current_room in room:
                int_data = room[player.current_room]
                interact = int_data[0]
                if interacts[interact].talisman:
                    talisman(interact)
                    if interacts[interact].message_attack:
                        if interacts[interact].state == False:
                            print(text_wrapper(interacts[interact.strip()].message_attack))
                            interacts[interact.strip()].state = True
                            game_on = False
                            break</pre>

This block works in a similar way to an earlier block which checks if an enemy NPC is in the room and is going to attack the player. The purpose here is to actually attack the player in the case when they have entered a room without the `talisman` item. The talisman is an object which protects you from the attack. In the case of the guard, there is no talisman; you have to kill him, but in the case of Fat Bob, whose mode of attack is an attempted strangulation, the line `if interacts[interact].talisman:` checks if there is a class variable `talisman` for that particular instance of `interacts`. If so the function `talisman()` is called which checks for the presence of the corresponding `talisman` item in `player.inventory()`, in this case being the item `collar`, described as a _**cervical neck brace**_. Since the function `talisman()` triggers the flag `interacts[interact].state = True`, the subsequent conditional is bypassed. In the case where the player is not holding the talisman in their inventory, the following conditional block triggers the `attack` message and the `game_on` flag breaking the loop and triggering the reset sequence.

<pre>if game_on == True:</pre>

All of the following block depends on nothing previously having triggered the `game_on` flag to `False`.


<pre>if "rucksack" in player.inventory:
    rucksack()</pre>
If the player is carrying the item rucksack, the function `rucksack()` is called. This expands `player.inventory` from 2 to 9 items.
<pre>if ("phone" in player.inventory and player.phone_can_be_charged == True and player.current_room == -551) or ("phone" in rooms[player.current_room].objects.keys() and player.phone_can_be_charged == True and player.current_room == -551):</pre>
In the case of the following conditions;\
the player is carrying the phone, _**and**_ it is possible to charge the phone, _**and**_ the current room is -551,

or

the phone is in the same room as the player, _**and**_ it is possible to charge the phone, _**and**_ the current room is -551
<pre>player.phone_charged = True</pre>
Set the `player.phone_charged` flag to `True` and print the following message:
<pre>print(text_wrapper("Ivan charges your phone. Now your Nokia's battery is at 100%."))</pre>
<pre>player.phone_can_be_charged = False</pre>
In order not to allow this action to be repeated the above flag is now set to `False`.
<pre>if (player.phone_charged == True and player.phone_updated == False):</pre>

The `player.phone_updated` flag prevents the description of the phone being updated more than once.
<pre>player.phone_updated = True</pre>
<pre>if "phone" in player.inventory:</pre>
If the player is carrying the phone:
        <pre>player.inventory["phone"] = "\n  ***WELCOME TO NOKIA***\n\n||||||||||        BATTERY  100%\n..........        SIGNAL     0%\n\nCONTACTS:\nChemical Chris\nFast Eric\nBig Bev\nFat Bob\n"
            else:</pre>
Otherwise, the phone must be in the same room as mandated by an earlier conditional. In which case the phone is held in an instance of the rooms class, and is updated thus:
<pre>rooms[player.current_room].objects["phone"] = "\n  ***WELCOME TO NOKIA***\n\n||||||||||        BATTERY  100%\n..........        SIGNAL     0%\n\nCONTACTS:\nChemical Chris\nFast Eric\nBig Bev\nFat Bob\n"</pre>
<pre>if (player.phone_updated == True and player.current_room == 2651):
    player.phone_signal = True</pre>

In the above conditional, if the player goes to the top of the tower where there is phone signal, he can make a call. Thus `player.phone_signal = True.`

In this case:

<pre>if "phone" in player.inventory:
    player.inventory["phone"] = "\n  ***WELCOME TO NOKIA***\n\n||||||||||        BATTERY  100%\n||||||||||        SIGNAL  100%\n\nCONTACTS:\nChemical Chris\nFast Eric\nBig Bev\nFat Bob\n"</pre>

We see that the phone’s description is updated to show a slightly different description; the phone’s signal is now 100%.

<pre>elif (player.phone_updated == True and player.current_room != 2651):
    player.phone_signal = False</pre>
Otherwise, if the player is not at the top of the tower (room 2651), the `player.phone_signal` flag is set to `False`.

<pre>if "phone" in player.inventory:
    player.inventory["phone"] = "\n  ***WELCOME TO NOKIA***\n\n||||||||||        BATTERY  100%\n..........        SIGNAL     0%\n\nCONTACTS:\nChemical Chris\nFast Eric\nBig Bev\nFat Bob\n"</pre>

In this case, if the player is carrying the phone, the phone’s description is updated to show a phone signal of 0%.

<pre>if (player.current_room == -349 or player.current_room == -939):
    player.maze = False</pre>

Rooms -349 and -939 mark exit points from the maze. Thus, the `player.maze` flag is set to `False` when the player enters these rooms.

<pre>elif player.current_room == -1349:
    player.maze = True</pre>

Likewise, room -1349 is the entry point to the maze. The `player.maze` flag is set to `True`.

<pre>commands(input("What's next? ").lower()), player.current_room</pre>

This is the key part of the `main_loop()` function. After passing through all of the preceeding conditionals, the input to the command prompt _**What’s next?**_ Is converted to lower case and passed to the `commands()` function along with the player’s current room.
<pre>count += 1</pre>
The count variable is incremented by one to show that a move has been made.
<pre>last_move = count -1</pre>
Also the previous move number is recorded.
<pre>moves_possible = True</pre>

And the flag moves_possible is set to `True`, just in case it had been previously set to `False`.

<pre>else:</pre>

Referring to the correspoding `if game_on == True` conditional above, if `game_on` is `False`:
<pre>reset()</pre>

`reset()` is called, clearing all flags, variables, and reloading game data from the JSON files.
<pre>moves_possible = True</pre>

Now the player can play.
<pre>count = 1</pre>

It is the first move.

<pre>last_move = 1</pre>

There is no meaningful previous move.

<pre>rooms[996].describe()
rooms[997].describe()</pre>

We get descriptions of the arrest sequence.
<pre>game_on = True</pre>

The condition for the operation of the `while game_on == True` loop is set to `True`.

<pre>continue</pre>

We return to the start of the loop.
###### [back](#contents)
### Command Parsing - `commands()`

The module `re` (Python’s regular expression library) is used to search input strings from `main_loop`’s input, argument `b`. The six following variables are created:
- `compass` – this handles movement between rooms, e.g. _**go north**_, or just _**n**_
- `action` – verb noun, e.g. _**drop torch**_
- `do_with` – this takes care of more complicated actions such as _**kill guard with torch**_
- `one_word_commands` – e.g. _**look**_, _**help**_
- `give_to` – similar to `do_with`; this takes care of the command _**give item to somebody**_
- `call` – _**call name**_ or _**call nick name**_

Examining the regex for variable `action`:

<pre>action = re.search(r'^ *(get|drop|examine|search|teleport)( *)(.+) *$', b)</pre>

We see `^` marking the start of the string, `*` preceded by a space allowing the user to  accidentally input a space before the command. In the first group, enclosed in parentheses we see commands `get`, `drop`, `examine`, `search`, and `teleport` separated by `|`, indicating the `OR` logical operator. Enclosed in the second group of parentheses we see `*`preceded by a space, which allows for unlimited spaces between the first and third groups. The third group `(.+)` allows for any number of any character, so basically any word or number/symbol combination. Finally we see a repeat of `*` preceded by a space to allow for any amount of white space at the end of the string. `$` marks the end of the regex, ensuring that no additional characters are captured. An example command would be “_**get torch**_”. "&nbsp;&nbsp;&nbsp;_**get**_&nbsp;&nbsp;&nbsp;_**torch**_&nbsp;&nbsp;&nbsp;" would also work, but not “_**gettorch**_”, or "&nbsp;&nbsp;&nbsp;_**gettorch**_&nbsp;&nbsp;&nbsp;". In terms of design choices I felt that not allowing a space between words is consistent with the feel of the 8/16-bit computing era. Whilst the regex is case sensitive, upper case input has already been converted to lower case in the input to the `commands()` function from the `main_loop()` function.

The following set of conditionals determine what happens in the case of a match or no match for any of these variables.

Starting with `compass`:
<pre>if compass:
    go, direction = compass.groups()
    direction = direction.strip()
    if moves_possible == True:</pre>
The matched regex is filtered into two groups; the optional `go`, and `direction`. The string direction is cleaned up with `strip()` in order to remove leading and trailing white space.\
If it is possible for the player to make a move other than `do_with`, such as _**kill NPC with hammer**_, the player can move rooms using a compass direction, stored in the variable `direction` as _**north**_, _**n**_, _**southwest**_, _**sw**_, etc.

<pre>if direction in ("n", "north"):
    direction = "north"</pre>

If the variable `direction` holds any of the items in the tuple, then `direction` is updated to the word, e.g. in this case, _**north**_.

<pre>if direction in rooms[player.current_room].exits:
    player.current_room = room_handler(direction, player.current_room)</pre>

If the string in the updated `direction` is found in the `exits` attribute of the current room instance, then the direction and the current room are passed to the function `room_handler()`, the output of which is the new room number which updates `player.current_room`.
<pre>else:
    print("You can't go that way")</pre>
In the case where `direction` is not found in the list of exits, you cannot go that way, `player.current_room` is not updated, and you get an appropriate message.

<pre>elif action:
    keyword, space, item = action.groups()</pre>

If `re` matches `action`, the regex is divided into the three groups `keyword`, `space`, and `item`, as per the parentheses in the regex.
<pre>item = item.strip()
    keyword = keyword.strip()</pre>
Leading and trailing white space is cleaned from item and keyword.
<pre>if (keyword and space and item):</pre>
If all of the groups hold a string. This excludes player input error where a word is missing and the variable holds `None`.
<pre>if moves_possible == True:</pre>
Global variable `moves_possible` has been covered earlier in the discussion of `main_loop()` and is applied here in order to stop the player from making actions while under threat of attack.
<pre>if keyword == "get":
rooms[player.current_room].get(item.lstrip())</pre>
In the case of _**get item**_ the `item` string has its leading white space removed and is inputted as an argument into the `get` method of the current room’s instance of the `Room` class.

<pre>elif keyword == "drop":
    player.drop(item.lstrip())</pre>
In the case of _**drop item**_, the `player.drop` method is called inputting the item string as an argument. This will be covered in a later discussion of the `Player` class.

<pre>elif keyword == "examine":
    rooms[player.current_room].examine(item.lstrip())</pre>
As with `get`, except using the method `examine`.

<pre>elif keyword == "search":
if item.strip() == interact_in_current_room():
    rooms[player.current_room].search(item.lstrip())</pre>
As with `examine` and `get`, except this method is `search`. In this case the variable item maps to the name of an interact such as warden, guard, fat bob.

<pre>else:
    print(f"The {item.strip()} must be somewhere else.")</pre>
If the interact, `item`, is not here, an appropriate message is given.

<pre>elif keyword == "teleport":
    try:
        player.current_room = rooms[int(item.strip())]
        player.current_room = int(item.strip())
    except ValueError:
        print("Enter a valid room number.")
    except KeyError:
        print(f"Room {item} does not exist.")</pre>

This is a cheat mode I added in order to save time testing later stages of the game without moving around the map too much. It allows the player to jump to any room using the room number, e.g. _**teleport 450**_ takes you to the store room, _**teleport -939**_ takes you to the car park, which is the final room of the game. In the case where the player types something which is not a room number, e.g. _**teleport cat**_, this try-except block catches a `ValueError`. In the case where the player enters a room which does not exist, such as _**teleport 2**_, the try-except block catches a `KeyError`, since 2 is not a key to the `rooms` dictionary.

<pre>elif do_with:
    keyword, space, interact, space2, using, item = do_with.groups()
    if (keyword and space and interact and space2 and using and item):</pre>

If `re` matches `do_with`, and if all of the `do_with` groups contain strings, and if all the following conditions are met:

<pre>if (interact.strip() in interacts and keyword == interacts[interact.strip()].keyword and item.strip() == interacts[interact.strip()].item and item.strip() in player.inventory and interacts[interact.strip()].location == player.current_room and interacts[interact.strip()].state == False):</pre>

These are;
- the `interact` must be in the dictionary of `interacts`,
- the `keyword` variable must match the `keyword` in the `interacts` instance of the `interact` mentioned in the command,
- the `item` referred to in the command must match the `item` in the `interacts` instance of the relevant `interact`,
- this `item` must be in the player’s inventory,
- the `interact` must be in the same room as the player,
- the interact’s state must be `False`; meaning that its behaviour has not yet been triggered.

Providing the above conditions are met, the following actions happen simultaniously:
<pre>rooms[player.current_room].exits.extend(interacts[interact.strip()].exits)</pre>

The value from the key `exits` in the current `interact`’s instance of `interacts` is added to the list of `exits` in the current room. This means that a new exit is available to the player, such as in the case where a door is unlocked.
<pre>rooms[player.current_room].message = interacts[interact.strip()].message_true</pre>

`message_true` is copied to the `message` instance variable of the current room. This results in an alteration to the description of the room, reflecting a change made as a result of the player's actions.
In the `JSON` file, an example of `message_true` looks like this: `"message_true": "The door to Fat Bob's cell is ajar.",`. In this case `message_true` replaces the original message in room 351’s description - `"message": "Fat Bob softly whispers to you through his cell door - \n'Hey there matey... are you going to help a friend...?'"`, .
It is also possible that there is no `message` instance variable in the `rooms` dictionary, in which case `message_true` is just copied and the variable is created.

<pre>print(text_wrapper(interacts[interact.strip()].message_action))</pre>

A message describing the action is printed. This may look like _**You unlock Fat Bob's cell.**_
<pre>interacts[interact.strip()].state = True</pre>
This flag is used to prevent the preceeding sequence of events being repeated, for example to avoid the player killing an NPC twice.

<pre>if keyword == "kill":
        interacts[interact.strip()].keyword = "search"
        interacts[interact.strip()].message_action = f"You search the {interact.strip()}'s pockets."</pre>

<pre>else:
    print("You can't do that.")</pre>

In the case where you have killed an NPC, the `interact` may now be searched. In order to do that, the `keyword` _**kill**_ is overwritten with _**search**_. The old `message_action` is changed to the generic one _**You search the guard’s pockets**_. If any of the matched words in the command are wrong, the message _**You can’t do that.**_ is printed.

The `elif give_to` block works shares much in common with the `do_with` block. Its purpose is to enable the player to give an item to an NPC in exchange for some favour or gift in return. There is only one NPC in _**The Big House**_ which uses this facility, however I designed it to be more flexible than is needed here. This is why it offers the option to expand the list of exits in the same way as `do_with`. In this single case the interact is `ivan`. The original description of room -551, where `ivan` is located includes the following message:

<pre>"message": "Ivan the Terrible Chef stands before the marble alter sharpening his knives... 'Ah... but I have only this beetroot. Blyat...'\nYou notice an old phone charger and a couple of dumb phones sitting on the shelf across the room.",</pre>

This should give the player the clue that Ivan would like some additional ingredients, and that in return he might be able to charge your phone. The player should have the item `fish` in their inventory before inputting the command _**give fish to ivan**_.

<pre>player.inventory.pop(item.strip())</pre>

The item, which in this case is the _**fish**_, is deleted from the player’s inventory.

<pre>print(text_wrapper(interacts[interact.strip()].message_help_you))</pre>

`message_help_you` is printed. The player gets the following message: _**Spacibo bolshoi! Fish make base of klassik salat. I can charge for you phone. Now I am just needing one more thing for Fat Bob's last meal.**_

<pre>rooms[player.current_room].exits.extend(interacts[interact.strip()].exits)</pre>

In the case where giving something to an NPC may result in a door being opened or an exit otherwise revealed, such as in the case with the guard, this line adds exits to the room’s list of available exits. In the case of Ivan, our only NPC of this kind, it does nothing.

<pre>rooms[player.current_room].message = interacts[interact.strip()].message_help_true</pre>

A new message replaces the room’s original message:

<pre>"message_help_true": "Ivan the Terrible Chef is pottering about the kitchen, mumbling and grumbling incoherently about how he is sometimes forced to be picking suspect mushrooms off the passage walls to use in the prison food. ‘Things are so bad here’, he rants. He would like to put a spanner in the spokes of the wheels of ‘these chiefs in tower’.",</pre>

<pre>player.phone_can_be_charged = True</pre>

It is now possible for the player to charge their phone. An explanation of how the phone is charged is given in the discussion of `main_loop()`. To summarise, it depends on the above flag being set to `True`, and the phone either being in the player’s inventory or in room -551 at any point after the flag is set. If either of these conditions is met, the phone’s description is updated from

<pre>"A Nokia 3310. It looks a lot like the phone that was in your pocket when you were arrested. The battery is dead."</pre>

to

<pre>“\n  ***WELCOME TO NOKIA***\n\n||||||||||        BATTERY  100%\n..........        SIGNAL     0%\n\nCONTACTS:\nChemical Chris\nFast Eric\nBig Bev\nFat Bob\n"</pre>

<pre>interacts[interact.strip()].state_help_you =True</pre>

This flag is set `True` as a condition of allowing the second part of the gift-giving process to take place.

The player has earlier been given the hint that Ivan needs something else to complete his recipe -  _**Now I am just needing one more thing for Fat Bob's last meal**_. The player also knows that Ivan is making some kind of _**'klassik salat'**_ involving fish. The player might also suspect that Ivan is Russian. With the help of Google, it should be easy to deduce that the next stage of gift giving is as follows; _**give shuba to ivan**_.
The `shuba` is `popped` (deleted) from the player's dictionary, as before, `message_give_to_you` is printed, any new exits are added to the room’s list of exits, although as before, there are none, and `message_give_true` is copied into the message instance variable of the room’s description.

<pre>rooms[player.current_room].objects.update(interacts[interact.strip()].pockets)</pre>

Item(s) in the `interact`’s pockets variable are copied into the dictionary of objects in the current room, in this case -551. This is the gift Ivan gives to you.

<pre>"pockets": {"crowbar": "A heavy, iron crowbar. About three feet long. Good for prying lids and hatches."}</pre>
<pre>interacts[interact.strip()].pockets = {}</pre>

`pockets` is cleared, resulting in all items being deleted.

The result is that the player can now see the ‘gift’ in the room available to _**get**_. A better design might have been to check if the player’s inventory is fewer than 2, or 9 if he is carrying the rucksack, if so adding the gift directly and only if they are at the limit of their carrying capacity add the item to the room’s dictionary of objects.

The `elif call` block works on the following conditions being met:

<pre>if player.how_many_calls == 0:</pre>

The player gets one chance only to make a call, otherwise

<pre>elif player.how_many_calls > 0:</pre>

they get a message telling them that they are out of credit and that they must make an expensive call in order to top up their balance. There is no facility to do this, and if the player gets this message, the game is unwinnable.

<pre>if ("phone" in player.inventory and player.phone_charged == False and player.phone_signal == False):
    print("You need to charge your phone first.")
elif ("phone" in player.inventory and player.phone_charged == True and player.phone_signal == False):
    print("No mobile signal here.")
elif ("phone" in player.inventory and player.phone_charged == True and player.phone_signal == True):</pre>

The conditionals above determine whether the player is carrying the phone, whether it is charged, and whether there is phone signal. The only location high enough to get phone signal is room 2651, which is the top of the watchtower. Only in this case can the player make a call.
They can call one of four _**‘friends’**_.
Should the player call one of the ‘wrong’ friends, _**Chemical Chris, Big Bev, or Fat Bob**_, the player gets a message describing the call, held in the dictionary `rooms`' descriptions, `player.you_are_fckd` is set to `True`, since the game is now unwinnable,  and `player.how_many_calls` is incremented by 1, thus preventing further calls.

In the case where they choose to call _**Fast Eric**_, a description of the call is given, the `player.car_waiting` flag is set to `True` (N.B. this flag is not actually used), as before `player.how_many_calls` is incremented by 1, the room’s message is updated to show that a car is waiting, the description of the final room, room -939, is updated with something relevant to the situation, and finally the room’s updated message is printed.

The `elif one_word_commands` block is the least sophisticated. _**look**_ repeats the current room’s description, _**help**_ prints a little message of orientation and advice, and _**quit**_ calls the function `reset()`, which clears all variables and flags before reloading `JSON` files, calling `main()`, which takes the player back to the main menu ready to start a fresh game from the beginning. The command _**inventory**_, or _**inv**_, results in a list of items the player is carrying being printed. The _**inflect**_ module is used to provide correct indefinite articles, _**a**_ and _**an**_.
###### [back](#contents)
### Room Handling - `room_handler()`

This was the starting point for the game's design. I imagined a 2D grid with an x-axis 0-9, and a y-axis 0-90, thus giving a square of numbers 0-99. Later on I revised this to what we have now which is 0-999, plus a z-axis which can be accessed by adding or subtracting 1000. The game starts in room 250. In order to go north, 100 is added to the room number. To go south, subtract 100. To get east and west, add or subtract 1 respectively. Northeast + 101, northwest +99, southeast -99, southwest -101, up +1000, down -1000.

Input to this function comes from the `commands()` function, filtered through the `if compass` block, which in turn is received from the `main_loop()` function. In the `if compass` block of the `commands()` function we see the following conditional:

<pre>if direction in rooms[player.current_room].exits:
    player.current_room = room_handler(direction, player.current_room)</pre>

This functions to update `player.current_room` with the new room number by passing in the direction word, e.g. _**north**_, and `player.current_room`, e.g. _**250**_, as arguments _**a**_ and _**room**_ respectively. The updated room is thus returned

<pre>if a == "north":
    room += 100
    return room</pre>

and `player.current_room` is updated.
###### [back](#contents)
### Classes and Objects
### Room

<pre>def __init__(self, room_id, description, message, objects, exits, interacts=None):
    self.room_id = room_id
    self.description = description
    self.message = message
    self.objects = objects
    self.exits = exits
    if interacts != None:
        self.interacts = interacts
    else:
        self.interacts = []</pre>

Instances of the `Room` class have the following attributes:
`room_id` this stores the room number in the form of an integer,
`description` this stores the description of each room in the form of a string,
`message` this is an addition to the description of each room - also a string,
`objects` not to be confused with the programming term, this stores a dictionary of items collected by the player,
`exits` stores a list of exits from each room,
`interacts` if there is one or more interacts in the room interacts stores them in a list.

In addition to `__init__()`, `Room` has several other methods; `describe()`, `get()`, `examine()`, and `search()`. `The drop()` method can be found in the Player class, since I felt that it was more closely related to the player. It may also have been reasonable to locate `get()` and `examine()` in the `Player` class. The functionality would not have been affected. `Room` is also supported by the auxiliary functions `load_rooms_from_json()` and `index_interacts_into_Room()`, which will be discussed separately.

### Describe - `describe()`
<pre>items = []
    description = []
    description.append(self.description)</pre>

An empty list to hold items (`items = []`) is initialised, as is a list to hold a full description (`description = []`). The main description of the room held in `self.description` is appended to the list `description`.
Further attributes `message`, `objects`, and `exits` may or may not be present depending on whether their keys exist in the JSON file, and so are appended to the list by a series of conditionals:

<pre>if self.message:
    description.append(self.message)</pre>
If there is a message, add it to the description.

<pre>if self.objects:
    for object in self.objects:
        object = p.a(object)
        items.append(object)</pre>
If there are any items in the room this _**for**_ loop iterates through each item, adds a comma and a grammatical article to it, (such as _**a chair, an apple,**_) stores it as a string in the variable `object`, before appending that variable to the list of items. The _**inflect**_ module handles this; an instance of this class being created globally, `p = inflect.engine()`, in order to be used in other places throughout the program.

<pre>look = f"There is {p.join(items)} here."
look = str(look)
description.append(look)</pre>

The full sentence is created with correct punctuation and appended to the list `description`.
Only singular countable nouns can be parsed using this method. In order to handle uncountables, such as cheese, plurals, and collectives, some slightly more complex logic would be required, since inflect on its own appears unable to do this. Additionally, the regex would need to handle separately spaced words to refer to one item. I decided to keep it simple because I was aiming for a minimum viable product. Here are some examples that I decided not to accommodate:

_**a bunch of keys**_

_**some marbles**_

(There aren’t) _**any marbles**_ here

(You pick up) _**the cheese**_

<pre>elif self.exits:
    count = len(self.exits)</pre>

If the room has exits, store the number of exits in the variable `count`.
The following block is designed to handle the grammatical situation where there may be one or more exits with different grammatical rules. For example _**You see an exit to the north**_ is fine, but _**You see an exit to the down**_ would not be correct standard British English. Here I have chosen _**You see an exit going down**_. In the case where there are two or more exits, we have _**You see exits north, south, and up**_, which is acceptable. As before, the sentence is compiled and appended to the description.

<pre>elif self.exits:
count = len(self.exits)
if (count == 1 and "up" not in self.exits and "down" not in self.exits):
    exit = f"You see an exit to the {p.join(self.exits)}."
    exit = str(exit)
    description.append(exit)
elif (count == 1 and ("down" in self.exits or "up" in self.exits)):
    exit = f"You see an exit going {p.join(self.exits)}."
    exit = str(exit)
    description.append(exit)
else:
    exits = f"You see exits {p.join(self.exits)}."
    exits = str(exits)
    description.append(exits)</pre>

Finally the list of strings is joined using the `join` method, which adds commas and conjunction (_**and**_); inserting a new line between each string, before being passed as an argument to the `text_wrapper()` function, whose return is printed. `text_wrapper()` will be explained in more detail subsequently; its purpose is to wrap all text to 80 columns without breaking words.

<pre>print(text_wrapper("\n".join(description)))</pre>

### Get – `get()`

The purpose of this method is to allow the player to pick up items from the room they are in.

<pre>def get(self, item):
    if len(player.inventory) < player.max_inventory:
        if item in self.objects:
            item_data = self.objects.pop(item)
            player.inventory[item] = item_data
            print(f"You pick up the {item}.")
        else:
            print(f"There is no {item} here.")
    else:
        print(f"Your pockets are full.")</pre>

The argument item is passed in from the `commands()` function when the player provides an input such as _**get torch**_. The first conditional checks whether the number of items the player is carrying is fewer than the maximum permitted number, `player.max_inventory`, otherwise the player gets the message _**Your pockets are full**_. If the item is in the current room, `self.objects`, the item is ‘popped’ (deleted) from `self.objects` and added to `item_data`, which is added to the player’s inventory. If the item is not in the current room, (`else`), the player gets a message such as _**There is no torch here**_.

### Examine – `examine()`

The purpose of this function is to print the value of the dictionary, where `item` is the key.
In the example below, the output would be _**It is a heavy, aluminium Maglite. Could be considered an offensive weapon.**_

<pre>{"torch": "It is a heavy, aluminium Maglite. Could be considered an offensive weapon."}</pre>

<pre>def examine(self, item):

    if item in self.objects:
        print(text_wrapper(self.objects[item]))
    elif item in player.inventory:
        print(text_wrapper(player.inventory[item]))
    else:
        print(f"There is no {item} here.")</pre>

The conditionals cater for three possible situations:\
The item is in the room; `self.objects`.\
The player is carrying the item; `player.inventory`.\
Neither case is true, in which case the player gets the message _**There is no torch here.**_

### Search – `search()`

The purpose of this function is to allow the player to search the pockets of NPCs which are dead or which the player has killed.
<pre>def search(self, interact):</pre>

The interact argument here actually takes the variable `item` passed from the `commands()` function.

<pre>if interacts[interact].pockets:
    print (text_wrapper(interacts[interact].message_action))

    rooms[player.current_room].objects.update(interacts[interact].pockets)
    interacts[interact].pockets = {}

    objects = p.a(p.join(list(rooms[player.current_room].objects.keys())))
    print (f"There is now {objects} here.")

else:
    print(f"You search the {interact}, yielding nothing.")</pre>

If the interact is holding an item in its ‘pockets’, `message_action` is printed.
The item is copied from the `pockets` attribute of the interact to the `objects` attribute of the current room.
The interact’s `pockets` dictionary is cleared.
The full list of objects in the room, both the new items and the ones which were already there, is printed using inflect for punctuation and articles.

    There is a torch here.
    You see an exit to the north.
    What's next? search warden
    You rifle through the dead warden's pockets, yielding various items.
    There is now a torch, wallet, and lighter here.
    What's next?

In the event that the `interact` has nothing in its `pockets`, such as when you have already searched it, a message is given, e.g. **You search the warden, yielding nothing.**
A problem in the design appears when you try to search an interact which wouldn’t logically have pockets or hidden items, such as a door.

    You are in a narrow stone passageway.
    There is a locked door here.
    You see exits north and south.
    What's next? search door
    You search the door, yielding nothing.
    What's next?

This quirk was discovered in the write-up phase, after the testing and debugging. I have decided to leave it as it is for now, until or unless I decide to develop the game further. It could be fixed using some conditional logic.

### Interacts

Instances of the `Interacts` class have many attributes for holding various strings, lists, dictionaries, and states. This class was designed with flexibility in mind; however, were I to design this game again from scratch, I would implement more than one class for this category, each with a narrower range of functionality. For example, it would be better to have separate classes for enemy NPCs, inert items such as doors and hatches, and benign actors who give gifts or information in exchange for items. This class has no methods.

The following attributes are stored in `Interacts`:\
`location`; the room number where the `interact` lives,\
`keyword`; the keyword that activates the `interact`, e.g. _**kill**_, _**search**_,\
`item`; the first item that can be given to the `interact`,\
`item2`; the second item that can be given to the `interact`,\
`exits`; any new exits that solving the `interact`’s puzzle can be added to the current room,\
`pockets`; what the interact has in its pockets – the player can get these by searching the `interact` when it is dead,\
`talisman`; the item which, if carried by the player, can protect them from an attack by an enemy NPC `interact`,\
`message_talisman`; the message the player gets if they avoid attack by carrying the `talisman` item,\
`message_attack`; the message the player gets if they are attacked by an enemy NPC `interact`,\
`message_true`; this is the message given to the player if he has solved the `interact`’s first or only puzzle. This message is persistent and stays with the description of the room, in the attribute `message`,\
`message_action`; this message is given to the player only once, upon solving the first or only puzzle,\
`message_help_you`; this message is displayed only once, upon giving a gift to a benign NPC,\
`message_help_true`; this message is persistent and stays in the attribute `message`, until the player has completed the second stage of their interaction with the NPC,\
`message_give_to_you`; like `message_action`, this message is displayed only once, upon completing the second stage of their interaction with the NPC,\
`message_give_true`; this final message is persistent and is copied to the `message` attribute of the `rooms` instance,\
`state`; initialised `False`, set to `True` once the first stage of the interaction has taken place,\
`state_help_you`; initialised `False`, set to `True` after the `interact` has received their first gift

### Player

Instances of the `Player` class have several attributes for holding dictionaries, integers and states related to the player.\
These are:

`current_room`; initialised as the starting room, room 250, when the class is created - `player = Player(250)`,\
`inventory`; the dictionary of items the player has collected,\
`max_inventory`; the maximum number of items the player may carry. Initially set to 2, this is expanded to 9 when the player finds the rucksack,\
`move_history`; dictionary of moves mapped to room numbers in the format _**{1:250, 2:350, 3:351, 4:351}**_ which is updated by the method `move_tracker()` in the same class,\
`turns_in_room`; an integer storing the number of turns which have been made in the same room. See discussion of `main_loop()`,\
`phone_can_be_charged`; initialised as `False` and set to `True` when the player gives the fish to Ivan. See discussion of the `elif give_to` block in the `commands()` function,\
`phone_charged`; as per `phone_can_be_charged`,\
`phone_updated`; as per `phone_can_be_charged`,\
`phone_signal`; set to `True` when the player is in room 2651. See discussion of `the main_loop()`,\
`maze`; if the player is in the maze this flag is set to `True`,\
`you_are_fckd`; `True` if the game becomes unwinnable,\
`car_waiting`; `True` if the player makes the correct phone call,\
`how_many_calls`; this variable stores the number of calls the player has made,

In addition to `__init__()`, `Player` has two other methods. These are `drop()`, and `move_tracker()`.
The purpose of `drop()` is to release an item from the player’s inventory. I decided to include it in the `Player` class since it represents something going from the player into the environment.

### Drop - `drop()`

<pre>if (item in self.inventory and item == "rucksack"):</pre>
`drop()` takes the argument `item`. The first check is to see if the item to be dropped is the rucksack. This is important since presence of the rucksack in the player’s inventory expands `player.max_inventory` from 2 to 9 items; this represents the potential number of items the player could be carrying.

<pre>if len(self.inventory) > 2:
    print("You need to drop something else first.")</pre>

The next check is to see how many items the player is actually carrying. It is possible they may be carrying only the rucksack, or the rucksack plus one other item; in which case `drop()` should work normally. If the player is carrying three or more items, they need to drop other items until they are carrying only two items before the rucksack may be dropped.
This logic was implemented in order to correct a bug/feature where it had been possible to collect the rucksack, thus expanding `player.max_inventory` to 9, and then drop the rucksack without resetting `player.max_inventory` to 2, keeping the full capacity.

<pre>else:
    rooms[player.current_room].objects[item] = self.inventory.pop(item)
    print(f"You drop the {item}.")
    player.max_inventory = 2</pre>

Since the player is carrying only one or two items, the rucksack is 'popped' from the player’s inventory and copied to the list of objects in the current room. The message _**You drop the rucksack.**_ is printed, and `player.max_inventory` is set to 2.

<pre>elif (item in self.inventory):
    rooms[player.current_room].objects[item] = self.inventory.pop(item)
    print(f"You drop the {item}.")</pre>

This conditional branches from the first _**if**_ statement and handles the case where the player is carrying the item they want to drop, and the item is not the rucksack. As before the item is moved from the player’s inventory to the current room’s list of objects without need to set `player.max_inventory`.

<pre>else:
    print(f"You don't have the {item}.")</pre>

This final conditional covers the case where the player is not carrying the item they wish to drop, or the item doesn’t exist in the game at all, such as _**drop cat**_.

### Move Tracker - `move_tracker()`

The purpose of `move_tracker` is to create a dictionary of move numbers and rooms, in the format, _**{1:250, 2:350, 3:351, 4:351}**_, as mentioned earlier. It receives two arguments; `move number`, from `count` in the `main_loop()` function, and `room_number`, from `player.current_room`. It is used to keep track of the number of moves the player has made in the current room in order to avoid printing the description of the room more than once and to synchronise the triggering of enemy NPCs’ behaviours.

<pre>def move_tracker(self, move_number, room_number):
    self.move_history[move_number] = room_number</pre>
###### [back](#contents)
### Auxiliary Functions

### Reset – `reset()`

The purpose of this function is to reset all instance variables and states to their initial settings before reloading `JSON` files into empty `rooms` and `interacts` dictionaries. This function is called from `main_loop()` in two possible cases:\
The `game_on` flag is set to `False` causing the control flow to break out of the main loop,

<pre>else:
    reset()
    moves_possible = True
    count = 1
    last_move = 1
    rooms[996].describe()
    rooms[997].describe()
game_on = True
continue</pre>

The player completes the game; in which case `reset()` is called, followed immediately by `main()`, when the player presses space. This takes the player back to the main menu with a fresh reload of the game in case they wish to play again – or, more likely, exit the program.

<pre>if (player.current_room == -939 and "wallet" in player.inventory):
    rooms[991].describe()
    print("SUITABLE COMPLETED GAME MESSAGE")
    while True:
        in_put = getch()
        if in_put ==" ":
            print(in_put)
            reset()
            main()
        else:
            continue</pre>

### Text Wrapper - `text_wrapper()`

The purpose of this function is to wrap all text output of more than 80 characters in length without breaking words.

From `textwrap`’s documentation: `textwrap.wrap(text, width=70, …)`\
As can be seen from the code sample below, only two arguments are used; the input variable, `line`, from the _**for**_ loop, and `width`, which is this case is set to 80 in order to look a bit like a retro terminal or 8-bit computer’s command line; 80 column mode.

<pre>def text_wrapper(description):
    full_text = description
    lines = full_text.split("\n")
    wrapped_lines = []
    for line in lines:
        if line.strip():
            wrapped_lines.extend(textwrap.wrap(line, width=80))
        else:
            wrapped_lines.append('')
    return ("\n".join(wrapped_lines))</pre>

The input argument, `description`, comes from the `rooms.describe()` method, as part of the process of outputting a description, and several places in both the `main_loop()` and `commands()` functions, where a long message is displayed, such as:

<pre>elif player.how_many_calls > 0:
    print(text_wrapper("You are out of credit. You can top up your balance by calling Vodafone on 0333 3040 191. Calls cost 39p a minute."))</pre>

The `description` string is copied to the `full_text` variable, the content of which is split on new lines creating a list which is stored in `lines`.
The list `wrapped_lines` is initialised to hold the final output.
The _**for**_ loop, `for line in lines`, iterates through each item in the list `lines`. In the case of a string after leading and trailing whitespace has been stripped, this is added to the list `wrapped_lines`. Otherwise in the case of `\n\n` a blank line is added to separate two paragraphs.\
The list of `wrapped_lines`, joined on `\n` line breaks is returned.

### Talisman - `talisman()`

This function, called from `main_loop`, checks for the item `talisman` in the player’s inventory in the case where an enemy NPC interact has the corresponding `message_talisman`.

Let us refer again to the relevant block in the `main_loop()` from which `talisman()` is called:

<pre>if player.turns_in_room > 0:
        for room in rooms[player.current_room].interacts:
            if player.current_room in room:
                int_data = room[player.current_room]
                interact = int_data[0]
                if interacts[interact].talisman:
                    talisman(interact)</pre>

`talisman()` gets called in the case where the player meets the following conditions:
they have been in the room for at least one move,
there is an `interact` in the room,
that `interact` has the attribute `talisman`.

<pre>def talisman(attacker):
    if interacts[attacker].talisman in player.inventory:
        if interacts[attacker].state == False:
            print(text_wrapper(interacts[attacker].message_talisman))</pre>

If the player has the `talisman` in their inventory, and if the `interact`’s state is `False`, meaning that this is the first time this behaviour has been triggered, that `interact`’s `message_talisman` is printed. This is a message describing the scenario in which the player is not attacked. The following block caters for the case where the `interact` has the attribute `message_true`. In this game it is not used in combination with a `talisman`, however since I wrote the content of the game in tandem with the program I anticipated more required versatility. `message_true` is a persistent message which describes a changed situation.

<pre>if interacts[attacker].message_true:
    print(text_wrapper(interacts[attacker].message_true))</pre>

Following the flow from the earlier _**if**_ block, in either case the `interact`’s state is set to `True`:

 <pre>       interacts[attacker].state = True
    else:
        return</pre>

Because of this, the player can drop the `talisman` and repeatly pass through the room where the `interact` lives without the behaviour being repeated.\
Returning to the line in `main_loop()` following the point where `talisman()` was called, we see that since `talisman()` has already set the `interact`’s state to `True`, and so `message_attack` is not printed.

<pre>if interacts[interact].message_attack:
        if interacts[interact].state == False:
            print(text_wrapper(interacts[interact.strip()].message_attack))
            interacts[interact.strip()].state = True
            game_on = False
            break</pre>

There is one `interact` to whom a `talisman` applies in this game; Fat Bob.
If the player enters room 352 without the `talisman` item, after attempting to make another move in that room `message_attack` is printed:

<pre>You are in Fat Bob's cell. There seems to be a low-key mining operation here.
You see exits northeast and west.
What's next? look
Grinning menacingly, Fat Bob turns, blocking the space between you and the
doorway. 'You stupid b*stard', he says, as he grabs your throat in an attempt to
strangle you. You are not going quietly into the night, however.
The noise caused by the commotion alerts the guards.</pre>

In this case `game_on` is set to `False` causing `reset()` to be called and `main_loop()` to be broken. The player should have learned from the previous case that Fat Bob is going to try and strangle them. Upon exploration the player finds the collar, which is described as follows:

<pre>What's next? examine collar
It is a cervical collar for neck support, made of a sturdy, plastic-like material.</pre>

The player should guess that the collar can serve as a ‘talisman’ against Fat Bob.\
Let’s look at the case where the player is carrying the talisman:

<pre>What's next? inv
You are carrying a key and collar.
What's next? e
You are in Fat Bob's cell. There seems to be a low-key mining operation here.
You see exits northeast and west.
What's next? look
'Alright matey', Fat Bob says, grinning obnoxiously; 'I'm off'. Fat Bob leaves
quickly and silently.
What's next? look
You are in Fat Bob's cell. There seems to be a low-key mining operation here.
You see exits northeast and west.
What's next?</pre>

### Rucksack - `rucksack()`

<pre>def rucksack():
    player.max_inventory = 9</pre>

As mentioned earlier in the discussion of `main_loop()`, if the player finds the `rucksack`, the capacity of their inventory is expanded from 2 to 9 items. This function is called from `main_loop()` in the case where the player is carrying the rucksack.

### Check if an interact is in the current room - `interact_in_current_room()`

The purpose of this function is to check if the current room has an interact in it. It is called from the `elif action` block of the `commands()` function in the case where the player uses the command _**search**_ in the variable format `keyword item`, where `keyword = search`, and `item = interact`. An example command might be _**search warden**_.\
Thus:
<pre>if item.strip() == interact_in_current_room():
    rooms[player.current_room].search(item.lstrip())</pre>

So in our case `item` = _**warden**_, and the return of `interact_in_current_room()` for room 250 should also be _**warden**_. In which case _**warden**_ is passed as an argument to the `search()` method of the `Room` instance corresponding to room 250.

<pre>def interact_in_current_room():
    for room in rooms[player.current_room].interacts:
        if player.current_room in room:
            int_data = room[player.current_room]
            interact = int_data[0]
            return interact</pre>

This function depends on the attribute interacts actually having been populated by the function `index_interacts_into_Room()`. In this case it is worth noting that while all items in the dictionary are indexed into rooms only the first item in the dictionary is returned, i.e. if there are two interacts in the room, only the one at index `[0]` is returned. For example there may be a `guard[0]` and a `cupboard[1]`; the cupboard would be ignored. Actually there are no cases in this game where there are two interacts in the same room. It is another case where intended flexibility and scaling were abandoned in favour of aiming for a minimum viable product.

### Clear Screen - `clear_screen()`

The purpose is to clear the screen. This function is called from `main()` before showing the start of the game, about, and exit.
Depending on the client’s operating system `cls` or `clear` is used.

<pre>def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')</pre>
###### [back](#contents)
### Loading Data from JSON Files

Data describing the classes `Room` and `Interacts` is stored in `JSON` files named `rooms.json` and `interacts.json`. It is loaded into fresh dictionaries during the running of the program in two cases; the first being when the program is first executed, and secondly when the `reset()` function is called, all flags and variables are cleared, the initial data for the game is reloaded. Let us use the `rooms` loader as an example:

<pre>def load_rooms_from_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        rooms = {}
        for room_id, details in data.items():
            rooms[int(room_id)] = Room(
                room_id=int(room_id),
                description=details["description"],
                message=details.get("message"),
                objects=details.get("objects", {}),
                exits=details.get("exits", [])
            )
        return rooms</pre>

This function relies on the _**json**_ module having been imported.\
`with open() as file:` is used to open the `JSON` file.\
The `JSON` file is loaded into variable `data`.\
Dictionary `rooms` is initialised in order to store instantiated `Room` objects. The _**for**_ loop iterates through dictionary keys `room_id` and values `details`, where `room_id` corresponds to room numbers – stored as strings in the JSON file, and `details` corresponds to nested dictionaries containing attributes `description`, `message`, `objects` – with its own nested dictionary, and `exits` – with its own nested list as a value. For each `room_id` a new instance of the `Room` class is instantiated with these attributes passed to the constructor.

`return rooms` returns the dictionary of `Room` instances to the caller, where it is assigned to the variable `rooms` for use throughout the game. `load_interacts_from_json()` works in exactly the same way, except with a greater number of attributes.
###### [back](#contents)
### Limitations
Early on in this project I was aiming to keep the code separate from the game data in order to create a game engine with rooms, items, characters, and puzzles that could be swapped out to make completely different games. The `Interacts` class really broke this design philosophy in trying to be a catch-all for any kind of entity  the player could interact with. Conditional logic in the `main_loop()` and in the `commands()` functions which determines how the player interacts with interactive elements is likely to break down in the case where the `JSON` data is altered or replaced for another game or storyline with different characters.
With this in mind the `Interacts` class should be split into different classes with fixed behaviours such as;
- things you can open like doors, hatches, and cupboards,
- enemies that need to be killed or they will attack the player,
- enemies that are benign when the player is carrying a talisman,
- NPCs who receive gifts in return for favours,
- NPCs who receive gifts in exchange for gifts.
