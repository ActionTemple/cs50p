

# Lesson 1: Your First Python Class - The Simplest Example

# Let's start with the most basic class possible
class Greeting:
    # This is a simple method that says hello
    def say_hello(self):
        print("Hello, world!")

# Quick Task 1: Create and Use the Class
def lesson_1_task():
    # Create an object (instance) of the Greeting class
    greeter = Greeting()

    # Call the method
    greeter.say_hello()

# Uncomment the line below to run the task
lesson_1_task()

# Reflection Questions:
# 1. What does 'self' mean in the method?
# 2. How is creating an object different from calling a function?
