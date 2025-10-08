

def main():
    num = int(input("Number: "))
    

    num = add_five(num)
    print (f"+5: {num}")


    num = multiply_by_two(num)
    print (f"x2: {num}")


    num = subtract_three(num)
    print (f"-3: {num}")

def add_five(num):
    return num + 5



def multiply_by_two(num):
    return num * 2



def subtract_three(num):
    return num -3


main()
