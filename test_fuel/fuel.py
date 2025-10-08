
# Fuel Guage
# Andrew Waddington

from decimal import *
getcontext().prec = 2

def main():
    fraction = input("Fraction: ")
    convert(fraction)

    print (percentage)
    percentage = gauge(percentage)
    #print (convert(fraction))
    #print (f"{gauge.percentage()}" + (a))

def convert(fraction):
    x, y, z = fraction.partition("/")
    x1 = int(x)
    z1 = int(z)
    #print (x1)
    #print (y)
    #print (z1)
    if y == ("/"):
        a = Decimal(x1/z1)
        percentage = Decimal(a * 100)
        return percentage


def gauge(percentage):
    if percentage <= 1:
        print ("E")
    elif percentage >= 99:
        print ("F")
    else:
        percentage = int(percentage)
        a = ("%")

        return percentage


if __name__ == "__main__":
    main()
