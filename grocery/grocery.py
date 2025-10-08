# Grocery List
# Andrew Waddington



grocery_list = {}


def main():

    while True:
        try:

            food = input().upper()
            grocery_list.update({food: grocery_list.get(food, 0) + 1})




        except EOFError:
            print()
            for food in sorted(grocery_list.keys()):
                print(f"{grocery_list[food]} {food}")


            break



main()


