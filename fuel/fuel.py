
# Fuel Guage
# Andrew Waddington

from decimal import *
getcontext().prec = 2

def main():
    try:

        fuel_left = input("Fraction: ")

        x, y, z = fuel_left.partition("/")

        x1 = int(x)
        z1 = int(z)
       # print (x1)
       # print (y)
       # print (z1)
    except ValueError:
       # print("VE")
        main()
    while int(x1) > int(z1) > 0:
       # print("top heavy fraction")
        fuel_left = input("Fraction: ")
        x, y, z = fuel_left.partition("/")
        x1 = int(x)
        z1 = int(z)
    try:
        if y == ("/"):
                a = Decimal(x1/z1)
                #print (a)
                percentage = Decimal(a * 100)
                if percentage <= 1:
                    print ("E")
                elif percentage >= 99:
                    print ("F")
                else:
                    percentage = int(percentage)
                    a = ("%")

                    print (f"{percentage}" + (a))
    except ZeroDivisionError:
       # print("ZDE")
        main()


main()
