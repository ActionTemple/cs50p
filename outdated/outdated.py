

# Outdated
# Andrew Waddington

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():

    dd = (0)
    mm = (0)
    yyyy = (0)
    month = ""



    date = input("Date: ").strip()

    if "/" in date:
        #print (date)
        x, y, z = date.split('/')
        #print (y)
        dd = y
        mm = x
    else:
        for c in date:
            if not c.isalpha():
                continue
            else:
                month +=c


    mm = date[0:2]
    yyyy = date[-4:]
    dd = date[-7:-5]
    d_d = date[-8:-5]
    if (dd.strip(',')).isalpha():
        main()

    elif not mm.isalpha():
        mm1 = int(mm.strip('/'))
        dd1 = int(dd.strip('/'))
        if mm1 < 13 and dd1 < 32:
            print(f"{yyyy}-{mm1:02}-{dd1:02}")
        else:
            main()
    else:
        comma = date[-6:-5]
        if comma != (','):
            main()
        else:
            month_b = (months.index(month.title()))
            month_c = int(month_b + 1)
            ddd = int(d_d.strip(','))
            if ddd < 32:
                print(f"{yyyy}-{month_c:02}-{ddd:02}")
            else:
                main()


main()
