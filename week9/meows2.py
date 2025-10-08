

class Cat:
    MEOWS = 3 #capitalisation is intended to show a constant. Not enforced by Python

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()
