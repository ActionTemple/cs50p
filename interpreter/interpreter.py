

# interpreter
# Andrew Waddington

def printer():
    print (a)

expression = input("Expression: ")


x, y, z = expression.split(" ")


if y == ("+"):
    a = float(x) + float(z)


elif y ==("-"):
    a = float(x) - float(z)


elif y ==("*"):
    a = float(x) * float(z)


elif y==("/"):
    a = float(x) / float(z)


printer ()
