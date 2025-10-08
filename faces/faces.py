


# Faces
# Andrew Waddington
# str.replace(old, new, count=-1)

def main():
    var1 = input("Say hello: ")
    output = convert(var1)
    print (output)

def convert(var1):
    firstpass = var1.replace(":)", "🙂")
    output = firstpass.replace(":(", "🙁")
    return output
main()
