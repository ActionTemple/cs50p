

# Cookie Jar
# Andrew Waddington

class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size
        if capacity <= 0:
            raise ValueError("No cookies left")

    def __str__(self):
        return f"{self.size * "🍪"}"


    def deposit(self, n):

        self.size += n
        if self.size > self.capacity:
            raise ValueError("Jar is full")

    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError("Jar is empty")

@property
def capacity(self):
    return self.capacity

@capacity.setter
def capacity(self, capacity):
    if self.capacity <= 0:
        raise ValueError("less than zero")
    self.capacity = capacity


@property
def size(self):
    return self.size

@size.setter
def size(self, n):
    self.size = n


jar = Jar()
jar2 = Jar()


def main():
    print (f"Cookie Jar: {jar}")
    jar.deposit(5)
    print (f"Cookie Jar: {jar}")
    #jar.withdraw(6)
    jar.withdraw(3)
    print (f"Cookie Jar: {jar}")
    jar.deposit (6)
    print (f"Cookie Jar Capacity: {jar.capacity}")
    print (f"Cookie Jar: {jar}")
    jar2.deposit(11)
    print (f"Cookie Jar 2: {jar2}")
    jar2.withdraw(4)
    print (f"Cookie Jar 2: {jar2}")
    jar2.deposit(1)
    print (f"Cookie Jar 2: {jar2}")
    #jar2.withdraw(14)
    #print (f"Cookie Jar 2: {jar2}")
    print (f"Cookie Jar 2 Capacity: {jar2.capacity}")


if __name__ == "__main__":
    main()
