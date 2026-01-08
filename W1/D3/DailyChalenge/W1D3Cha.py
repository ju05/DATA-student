
# # Challenge 1: Letter Index Dictionary
# # Declare a variable and ask the user to input a word (string type).
# user_word = input("Please input the word: ")
# # Declair a new empty dictionary
# final_dict = {}
# # Create a loop to go through each character in the word and get its index.
#
# for i, char in enumerate(user_word):
#     # Check if the character is already in the dictionary.
#     if final_dict.get(char):
#         # If the character already exists, append the index to its list of positions.
#         final_dict[char].append(i)
#     else:
#         # If the character does not exist, create a new key-value pair where the value is a list containing the
#         # current index.
#         final_dict[char] = [i]
# print(final_dict)

# # Challenge 2: Affordable Items
# # Declare a new dictionary where keys are item names and values are their prices (both as strings).
# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# # Declare a new variable for the amount of money in our wallet (as a string).
# wallet = "$1"
# # Remove the dollar sign from the wallet string and convert it to an integer.
# money = int(wallet.replace("$", ""))
# # Declare a new list to store the names of items we can afford.
# list_name = []
#
# # Start a loop to go through each key-value pair in the dictionary using the .items() method.
# for name, cost in items_purchase.items():
#     # Convert the price string to an integer by removing any symbols (like $ or ,).
#     new_cost = int(cost.replace("$", "").replace(",", ""))
#     # Check if the current item is affordable by comparing its price to the remaining money.
#     if money >= new_cost:
#         # If the item is affordable, add it to the list and subtract its cost from the remaining money.
#         list_name.append(name)
#         money -= new_cost
# # Before printing, check if the list has any items. If so, print them sorted. Otherwise, print "Nothing".
# if list_name:
#     print(sorted(list_name))
# else:
#     print("Nothing")
