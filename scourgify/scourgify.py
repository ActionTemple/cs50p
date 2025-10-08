

# Scourgify
# Andrew Waddington

import sys
import csv


try:
    with open(sys.argv[1]) as my_file:
        myFile = my_file.readlines()[1:]
        with open((sys.argv[2]), 'w', newline="") as my_CSV:

            write = csv.writer(my_CSV, quoting=csv.QUOTE_NONE, quotechar=None, escapechar=" ")
            write.writerow(["first", "last", "house"])
            for row in myFile:

                a, b, c = row.partition(",")
                a = a.lstrip('"')
                d, e, f = c.partition(",")
                d = d.rstrip('"')
                d = d.lstrip()
                f = f.rstrip("\n")
                output_row = [d, a, f]
                write.writerow(output_row)
                continue


except FileNotFoundError:
    sys.exit("File Not Found")

if len(sys.argv) <3:
    sys.exit("Not enough arguments")
elif len(sys.argv) >3:
    sys.exit("Too many arguments")

elif (sys.argv[1])[-3:] != "csv":
    sys.exit("Not a CSV file")
