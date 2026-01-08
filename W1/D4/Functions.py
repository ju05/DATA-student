# Functions
# Syntax

# def func_name():
#     """Describe what this function does"""  # doc strings
#     print("I am a function")
#
# func_name()
# print(func_name.__doc__)

# create a function called greetings that prints "hello" in our mother tongue
#
# def greetings(language = "SP", name = "Pupkin"):
#     """This function greet you in Russian"""
#     if language == "PT":
#         print(f"Ola {name}")
#     elif language == "RU":
#         print(f"Привет {name}")
#     elif language == "SP":
#         print(f"Hi {name}")
#     else:
#         print(f"I don't know this language {name}")
#

# greetings("PT", "My")
# greetings("RU", "My")
# greetings("BL", "My")
# greetings("My")


# greetings(language="PT", name="My")
# greetings(language="PT")


# "Hello Sunshine".replace("Hello", "Lala")
#
#
# def country_info(city="Naboo"):
#     if city == "Moscow":
#         print(f"{city} is a capital of Russia")
#     else:
#         print(f"{city} is a planet from War Stars")
#
#
# city_1 = input("Your city is: ")
# country_info(city_1)
# country_info()
#
#
# def country_name(city="Naboo"):
#     if city == "Naboo"

# return keyword
#
# def calculation(num1, num2):
#     result = num1 + num2
#     return result
#
#
# # print(calculation(5, 4))
#
# sum1 = calculation(2, 5)
#
# print(sum1)

# countries = ["Brazil", "Israel", "China"]
#
# def contry_info(countries):
#     for country in countries:
#         if country == "Israel":
#             return country
#
# print(contry_info(countries))

# SCOPES
# Global scope: on the file, in general
# Local scope: idented block (if statement, a for loop, a function...)

#
# global_var = 100
# def calculation(a, b):
#     addition = a + b
#     substraction = a - b
#     # global_var = 50
#     global global_var
#     global_var = 70
#     return addition, substraction
#
#
# addition, substract = calculation(5, 7)
# # print(addition, substract)
# print(global_var)
#
#
# def decode_matrix_string(matrix_str: str) -> str:
#     matrix = [list(line) for line in matrix_str.strip().split('\n')]
#     max_cols = max(len(row) for row in matrix)
#     chars = []
#     for col in range(max_cols):
#         for row in range(len(matrix)):
#             if col < len(matrix[row]):
#                 char = matrix[row][col]
#                 chars.append(char if char.isalpha() else " ")
#     return " ".join("".join(chars).split())
#
#
# string = " \n     asdf \n 123 qwe 567 ghj"
# matrix = [list(line) for line in string.strip().split("\n")]
# print(matrix)


