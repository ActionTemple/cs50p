
# Little Professor
# Andrew Waddington

import random


def main():
    numbers = []
    count = 0
    right_answers = 0
    level = get_level()

    while count < 10:
        X, Y = generate_integer(level)
        numbers.extend([X, Y])


        answer = X + Y
        count_b = 0

        while True:
            try:
                your_answer = int(input(f"{X} + {Y} = "))
                if your_answer == answer:
                    right_answers += 1
                    count += 1
                    break
                else:
                    print("EEE")
                    count_b += 1
                    if count_b == 3:
                        count += 1
                        print(f"{X} + {Y} = {answer}")
                        break
            except ValueError:
                continue


    print(f"{numbers}".replace("[", "").replace("]", "").replace(",", ""))

    print(f"Score: {right_answers}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            continue


def generate_integer(level):

    if level == 1:
        level = 9
        X = random.randint(0, level)
        Y = random.randint(0, level)
    elif level == 2:
        level = 99
        X = random.randint(10, level)
        Y = random.randint(10, level)
    else:  
        level = 999
        X = random.randint(100, level)
        Y = random.randint(100, level)

#    X = str(X).strip("(, )")
 #   Y = str(Y).strip("(, )")
 #   X = int(X)
 #   Y = int(Y)

    return X, Y



if __name__ == "__main__":
    main()
