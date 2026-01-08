# class Parent:
#     def __init__(self):
#         pass
#
#     def speak(self):
#         print(f"Parent is speaking")
#
#
# class Child(Parent):
#     pass
#
#
# class Grandchild(Child):
#     pass
#
#
# obj1 = Child()
# obj1.speak()
#
# obj2 = Grandchild()
# obj2.speak()


class Animal:
    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs
        self.full_name = f"{name} {family}"


class Dog(Animal):
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs)
        self.trained = trained
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")

    def sleep(self):
        return f"{self.name} is sleeping too much"


class Cat(Animal):
    def __init__(self, name, family, legs, friendly, nick_name):
        super().__init__(name, family, legs)
        self.trained = friendly
        self.nick_name = nick_name

    def get_crazy(self):
        print(f"{self.name} is running with its {self.legs} in full power")


class Alien:
    def __init__(self, personal_name, planet):
        self.personal_name = personal_name
        self.planet = planet

    def fly(self):
        return f"{self.personal_name} is flying around"

    def sleep(self):
        return f"{self.personal_name} is sleeping"

    def make_sound(self):
        return f"{self.personal_name} is making a sound from Alien"


class AlienDog(Alien, Dog):
    def __init__(self, name, family, legs, personal_name, planet):
        Alien.__init__(self, personal_name, planet)
        Dog.__init__(self, name, family, legs)


"*******************************************************************************"

# lion = Animal('Lion', "Felidae", 4)
# print(lion.__dict__)

# dog_1 = Dog("Dog", "Canidae", 4)
# dog_1.bark()
# cat_1 = Cat("Cat 1", "Family Cat 1", 4)
# cat_1.get_crazy()

# aliendog = AlienDog(family="Dog 5", name="Family Dog 5", legs=4, personal_name="Rexi", planet="Saturn")
# # aliendog.bark()
# # print(aliendog.name, aliendog.family, aliendog.planet)
# print(aliendog.sleep())
#
# print(Dog.sleep(aliendog))

# cat_1 = Cat("Cat 1", "Family Cat 1", 4, True, "Cat nick name")
# print(cat_1.__dict__)


# add two other attributes specifically to the Dog class: trained (boolean), age (int)
# use the super().__init__() to do so
# create an instance of Dog after that and analyse what changed
dog_1 = Dog("Dog", "Canidae", 4, True, 10)
print(dog_1.__dict__)