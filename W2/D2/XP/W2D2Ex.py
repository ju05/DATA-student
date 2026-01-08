# Exercise 1: Pets
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class BengalCat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)


class ChartreuxCat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)


class SiameseCat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)


bengal_obj = BengalCat("Cat 1", 1)
chartreux_obj = ChartreuxCat("Cat 2", 2)
siamese_obj = SiameseCat("Cat 3", 3)
all_cats = [bengal_obj, chartreux_obj, siamese_obj]
sara_pets = Pets(all_cats)
sara_pets.walk()

# Exercise 2: Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight/self.age*18

    def fight(self, other_dog):
        if other_dog.run_speed()*other_dog.weight < self.run_speed()*self.weight:
            return self.name
        elif other_dog.run_speed()*other_dog.weight > self.run_speed()*self.weight:
            return other_dog.name
        else:
            return "Tie"


dog_1 = Dog("Dog 1", 1, 1)
dog_2 = Dog("Dog 2", 3, 2)
dog_3 = Dog("Dog 3", 4, 3)
print(dog_1.bark())
print(dog_2.run_speed())
print(dog_3.fight(dog_2))


# Exercise 4: Family and Person Classes
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        if self.age < 18:
            return False
        else:
            return True


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends.")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")

    def family_presentation(self):
        print(f"{self.last_name}")
        for member in self.members:
            print(f"{member.first_name} {member.age}")


spektor = Family("Spektor")
print(spektor.__dict__)
spektor.born("Ilia", 20)
spektor.born("Anna", 10)
spektor.born("Anton", 30)
spektor.check_majority("Ilia")
spektor.family_presentation()
