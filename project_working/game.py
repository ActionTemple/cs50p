


objects = ["torch", 55, "knife", 43, "cheese", 33]



room = 45
"""
class Room:
    def __init__(self, room_number, room_name, description, items, exits):
        self.room_number = room_number
        self.room_name = room_name
        self.description = description
        self.items = items
        self.exits = exits
"""


def main():

    while True:
        room_handler(input("What's next: ").lower())
        print(f"You are in room {room}")
        if room in objects:
            x = (objects.index(room))
            y = x - 1
            print(f"There is a {objects[y]} here")



def room_handler(a):
    global room
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
