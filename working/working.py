

# Working 9 to 5
# Andrew Waddington

import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError("ValueError"):
        sys.exit(1)




def convert(s):
    # tomorrow start again with a test file and build up the regular expression in small pieces starting with the first number, then :, then 24hr, AM/PM etc

    if " to " not in s:
        raise ValueError

    matches = re.search(r'^([0-9]|0[0-9]|1[0-2])(\:)?(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])?( AM| PM)?( to )([0-9]|0[0-9]|1[0-2])(\:)?(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])?( AM| PM)?$', s)
    if not matches:
        raise ValueError

    a, b, c, d, e, f, g, h, i = matches.groups()




    if d is None:
        d = " AM"
    if i is None:
        i = " AM"



    if len(a) == 1:
        a = (f"{int(a):02}")
    else:
        a = int(a)
    if len(f) == 1:
        f = (f"{int(f):02}")
    else:
        f = int(f)

    if d == (" PM"):
        if 0 < int(a) < 12:
            a = int(a) + 12
            #a = str(a)
        if a == 0:
            raise ValueError
    if i == (" PM"):
        if 0 < int(f) < 12:
            f = int(f) + 12
            #f = str(f)
        if f == 0:
            raise ValueError

    if d == (" AM"):
        if a == 12:
            a = 0
    if i == (" AM"):
        if f == 12:
            f = 0


    if b == None:
        b = (":")
    if c == None:
        c = 0
    if  g == None:
        g = (":")
    if h == None:
        h = 0



   # print (f"a {a}")
  #  print (f"b {b}")
  #  print (f"c {c}")
  #  print (f"d {d}")
  #  print (f"e {e}")
   # print (f"f {f}")
  #  print (f"g {g}")
  #  print (f"h {h}")
# print (f"i {i}")





    #s = (f"{a}{b}{c}{e}{f}{g}{h}")
    s = (f"{a:02}:{c:02} to {f:02}:{h:02}")


    return (s)



if __name__ == "__main__":
    main()
