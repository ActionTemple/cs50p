
# Watch on YouTube
# Andrew Waddington


import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):

    if matches := re.search(r'^(<iframe)( src="https?://)?(www\.)?(youtube\.com/embed/)(.*)(">)(</iframe>)$', s, re.IGNORECASE):
        return (f"https://youtu.be/{matches.group(5)}")

if __name__ == "__main__":
    main()


 