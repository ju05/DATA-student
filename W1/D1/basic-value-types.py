# basic value type

# string: is a sequence of chars that represents text in python

# "Hello Python"

# string methods
# print("hello python".capitalize())
# print("hello python".upper())
# print("HELLO PYTHON".lower())

# print("Goodnight moon".replace("moon", "Honey"))

# 3 snrings: SEQUENCE of chars: IT ALLOW US TO USE INDEXES (POSITIONS)

# gretings = "Hello python"
# print(gretings[6:12]) #slicing a string
# print(gretings[2])

# description = "strings are..."
# print(description.upper())
# print(description.replace("are", "is"))
# print(description[0:7])

# numbers: INTEGER, FLOAT, COMPLEX

# a = 5 #int
# b = 2.7 #float
# c = 5 + 3
# print(11//3) #floor division
# print(11%3) #modulus division
#
# print(round(10/3,2))

#TYPE CUSTING
# my_age = 35
# print("Hello, my name is, I am " + str(my_age) + " years old")
#
# price = "150"
#
# result = int(price) + 5
# print(result)

# user_name = input("What is your name? ")
#
# print(user_name)
#
# user_age = int(input("What is your age? "))
# print(user_age + 50)

# BOOLENS: True or False values
# COMPARISON OPERATORS

# print(3 > 4)
# print(3 < 4)
# print(3 <= 4)

#COMPARISON KEY WORDS
# print("JS" is "Python")
# print("Python" is "Python")
# print("Python" is not "Python")

# a = 350
# b = 350
# c = a
#
# print(a == b)
# print(a is b)
# print(a is c)
# print(id(a))
# print(id(b))


bank_balance = '33000'
phone_number = 532287514
#
# print(type(int(bank_balance)))
# print(type(str(phone_number)))



#STRING FORMATING
print(f"Your bank balance is {bank_balance} therefore you can take a loan")
name = "Ilia"
age = 34
# message = "My name is {}, I am {} years old".format(name, age)
# print(message)

if age == 35:
    print(age)
else:print((name))

user_name = "ilia"
welcom_message = f"{user_name}, welcom"
print(welcom_message)

user_name += " my name"
print(user_name)


#VARIBLES: NAMING
my_adress = "Ashkelon"
