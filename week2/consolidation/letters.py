
def main():
    """
    print (write_letter("Mario", "Princess Peach"))
    print (write_letter("Luigi", "Princess Peach"))
    print (write_letter("Daisy", "Princess Peach"))
    print (write_letter("Yoshi", "Princess Peach"))
    """
    names = ["Mario", "Luigi", "Daisy", "Yoshi", "Bowser"]
    #for i in range(len(names)):
    for name in names:
        print(write_letter(name, "Princess Peach"))




def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to a ball at
        Peach's castle this evening at 7:00pm.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """


main()
