import sys
import random

# Guessing game
# Andrew Waddington

def main():
    n = ()

    try:
        n = int(input("Level: "))
        x = random.randint(1, n)
    except ValueError or KeyError:
        main()
    if int(n) <0:
        main()

    try:
        guess = int(input("Guess: "))
    except ValueError or KeyError:
        main()
   # print (guess)
    #print (x)

    if x == guess:
        print ("Just right!")
        sys.exit
    elif x > guess:
        print ("Too small!")
        main()
    else:
        if x < guess:
            print ("Too large!")
            main()

    sys.exit()

main()
