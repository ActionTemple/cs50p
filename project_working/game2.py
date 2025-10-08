import json

class Room:
    def __init__(self, room_number, description, items, exits):
        self.room_number = room_number
        #self.room_name = room_name
        self.description = description
        self.items = items
        self.exits = exits



    def describe(self):
        print(f"Room {self.room_number}: {self.description}")
        if self.items:
            print("You see:", ", ".join(self.items))
        print("Exits:", ", ".join(self.exits))


# Load rooms from JSON file
def load_rooms_from_json(rooms):
    with open("rooms.json", "r") as file:
        data = json.load(file)
        rooms = {}
        for room_number, details in data.items():
            rooms[int(room_number)] = Room(
                room_number=int(room_number),
                description=details["description"],
                items=details.get("items", []),
                exits=details.get("exits", [])
            )
        return rooms


# Example usage
#rooms = load_rooms_from_json("rooms.json")
#current_room = rooms[24]
#current_room.describe()


# connect this room handler below with the new class variables self. etc

def main():

    while True:
        rooms = load_rooms_from_json("rooms.json")
        current_room = rooms[(room_handler(room))]
        print(f"You are in room {current_room.describe()}")
        room_handler(input("What's next: ").lower())
        #if room in objects:
         #   x = (objects.index(room))
          #  y = x - 1
           # print(f"There is a {objects[y]} here")



def room_handler(a):
    global room
    room = 24
    if a == "n":
        room = room + 10
        return (room)
    elif a == "ne":
        room = room + 11
        return (room)
    elif a == "e":
        room = room + 1
        return (room)
    elif a == "se":
        room = room - 9
        return (room)
    elif a == "s":
        room = room - 10
        return (room)
    elif a == "sw":
        room = room - 11
        return (room)
    elif a == "w":
        room = room - 1
        return (room)
    else:
        if a == "nw":
            room = room + 9
            return (room)




main()
