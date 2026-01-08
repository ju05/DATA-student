# Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def get_amount(self, other_element):
        if isinstance(other_element, int):
            return other_element
        elif self.currency == other_element.currency:
            return other_element.amount
        else:
            raise TypeError("Cannot add between Currency type <dollar> and <shekel>")

    @staticmethod
    def plural_single(self):
        if self.amount == 1:
            return self.currency
        else:
            return self.currency + "s"

    def __str__(self):
        return f"{self.amount} {self.plural_single(self)}"

    def __repr__(self):
        return f"{self.amount} {self.plural_single(self)}"

    def __int__(self):
        return self.amount

    def __add__(self, another_amount):
        return self.amount + self.get_amount(another_amount)

    def __iadd__(self, another_amount):
        self.amount += self.get_amount(another_amount)
        return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 5)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
# print(c1+c3)

# Exercise 3: String module
import random
import string

all_letters = (string.ascii_lowercase + string.ascii_uppercase)
a = len(all_letters) - 1
new_str = []

for index in range(5):
    new_str.append(all_letters[random.randint(0, a)])
print(''.join(new_str))

# # Exercise 4: Current Date
from datetime import datetime


def corrent_date():
    return print(datetime.today().date())


corrent_date()

# Exercise 5: Amount of time left until January 1st
from datetime import datetime


def new_year_is():
    current_date = datetime.today()
    end_year = datetime.strptime(f"{current_date.year + 1}-01-01", "%Y-%M-%d")
    return print(end_year - current_date)

new_year_is()

# Exercise 6: Birthday and minutes
from datetime import datetime


def minutes_alife():
    birthday = input("Insert you birthday in format YYYY-MM-DD: ")
    birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
    return print(((datetime.today() - birthday_date).total_seconds()) / 60)


minutes_alife()

# Exercise 7: Faker Module
import faker


def generate_users(number):
    global users_list
    while len(users_list) != number:
        new_person = faker.Faker()
        new_user = {"name": new_person.name(),
                    "address": new_person.address(),
                    "language_code": new_person.language_code()}
        users_list.append(new_user.copy())
        new_user.clear()
    return users_list


users_list = []
print(generate_users(3))
