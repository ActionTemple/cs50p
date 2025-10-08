# Understanding Class Attributes and Methods

class Counter:
    def __init__(self, start_value=0):
        # This is the constructor - it runs when you create a new Counter object
        # The self.count is an "attribute" - it stores data in the object
        self.count = start_value

    def increment(self):
        # This method increases the counter by 1
        self.count += 1
        return self.count

    def decrement(self):
        # This method decreases the counter by 1
        self.count -= 1
        return self.count

    def doubler(self):
        self.count = self.count * 2
        return self.count

    def get_value(self):
        # This method just returns the current value
        return self.count

    def reset(self):
        # This method resets the counter to 0
        self.count = 0
        return self.count

# Let's demonstrate how this works
def counter_demo():
    # Create two separate counter objects
    counter1 = Counter()  # Starts at default value (0)
    counter2 = Counter(10)  # Starts at 10
    counter3 = Counter(100)

    print(f"Counter1 starts at: {counter1.get_value()}")
    print(f"Counter2 starts at: {counter2.get_value()}")
    print(f"Counter3 starts at: {counter3.get_value()}")

    # Increment counter1 three times
    print("\nIncrementing counter1 three times:")
    print(f"First increment: {counter1.increment()}")
    print(f"Second increment: {counter1.increment()}")
    print(f"Third increment: {counter1.increment()}")
    print(f"Let's increment our newest counter, counter3: {counter3.increment()}")

    # Decrement counter2 twice
    print("\nDecrementing counter2 twice:")
    print(f"First decrement: {counter2.decrement()}")
    print(f"Second decrement: {counter2.decrement()}")

    # Show that the counters are independent
    print("\nFinal values:")
    print(f"Counter1: {counter1.get_value()}")  # Should be 3
    print(f"Counter2: {counter2.get_value()}")  # Should be 8

    # Reset counter1
    print("\nResetting counter1:")
    counter1.reset()
    print(f"Counter1 after reset: {counter1.get_value()}")
    print(f"Counter2 is still: {counter2.get_value()}")
    print(f"Counter3 is now: {counter3.get_value()}")
    print(f"Let's double something. Let's double counter3 without altering any of the others: {counter3.doubler()}") # should be 202
# Run the demonstration
if __name__ == "__main__":
    counter_demo()
