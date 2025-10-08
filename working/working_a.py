

# Working 9 to 5
# Andrew Waddington

import re
import sys


def main():
    #try:
    print(convert(input("Hours: ")))
    #except ValueError("VE"):
        #sys.exit()


def convert(s):
    # tomorrow start again with a test file and build up the regular expression in small pieces starting with the first number, then :, then 24hr, AM/PM etc


    if matches := re.search(r'^([0-9]|0[0-9]|1[0-2])(\:)?(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])?( AM| PM)?( to )([0-9]|0[0-9]|1[0-2])(\:)?(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])?( AM| PM)?$', s):

        a = matches.group(1)
        b = matches.group(2)
        c = matches.group(3)
        d = matches.group(4)
        e = matches.group(5)
        f = matches.group(6)
        g = matches.group(7)
        h = matches.group(8)
        i = matches.group(9)

    if not matches:
        raise ValueError("There is a Value Error")


    else:


        if len(a) == 1:
            a = (f"{int(a):02}")
        if len(f) == 1:
            f = (f"{int(f):02}")
        if d == (" PM"):
            if 0 < int(a) < 12:
                a = int(a) + 12
            if a == ("00"):
                raise ValueError
        if i == (" PM"):
            if 0 < int(f) < 12:
                f = int(f) + 12
            if f == ("00"):
                raise ValueError

        if d == (" AM"):
            if a == ("12"):
                a = ("00")
        if i == (" AM"):
            if f == ("12"):
                f = ("00")

        if i == (" AM"):
            if f == 12:
                f == ("00")
        if b == None:
            b = (":")
        if c == None:
            c = ("00")
        if  g == None:
            g = (":")
        if h == None:
            h = ("00")



   # print (f"a {a}")
  #  print (f"b {b}")
  #  print (f"c {c}")
  #  print (f"d {d}")
  #  print (f"e {e}")
   # print (f"f {f}")
  #  print (f"g {g}")
  #  print (f"h {h}")
# print (f"i {i}")





    s = (f"{a}{b}{c}{e}{f}{g}{h}")
    

    return (s)



if __name__ == "__main__":
    main()
