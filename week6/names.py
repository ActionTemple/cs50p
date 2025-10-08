


name = input("What's your name? ")


with open("names.txt", "a") as file:
    file.write(f"{name}\n")
   






"""

names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"Hello, {name}")
"""
