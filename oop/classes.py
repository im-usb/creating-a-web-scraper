class Puppy:  # class definition

    def __init__(self):  # constructor
        self.name = "Ruffus"  # instance attribute
        self.age = 2
        self.breed = "Poodle"


ruffus = Puppy()  # instance of the class Puppy

# accessing the attributes of the instance
print(ruffus.name, ruffus.age, ruffus.breed)
