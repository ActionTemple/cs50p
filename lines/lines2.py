
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
        elif i.lstrip().startswith("#"):
            continue

        elif '"""' in i or "'''" in i:
            if '"""' in i:
                doc = '"""'
            else:
                doc = "'''"
            if i.count(doc) % 2 == 0:
                #continue
                if not i.lstrip().startswith(("'''",'"""')):
                    lines +=1
                    continue
                continue
            else:
                docstring = True
            for i in my_file:
                if '"""' in i or "'''" in i:
                    docstring = False
                    break


        else:
            if i.strip() != str():
                lines += 1

#my_file.seek(0)
#for n in my_file:
#    if '"""' in n or "'''" in n:
#        if not n.startswith(("'''",'"""')):
#            lines +=1


print (lines)
