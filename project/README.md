# The Big House
### Video Demo:  <URL HERE>
### Description:
The Big House is a text adventure in the style of Zork and Colossal Cave Adventure. The object of the game is to navigate the environment, in this case a prison, opening up areas of the map, until the player reaches their goal, which is to escape. In order to achieve this, the user inputs commands such as **GO NORTH**, or **KILL GUARD WITH AXE**.

### Introduction
The core of the program consists of a menu of options found in the main function, a main gameplay loop, and a command-parsing mechanism which employs several regular expressions. The main content of the game is supported by three classes; `Room`, which holds the content for each location and several functions related to the location; `Interacts`, which defines NPC (non-player character) and interactive objects, and `Player`, which holds variables associated with the player and two class functions related to the player.\
Additionally, there are a number of supporting functions used for such purposes as clearing the screen, wrapping the text to 80 columns, increasing the number of items the player can carry, and resetting the game.

Input to classes `Room` and `Interacts` is driven by _**for**_ loops in the functions `load_rooms_from_json()`, and `load_interacts_from_json()`. The corresponding JSON files comprise nested dictionaries and lists nested in dictionaries which are iterated over in order to instantiate and populate class objects. These JSON files store the overwhelming majority of the content of the game; room descriptions, items and their corresponding descriptions, enemy descriptions and enemy behaviour, behaviour and messages related to interactive objects, available exits from rooms, and also miscellaneous messages associated with the game such as help, instructions, the introduction, and the arrest/reset sequence.

### Menu - `main()`
This is the starting point of the program from the point of view of the user. It is found in the `main()` function. The screen is cleared by calling the `clear_sceen()` function, and one spare line is printed. A list stores four input options, 1 to 4, which are captured later in the _**while True**_ loop by the getch module. This module allows a single key input without the need for the user to press return. Conditionals control the action depending on the input. Either a message is printed using the `rooms[room number].describe` class method, the `exit()` function is called, and/or the loop is broken. In the case of option 1, the screen is cleared, one empty line is printed, and `rooms[999].describe`, which prints the introduction to the game, is called. The _**while True**_ loop is then broken out of, leading to the function `main_loop()` being called.

### The main game loop - `main_loop()`
This forms the backbone of the game, being the point from which most of the other functions are called.\
`rooms[997].describe()` - Rooms objects numbered 989 to 999 serve solely as messages and do not make use of other variables, such as message, objects, or exits. Room 997 is the second message given to start the game, and is repeated after the player is arrested and thrown back to the beginning.

The following variables are initialised:\
`count = 1`
This counts the number of moves the player has made and is incremented by 1 for every iteration of the main loop.

`last_move = 1`\
This is set to `count – 1` at the end of each loop

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

If the player is in room -939, regardless of how they got there, and they are carrying the wallet item in the `player.inventory` variable, that means they have completed the game and get the game’s ending stored in the object `rooms[991]`, plus an appropriate message clarifying the fact the game is over and they have successfully completed it. We have another _**while True**_ loop similar to the one in the main menu prompting the user to press space. Getch takes the input as before, ignoring all other characters until the space bar is pressed. `reset()` is called, resetting all the global and class variables and also reloading the json data into clean `Room` and `Interact` objects. Next, `main()` is called, taking the user back to the main menu in case they want to play again, read the instructions, see who wrote it, or most likely, exit the program.

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

### Command Parsing - `commands()`

### Room Handling - `room_handler()`

### Classes and Objects
