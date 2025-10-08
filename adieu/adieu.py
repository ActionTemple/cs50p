
# Adieu, Adieu
# Andrew Waddington

import inflect
import sys
p = inflect.engine()
names = []


def main():
    while True:
        try:
            na_me = input()
            names.append((na_me))


        except EOFError:
            #print()

            print(f"Adieu, adieu, to",(p.join(names)))
            sys.exit()
main()
