

# Pizza Py
# Andrew Waddington

import sys
import csv
from tabulate import tabulate



try:
    with open(sys.argv[1]) as my_file:
        myFile = csv.DictReader(my_file)
        print(tabulate((myFile), tablefmt="grid", headers="keys"))


except FileNotFoundError:
    sys.exit("File Not Found")

if len(sys.argv) <2 :
    sys.exit("Not enough arguments")
elif len(sys.argv) >2:
    sys.exit("Too many arguments")

elif (sys.argv[1])[-3:] != "csv":
    sys.exit("Not a CSV file")



