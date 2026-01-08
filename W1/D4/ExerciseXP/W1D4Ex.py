# Exercise 1: What Are You Learning?
# def display_message():
#     print("I am learning about functions in Python.")
#
#
# display_message()

# Exercise 2: What’s Your Favorite Book?
# def favorite_book(title):
#     print(f"One of my favorite books is '{title}'.")
#
#
# favorite_book("Alice in Wonderland")

# Exercise 3: Some Geography
# def describe_city(city, country = "Unknown"):
#     print(f"{city} is in {country}")
#
#
# describe_city("Reykjavik", "Iceland")
# describe_city("Paris")

# Exercise 4: Random
# import random
#
#
# def random_number(user_number):
#     a = random.randint(1, 100)
#     if user_number == a:
#         print("Success!")
#     else:
#         print(f"Fail! Your number: {user_number}, Random number: {a}")
#
#
# random_number(50)

# Exercise 5: Let’s Create Some Personalized Shirts! ok
# def make_shirt(size="large", text="I love Python"):
#     print(f"The size of the shirt is {size} and the text is {text}.")
#
#
# make_shirt("large")
# make_shirt("medium ")
# make_shirt("small", "Custom message")
# make_shirt(size="small", text="Hello!")

# Exercise 6: Magicians…
# def show_magicians(magician_name):
#     for name in magician_name:
#         print(name)
#
#
# def make_great():
#     global magician_names
#     for i, name in enumerate(magician_names):
#         magician_names[i] = f"{name} the Greate"
#
#
# magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]
#
# make_great()
# show_magicians(magician_names)

# Exercise 7: Temperature Advice
import random


#
#
# def get_random_temp():
#     return random.randint(-10, 40)
#
# def main():
#     a = get_random_temp()
#     print(f"The temperature right now is {a} degrees Celsius.")
#     if a<0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     elif 0 <= a < 16:
#         print("Quite chilly! Don’t forget your coat.")
#     elif 16 <= a < 23:
#         print("Nice weather.")
#     elif 23 < a <= 32:
#         print("A bit warm, stay hydrated.")
#     elif 32 < a <= 40:
#         print("It’s really hot! Stay cool.")
# main()

# Bonus - Step 4: Floating-Point Temperatures (Bonus)
# def get_random_temp():
#     return random.uniform(-10, 40)
#
# def main():
#     a = get_random_temp()
#     print(f"The temperature right now is {a} degrees Celsius.")
#     if a<0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     elif 0 <= a < 16:
#         print("Quite chilly! Don’t forget your coat.")
#     elif 16 <= a < 23:
#         print("Nice weather.")
#     elif 23 < a <= 32:
#         print("A bit warm, stay hydrated.")
#     elif 32 < a <= 40:
#         print("It’s really hot! Stay cool.")
# main()

# Bonus - Month-Based Seasons (Bonus)
# def get_random_temp(main_seson):
#     if main_seson == 1:
#         return random.uniform(0, 20)
#     elif main_seson == 2:
#         return random.uniform(20, 40)
#     elif main_seson == 3:
#         return random.uniform(0, 20)
#     elif main_seson == 4:
#         return random.uniform(-10, 0)
#
#
# def main(seson):
#     a = get_random_temp(seson)
#     print(f"The temperature right now is {a} degrees Celsius.")
#     if a < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     elif 0 <= a < 16:
#         print("Quite chilly! Don’t forget your coat.")
#     elif 16 <= a < 23:
#         print("Nice weather.")
#     elif 23 < a <= 32:
#         print("A bit warm, stay hydrated.")
#     elif 32 < a <= 40:
#         print("It’s really hot! Stay cool.")
#
#
# def month_determ():
#     month = input("Input a month as number between 1 and 12: ")
#     if month.isnumeric():
#         month = int(month)
#         if month > 12:
#             print("This month doesn't exist!")
#             return 0
#         elif 3 <= month <= 5:
#             return 1
#         elif 6 <= month <= 8:
#             return 2
#         elif 9 <= month <= 11:
#             return 3
#         else:
#             return 4
#     else:
#         print("Sorry you don't input number!")
#         return 0
#
#
# a = month_determ()
# if a != 0:
#     main(a)
