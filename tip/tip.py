# tip calculator
# Andrew Waddington

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    dtf = dollars.replace("$","")
    return float (dtf)

def percent_to_float(percent):
    ptf = percent.replace("%", "")
    ptf2 = float (ptf)
    percent1 = ptf2/100
    return (percent1)


main()
