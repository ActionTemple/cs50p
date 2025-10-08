

# Frank, Ian, and Glen's letters

# Andrew Waddington

import sys
import random
from pyfiglet import Figlet

legal_commands = [
    '--version',
    '-h', '--help',
    '-f', '--font=',
    '-D', '--direction=',
    '-j', '--justify='

]



figlet = Figlet()
font_list = figlet.getFonts()

for lc in legal_commands:
    if not sys.argv[1] in legal_commands:
        sys.exit("Invalid Usage 1")

for fl in font_list:
    if not sys.argv[2] in font_list:
        sys.exit("Invalid usage 2")

if len(sys.argv) <3:
    sys.exit("Invalid usage 3")

my_string = input("Input: ")


f = Figlet(font=sys.argv[2])


print(f"Output: \n \n, {f.renderText(my_string)}")
