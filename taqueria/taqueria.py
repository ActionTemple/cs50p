
# Taqueria
# Andrew Waddington

import sys

d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    add_order = 0.0
    while True:
        try:

            user_input = input("Item: ").lower()
            #print(user_input)
            your_choice = d.get(user_input.title())
            if your_choice is None:
                raise KeyError()

            else:
                add_order += your_choice
                total(add_order)


        except KeyError:

            print()
        except EOFError:
            print()
            print (f"Total: ${add_order:.2f}")
            sys.exit()




def total(add_order):

    print (f"Total: ${add_order:.2f}")
    return
    #sys.exit()

main()




