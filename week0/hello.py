
def hello ():
    print (f"Hello, {first}")


name =input ("What's your name? ").strip().title()
#name = name.strip().title()
#name = name.capitalize()
#name = name.title()
#name = name.title().strip()

first, last = name.split()
#print (f"Hello, {first}")
hello ()



