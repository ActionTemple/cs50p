# camelCase
# Andrew Waddington

def main():
    a = input("camelCase: ").strip()

    convert(a)


def convert(a):
    d = ""
    for c in a:
        if c.islower():
            d += c
        else:
            d += ("_" + c.lower())
    print ("snake_case:", d.replace(" ", ""), end="")
    print ()

main()
