

import inflect

p = inflect.engine()

items = []

while True:
    objects = input("Next: ")

    #objects = p.a(objects)
    items.append((objects))
    items = p.a(items)
    break

print(f"There is",(p.join(items)),"here.")
