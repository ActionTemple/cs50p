# Just setting up my twttr 2
# Andrew Waddington



def main():
    word = input("Input: ")
    shorten (word)
    print(f"Output: ", shorten (word), end="")
    print()

def shorten(word):
    vowels = {"a", "e", "i", "o", "u"}
    d = ""
    for c in word:
        if c.lower() not in vowels:
            d += c

    return d
    #print(f"Output: ", d, end="")
    #print()


if __name__ == "__main__":
    main()
