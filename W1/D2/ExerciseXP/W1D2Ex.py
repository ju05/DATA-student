# Exercise 1: Favorite Numbers

# my_fav_numbers = {1, 3, 5, 7}
# print(my_fav_numbers)
# my_fav_numbers.add(4)
# my_fav_numbers.add(6)
# print(my_fav_numbers)
# my_fav_numbers.remove(6)
# print(my_fav_numbers)
# friend_fav_numbers = {2,3,4}
# our_fav_numbers = my_fav_numbers.intersection(friend_fav_numbers)
# print(our_fav_numbers)

# Exercise 2: Tuple

# tuple_test = (1, 2, 3)
# print(tuple_test)
# print(type(tuple_test))
# tuple_test = tuple_test + tuple(4, 5)

# Exercise 3: List Manipulation

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# print(basket)
# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# print(basket)
# basket.append("Kiwi")
# print(basket)
# basket.insert(0, "Apples")
# print(basket)
# x = basket.count("Apples")
# print(x)
# basket.clear()
# print(basket)

# Exercise 4: Floats

# new_list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# print(type(new_list))
# print(new_list)
#
# new_list.clear()
# print(new_list)
# a = 1.5
# b = 2
# for num in range(8):
#     if num%2 == 0:
#         new_list.append(a)
#         a += 1
#     else:
#         new_list.append(b)
#         b += 1
# print(new_list)

# Exercise 5: For Loop

# for num in range(1, 20 + 1):
#     print(num)
# for num in range(1 + 1, 20 + 1, 2):
#     print(num)

# Exercise 6: While Loop

# input_name = ""
# while input_name.upper() != "ILIA":
#     input_name = input("Please guess my name or press 'q' to exit ")
#     if input_name == "q":
#         break

# Exercise 7: Favorite Fruits

# user_fruit = input("Input your favorite fruits (you can input several fruits, separated by spaces): ")
# print(user_fruit)
# list_fruit = user_fruit.split()
# print(list_fruit)
# new_request = input("What fruit would you want: ")
# if new_request in list_fruit:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8: Pizza Toppings

# inter_topping = input("Add topping or type 'quit' to exit: ")
# list_toppings = []
# base_pizza = 10.00
#
# while inter_topping != "quit":
#     list_toppings.append(inter_topping)
#     print(f"Adding {inter_topping} to your pizza.")
#     base_pizza += 2.50
#     inter_topping = input("Add topping or type 'quit' to exit: ")
#
# if len(list_toppings)>0:
#     print("Your list of toppings is:")
#     for topping in list_toppings:
#         print(topping)
# else:
#     print("You don't have any toppings.")
#
# print(f"Your pizza cost: {base_pizza}$")

# Exercise 9: Cinemax Tickets

# person_age = ""
# person_list = []
# a = 0
# while person_age != "q":
#     person_age = input("Please insert age one of the person or 'q' for exit: ")
#     if person_age.isnumeric():
#         if int(person_age) > 12:
#             a += 15
#             if int(person_age) >= 16 and int(person_age) <= 21: # bonus part
#                 person_list.append(person_age)
#         elif int(person_age) > 3:
#             a += 10
#     elif person_age == "q":
#         break
#     else:
#         print("Please insert only age")
# print(f"Total price is {a}$")
# print(f"Final list allowed person {', '.join(person_list)}") # bonus part

# Exercise 10: Sandwich Orders

# sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
# finished_sandwiches = []
#
# while "Pastrami" in sandwich_orders:
#     x = sandwich_orders.index("Pastrami")
#     del sandwich_orders[x]
#
# for name in sandwich_orders:
#     finished_sandwiches.append(name)
#     print(f"I made your {name} sandwich.")
#
# print("Final list of sandwiches:\n" + '\n'.join(finished_sandwiches))
