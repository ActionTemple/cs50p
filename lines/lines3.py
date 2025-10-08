# Lines
# Andrew Waddington

import sys



total = int()
comments = int()
docstrings = int()
whitespace = int()
codelines = int()
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

        for j in i:
            if j == "#":

                break
            elif '"""' in i or "'''" in i:
                for c in my_file:
                    if '"""' in i or "'''" in i:
                        break
                    else:
                        for n in my_file:
                            if n.strip() != str():
                                lines += 1




"""

my_file.seek(0)
for n in my_file:
    if n.lstrip() != str():
        codelines += 1


my_file.seek(0)
for p in my_file:
    if p.strip() == str():
        whitespace += 1

my_file.seek(0)
for g in my_file:
    total +=1

my_file.seek(0)
for _ in my_file:
"""
 #   if '"""' in _ or "'''" in _:
  #      for c in my_file:
   #         if '"""' in _ or "'''" in _:
    #            docstrings +=1
#lines = (total - comments - docstrings - whitespace)
"""
print(f"Codelines: {codelines}")
print(f"Docstrings: {docstrings}")
print(f"Whitespace: {whitespace}")
print(f"Comments: {comments}")
print(f"Total: {total}")
"""
print (lines)
