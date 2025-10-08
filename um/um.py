
# Regular, um, Expressions
# Andrew Waddington


import re
import sys


def main():
    print(count(input("Text: ").lower()))


def count(s):
    counter = 0
    match = re.findall(r'^um| um | um\.| um\,| um\?', s, re.IGNORECASE)

    if match:
        counter = len(match)

    return (counter)



...


if __name__ == "__main__":
    main()
