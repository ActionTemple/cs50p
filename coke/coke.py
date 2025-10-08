

# Coke Machine
# Andrew Waddington

def printer():
    if result >0:
        print ("Amount Due:", (result))
    else:
        print ("Change Owed:", abs(result))

y = 50
z = 0
result = y

while z <50:

    x = int(input("Insert Coin: "))

    if x == 50:
        z += 50
        result = y - z

    elif x == 25:
        z += 25
        result = y - z

    elif x == 10:
        z += 10
        result = y - z

    elif x == 5:
        z += 5
        result = y - z
    printer()

