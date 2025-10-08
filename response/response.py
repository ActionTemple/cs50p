

# Response Validator
# Andrew Waddington

import validators

def main():
    print(validate(input("Email: ").lower()))



def validate(a):

    match = validators.email(a)
    if match == True:

        return ("Valid")
    else:
        return ("Invalid")


if __name__ == "__main__":
    main()

