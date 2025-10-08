

# Seasons of Love
# Andrew Waddington


import sys
import re
#from datetime import date
import datetime
import inflect


def main():
    try:
        birthday1 = (birthday(input("Date of Birth: ")))
    except ValueError: #("Invalid date"):
        sys.exit(1)

    todaysdate = datetime.date.today()

    x, y, z = birthday1.split("-")
    #print (todaysdate)
    #print (birthday1)

    birthday1a = datetime.date(int(x), int(y), int(z))
    seconds_in_your_life = todaysdate - birthday1a

    secs = (seconds_in_your_life.total_seconds())
    #secs = int(secs)
    mins = secs/60
    print (make_sentences(int(mins)))


def birthday(dob):
    matches = re.search(r'^([0-9][0-9][0-9][0-9])(\-)(0[0-9]|1[0-2])(\-)(0[0-9]|1[0-9]|2[0-9]|3[0-1])', dob)
    if not matches:
        raise ValueError
    a, b, c, d, e = matches.groups()

    a = int(a)
    c = int(c)
    e = int(e)

    if c == 2 and e > 28:
        raise ValueError
    if (c == 4 or c == 6 or c == 11) and e > 30:
        raise ValueError


    dob = f"{a}{b}{c:02}{d}{e:02}"

    return dob

def make_sentences(from_int):
    p = inflect.engine()
    count = from_int
    numbers_to_words = (p.number_to_words(count), p.plural_noun('minute'))
    numbers_to_words = str(numbers_to_words).replace('(', '').replace(')', '').replace("'", "")

    numbers_to_words = numbers_to_words[0].upper() + numbers_to_words[1:]
    numbers_to_words = numbers_to_words[0:-9] + numbers_to_words[-9:].replace(",", "")
    numbers_to_words = numbers_to_words.replace(" and", "")
    return numbers_to_words




if __name__ == "__main__":
    main()
