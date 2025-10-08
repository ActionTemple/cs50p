def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check length
    if len(s) <2  or len (s) > 6:
        return False

    for c in (s[0:2]):    # Checks first two chars
        if c.isdigit():   # If either is a digit
            return False
    for c in (s[:6]):       #Checks for illegal characters
        if not c.isdigit() and not c.isalpha():
            return False
    digit_index = -1    # loop to check for first digit
    for i in range(len(s)):
        if s[i].isdigit():
            digit_index = i
            break

    if digit_index != -1:   # if we find a first digit make sure it is not zero
        if s[digit_index] == '0':
            return False

        for c in s[digit_index:]:   #Checks all chars after first digit are digits
            if not c.isdigit():
                return False







    return True

main()
