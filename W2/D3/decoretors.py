import math
from datetime import datetime, date


class Person:

    def __init__(self, name, last_name, birthdate):
        self.name = self.upper_first_letter(name)
        self.last_name = self.upper_first_letter(last_name)
        self.birthdate = self.parse_birthday(birthdate)

    @classmethod
    def from_age(cls, name, last_name, age):
        current_year = datetime.today().year
        birth_year = current_year - age
        birth_date = f"{birth_year}-01-01"
        return cls(name, last_name, birth_date)

    @staticmethod
    def parse_birthday(date_string):
        return datetime.strptime(date_string, "%Y-%M-%d").date()

    @staticmethod
    def upper_first_letter(all_names):
        return all_names.title()

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        return age

    def __str__(self):
        return f"{self.name} {self.last_name} was burned on {self.birthdate}, \nage {self.age}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


p1 = Person("alICe", "woNDer", "1990-02-05")
# print(p1)
# print(repr(p1))
# print(Person.upper_first_letter("ghkjkj"))
#
# print(p1.name)
# print(p1.last_name)
#
# print(type(p1.birthdate))
#
# print(p1.age)
#
p2 = Person.from_age("Bob", "Smith", 36)
# print(p2.birthdate)
# print(datetime.today().year)


print(p1 == p2)

print(p1 < p2)