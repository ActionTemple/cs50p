

# Bank
# Andrew Waddington
# Test commit from VS code

greeting = input("Greeting: ").lower().strip()

if greeting.startswith("hello"):
    print ("$0")

# check if first letter of the word starts with "h", and if so print $20
elif greeting.startswith("h"):
    print ("$20")
else:
    print ("$100")

