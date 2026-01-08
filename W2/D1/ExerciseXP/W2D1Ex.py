# Exercise 1: Cats
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_cat(self):
#         print(f"The oldest cat is {self.name}, and is {self.age} years old.")
#
#
# def finde_oldest_cat(*args):
#     a = -1
#     name_cat = ""
#     for cat in args:
#         if cat.age > a:
#             a = cat.age
#             name_cat = cat
#     return name_cat
#
#
# cat1 = Cat("Name 1", 4)
# cat2 = Cat("Name 2", 8)
# cat3 = Cat("Name 3", 12)
#
# finde_oldest_cat(cat1, cat2, cat3).print_cat()

# # Exercise 2 : Dogs
# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def bark(self):
#         print(f"{self.name} goes woof")
#         return self
#
#     def jump(self):
#         print(f"{self.name} jumps {self.height*2} cm high!")
#
#
# davids_dog = Dog("Dog1", 20)
# sarahs_dog = Dog("Dog2", 40)
#
# list_dog = [davids_dog, sarahs_dog]
#
# for dog in list_dog:
#     print(dog.name)
#     print(dog.height)
#
# for dog in list_dog:
#     dog.bark()
#     dog.jump()
#
# if list_dog[0].height > list_dog[1].height:
#     print(f"{list_dog[0].name} height than {list_dog[1].name}")
# elif list_dog[0].height == list_dog[1].height:
#     print(f"{list_dog[0].name} equal {list_dog[1].name}")
# else:
#     print(f"{list_dog[1].name} height than {list_dog[0].name}")

# # Exercise 3 : Who’s the song producer?
# class Song:
#     def __init__(self, lyrics=[]):
#         self.lyrics = lyrics
#
#     def sign_me_song(self):
#         for line in self.lyrics:
#             print(line)
#
#
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
#
# stairway.sign_me_song()

# Exercise 4 : Afternoon at the Zoo
class Zoo:
    def __init__(self, zoo_name, animals=[]):
        self.zoo_name = zoo_name
        self.animals = animals

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(' '.join(self.animals))

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        result_output = {}
        for name in sorted(self.animals):
            if name[0] in result_output.keys():
                result_output[name[0]].append(name)
            else:
                result_output.update({name[0]:[name]})
        return result_output

    def get_groups(self):
        for key, value in self.sort_animals().items():
            print(f"{key}: {value}")

#
# ramat_gan_safari = Zoo("ramat_gan_safari ", ['Cat', 'Cougar', 'Bear', 'Giraffe', 'Lion', 'Zebra'])
# ramat_gan_safari.get_animals()
# ramat_gan_safari.add_animal("Giraffe")
# ramat_gan_safari.add_animal("Bear")
# ramat_gan_safari.add_animal("Baboon")
# ramat_gan_safari.get_animals()
# ramat_gan_safari.sell_animal("Bear")
# ramat_gan_safari.get_animals()
# ramat_gan_safari.sort_animals()
# ramat_gan_safari.get_groups()