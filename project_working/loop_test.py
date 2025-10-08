import json

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


index_interacts_into_Room("interacts.json")


#rooms[player.current_room].exits.extend(interacts[interact.strip()].exits)

