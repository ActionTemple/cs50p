
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
"""
    def get(self):
        if item in self.objects:
"""
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



rooms = load_rooms_from_json("rooms.json")


def main():

    room = 24

    while True:

        print(room)

        current_room = rooms[room]
        current_room.describe()
        room = room_handler(input("What's next: ").lower(), room)
        print(f"You are in room {room}")

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
