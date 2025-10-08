
# Lines
# Andrew Waddington

import sys


docstring = False
lines = int()

try:
    my_file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File Not Found")

if len(sys.argv) <2 :
    sys.exit("Not enough arguments")
elif len(sys.argv) >2:
    sys.exit("Too many arguments")

elif (sys.argv[1])[-2:] != "py":
    sys.exit("Not a python file")

else:
    for i in my_file:
        if docstring == True:
            continue
        elif i.strip() == str():
            continue
        #elif i.strip()== ("\n"):
            #continue
        elif i.lstrip().startswith("#"):
            continue
        elif "#" in i:
            lines +=1
            continue
#
#        elif '"""' in i or "'''" in i:
#            if '"""' in i:
#                doc = '"""'
#
#            else:
#                doc = "'''"
#            if not i.startswith(doc):
#                x, y, z = i.partition(doc)
#                if x.strip() != str():
#                    #print (x)
#                    lines += 1
#                    continue
#            if ";" in i:
#                x, y, z = i.partition(";")
#                print (f"First Z: {z.strip()}")
#                lines += 1
#                continue

#            if i.count(doc) % 2 == 0:
#                continue


#            else:
#                docstring = True
#
#            for i in my_file:
#                if '"""' in i or "'''" in i:
#                    docstring = False
#                    if ";" in i:
#                        x, y, z = i.partition(";")
#                        print (f"Second Z: {z.strip()}")
#                        lines += 1
#                    break


        else:
            if i.strip() != str():
                lines += 1


print (lines)

