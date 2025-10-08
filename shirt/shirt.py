

# CS50 P-Shirt
# Andrew Waddington
import sys
from PIL import Image
from PIL import ImageOps


def main():

    try:
        filename = sys.argv[1]
        outfile = sys.argv[2]
        d, e, f = outfile.partition(".")
        a, b, c = filename.partition(".")
        if c != f:
            sys.exit("Extensions do not match")
        with Image.open(sys.argv[1]) as img:
            img = ImageOps.fit(img, (600, 600))
            img.save(f"{a}.png")
            shirt = Image.open("shirt.png")

            shirt = ImageOps.fit(shirt, (600, 600))
            img.paste(shirt, (0, 0), mask=shirt)
            img.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File Not Found")


if len(sys.argv) <3:
    sys.exit("Not enough arguments")
elif len(sys.argv) >3:
    sys.exit("Too many arguments")



main()
