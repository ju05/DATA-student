# OOP: OBJECT ORIENTED PROGRAMING

# What is an object?
# What is a class?

# How to create a class

class Dog:

    def __init__(self, name, color, breed, age):
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age

    # How to create methods of the clsass
    def bark(self):
        print(f"{self.name} is barking")

    def walk(self, metters = 100):
        print(f"{self.name} is walking {metters}")

    def birthday(self):
        self.age += 1
        return self

    def rename(self, name):
        self.name = name
        return self.name




# # An instance (or object) of class Dog is created:
# shelter_dog = Dog()
#
# # Creating attributes to the instance
# shelter_dog.color = "Black"
# print(shelter_dog.color)
# pitbull = Dog()
# print(pitbull.color)

# Creating the instances of Dog after creating
shelter_dog = Dog('Rex',"black","shelter", 5)
# print(shelter_dog.__dict__)

husky_dog = Dog('Naida',"grey","husky", 9)
# print(husky_dog.name, husky_dog.color, husky_dog.breed, husky_dog.age)

my_dogs = [shelter_dog, husky_dog]
# print(my_dogs)
#
# for dog in my_dogs:
#     print(dog.name)

# print(type(husky_dog))

# print(help(str))

my_dogs_objects = [obj for obj in globals().values() if isinstance(obj, Dog)]
print(my_dogs_objects)
#
# husky_dog.bark()
#
# for dog in my_dogs:
#     dog.bark()

# for dog in my_dogs:
#     dog.walk(30)

# print(shelter_dog.age)
# shelter_dog.birthday()
# print(shelter_dog.age)
# # shelter_dog.age += 1
# # print(shelter_dog.age)
#
# print(shelter_dog.name)
# shelter_dog.rename("New name")
# print(shelter_dog.name)
#
# a = shelter_dog.rename("Next name")
# print(a)