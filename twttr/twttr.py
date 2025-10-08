
# Just setting up my twttr
# Andrew Waddington

def main():
    a = input("Input: ")
    removevowels (a)

def removevowels(a):
    vowels = {"a", "e", "i", "o", "u"}
    d = ""
    for c in a:
        if c.lower() not in vowels:
            d += c

    print("Output: ", d, end="")
    print ()


main ()
