

def main():
    greeting = input("Greeting: ").lower().strip()

    print (f"${(value(greeting))}")

def value(greeting):


    if greeting.startswith("hello"):
        return int(0)
# check if first letter of the word starts with "h", and if so print $20
    elif greeting.startswith("h"):
        return int(20)
    else:
        return int(100)


if __name__ == "__main__":
    main()







