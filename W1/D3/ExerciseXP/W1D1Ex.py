# Exercise 1: Converting Lists into Dictionaries
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# new_dict = {}
# for key, value in zip(keys, values):
#     new_dict[key] = value
#
# print(new_dict)

# Exercise 2: Cinemax #2 with Bonus part
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# ticket_sum = 0
# y_or_n = input("Do you want to insert the data? Y?")
# if y_or_n.upper() == "Y":
#     insert_name = ""
#     insert_age = ""
#     family.clear()
#     while insert_name != "q":
#         insert_name = input("Please input Name or 'q' for exit: ")
#         if insert_name == "q":
#             break
#         insert_age = input("Please input age or 'q' for exit: ")
#         if insert_age.isnumeric():
#             family[insert_name] = int(insert_age)
#         elif insert_age == "q":
#             break
#         else:
#             print("You should input age as a number! Try again.")
# for member in family:
#     if family[member] > 12:
#         ticket_sum += 15
#         print(f"Ticket for {member} cost 15$")
#     elif family[member] >= 3:
#         ticket_sum += 10
#         print(f"Ticket for {member} cost 10$")
#     else:
#         print(f"Ticket for {member} is free")
#
# print(f"Total cost is {ticket_sum}$")

# Exercise 3: Zara
# brand = [
#     {
#         "name": "Zara",
#         "creation_date": 1975,
#         "creator_name": "Amancio Ortega Gaona",
#         "type_of_clothes": ["men", "women", "children", "home"],
#         "international_competitors": ["Gap", "H&M", "Benetton"],
#         "number_stores": 7000,
#         "major_color":{
#             "France": ["blue"],
#             "Spain": ["red"],
#             "US": ["pink", "green"]
#         }
#     }
#
# ]
#
# # Change the value of number_stores to 2.
# brand[0]["number_stores"] = 2
# # Print a sentence describing Zara’s clients using the type_of_clothes key.
# print(f"Zara's clients are: {', '.join(brand[0]['type_of_clothes'])}")
# # Add a new key country_creation with the value Spain.
# brand[0]["country_creation"] = "Spain"
# # Check if international_competitors exists and, if so, add “Desigual” to the list.
# if brand[0]["international_competitors"]:
#     brand[0]["international_competitors"].append("Desigual")
# # Delete the creation_date key.
# del brand[0]["creation_date"]
# # Print the last item in international_competitors.
# print(brand[0]["international_competitors"][-1])
# # Print the major colors in the US.
# print(brand[0]["major_color"]["US"])
# # Print the number of keys in the dictionary.
# print(len(brand[0].keys()))
# # Print all keys of the dictionary.
# print(brand[0].keys())
#
# # Bonus
# more_on_zara = {
#     "creation_date": 1990,
#     "number_stores": 20
# }
# brand[0].update(more_on_zara)

# Exercise 4: Disney Characters
# 1. Create a dictionary that maps characters to their indices:
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# result_dict = {}
# for user in users:
#     result_dict[user] = users.index(user)
# print(result_dict)
# 2. Create a dictionary that maps indices to characters:
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# result_dict = {}
# for user in users:
#     result_dict[users.index(user)] = user
# print(result_dict)
# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# users.sort()
# result_dict = {}
# for user in users:
#     result_dict[user] = users.index(user)
# print(result_dict)
