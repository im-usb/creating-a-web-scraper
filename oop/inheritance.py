class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        # return a string
        return f"{self.name} is a {self.breed} and is {self.age} years old."

    def sleep(self):
        return "Zzzz!"


class GuardDog(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)  # call the __init__ method of the parent class
        self.aggressive = True

    def grumble(self):
        return "Grrrrr!"


class Puppy(Dog):  # class definition
    def __init__(self, name, breed, age):
        super().__init__(name, breed, 0.1)  # call the __init__ method of the parent class
        self.spoiled = True  # instance attribute
    # __str__ method, a special method used to define a human-readable string representation of an object.

    def __str__(self):
        # return a string
        return f"{self.name} is a {self.breed} and is {self.age} years old."

    def bark(self):
        return "Woof! Woof!"

    def introduce(self):
        return f"{self.bark()}! I am {self.name}. I am a {self.breed} and I am {self.age} years old."


# instance of the class Puppy
ruffus = Puppy(name="ruffus", breed="poodle", age=0.1)
# instance of the class Puppy
rocky = GuardDog(name="rocky", breed="beagle", age=2)

# Woof! Woof! I am ruffus. I am a poodle and I am 2 years old.
print(ruffus.introduce())
print(rocky.grumble())

print(ruffus)  # __str__ method is called
print(rocky)  # __str__ method is called
print(ruffus.sleep())
print(rocky.sleep())
