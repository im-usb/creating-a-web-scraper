class Puppy:  # class definition
    # __init__ method, a special method called when an instance (object) of a class is created. Allows the class to initialize the attributes of the object.
    def __init__(self, name, breed, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute
        self.breed = breed  # instance attribute

    # __str__ method, a special method used to define a human-readable string representation of an object.
    def __str__(self):
        # return a string
        return f"{self.name} is a {self.breed} and is {self.age} years old."


# instance of the class Puppy
ruffus = Puppy(name="ruffus", breed="poodle", age=2)
# instance of the class Puppy
rocky = Puppy(name="rocky", breed="beagle", age=2)

# accessing the attributes of the instance
print(ruffus.name, ruffus.age, ruffus.breed)
# accessing the attributes of the instance
print(rocky.name, rocky.age, rocky.breed)

print(ruffus)  # __str__ method is called
print(rocky)  # __str__ method is called
