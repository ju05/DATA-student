# shopping_list = ["milk","eggs","bread","eggs"]
# print(shopping_list)
# shopping_list.append("butters")
# print(shopping_list)
# shopping_list.remove("eggs")
# print(shopping_list[0])
# print(shopping_list)

# students = {"name": "John", "age": 20, "major": "Computer science"}
# print(students["age"])

# rick_dict = {
#     'first_name':'Rick',
#     'last_name':'Sanchez',
#     'first_name':'Rick1',
#     'last_name':'Sanchez1'
# }
#
# print(rick_dict)


# sample_dict = {
#    "class":{
#       "student":{
#          "name":"Mike",
#          "marks":{
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
#
# print(sample_dict["class"]["student"]["marks"]["history"])

# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# #
# # print(a_dict.items())
# # # output :
# # # dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])
# #
# # # The items() method returns a view object that displays
# # # a list of dictionary's (key, value) tuple pairs.
# #
# #
# for key, value in a_dict.items():
#     print(key, '->', value)

# output
# color -> blue
# fruit -> apple
# pet -> dog

#
# rick_dict = {
#     'first_name':'Rick',
#     'last_name':'Sanchez'
# }
# print(rick_dict)
#
# rick_dict["last_name"] = "San"
# print(rick_dict)
#
# shirts = [
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'S',
#     'price': 20
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'M',
#     'price': 25
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'L',
#     'price': 30
#   },
# ]
#
# for shirt in shirts:
# #     print(shirt)
#
# shirts = [
#   {
#     "name": "Awesome T-shirt 3000",
#     "size": "S",
#     "price": 20,
#     "pets": [("Refus", 9), ("Gafried", 8)],
#     "family":
#       {
#         "partner":
#           {
#             "first_name": "Liron",
#             "last_name": "Alon",
#             "age": 50
#           },
#         "chil":
#           {
#             "first_name": "Liron",
#             "last_name": "Alon",
#             "age": 50
#           }
#       }
#   }
# ]
#
#
# # print(shirts[0]["pets"][0][1])
# print(shirts[0][1])

# for pet in shirts[0]["pets"]:
#   print(pet[0])

# for family in shirts[0]["family"]:
#   print(shirts[0]["family"][family])
#

# user_a = {
#     'first_name': 'Bob',
#     'last_name': 'Ross', #STOP HERE, EXPLAIN
#     'age': 53, #EXPLAIN DATA TYPES AS VALUES
#     'address': 'Tel Aviv', #STOP HERE EXPLAIN ACESSING DATA
#     'hobbies': ['painting', 'guitar'], #STOP HERE EXPLAIN DATA TYPES: DICTS AND LISTS
#     'pets': [('Rufus', 9), ('Garfield', 8), ('Katty', 6)], #EXPLAIN LIST OF OTHER DATA TYPES (EX.:TUPPLES)
#     'family': {'partner':{
#         'first_name': 'Lior',
#         'last_name': 'Alon',
#         'age': 50
#         },
#         'sports': ['volleyball', 'soccer']
#         },
#     }
# }
# #print(user_a['first_name'])
# #print(user_a['hobbies'][1])
# #print(user_a['pets'][2][0])
#
# # for pet in user_a['pets']:
# #     print(pet[0])
#
# # print(user_a['family']['partner']['last_name'])
# # print(user_a['family']['children']['sports'][0])
# # print(user_a['family'])
#
#
# user_a['first_name'] = 'John'
#
# user_a['pets'][2][0] = 'Garfield_2'
#
# print(user_a)


# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
#
# }
# # sample_dict.update("name")
# # sample_dict.pop("name")
# # sample_dict.move_to_end("name")
# sample_dict['name2'] = sample_dict.pop('name')
#
# # sample_dict["name"] = "123"
# print(sample_dict)

# keys_to_remove = ["name", "salary"]


# print(sample_dict)
#
# for keys in keys_to_remove:
#     del sample_dict[keys]
#
# print(sample_dict)

new_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
print(new_str)
new_list = new_str.split(", ")
print(len(new_list))
new_list.sort(reverse=True)
print(new_list)