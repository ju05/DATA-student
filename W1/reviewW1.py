# Sequences and collections in python
# Organizing, storing and retrieving data

# List
# USE Cases: store and organize data that can be changed, order by index "flexible" collection
# creating a list = [] squared brackets
# methods
# append()
# extend()
# remove()
# pop()
# sort()

# methods that create a new list
# sorted()
# split()
# tasks = input("enter a task separated by coma: ")
# tasks_list = tasks.split()
# print(tasks_list)
#
# lis_1 = [1, 2, 3, 4]
# lis_2 = [4, 6, 7]
#
# list_3 = [*lis_1, *lis_2]
# print(list_3)

# TUPLES
# useful if you want to store information that shouldn't be change

# cordinates = (4, 6)
# x, y = cordinates
# print(x, y)
#
# addresses = ("Adress 1", "Adress 2", "Adress 2", "Adress 2")
# print(addresses.count("Adress 2"))

# SET
# USE cases: useful for data that you don't want to have dublicated

# fruits = {"A1", "A2", "A3"}
# vegetable = ["A6", "A2", "A5"]
#
# common = fruits.intersection(vegetable)
# print(common)


# DICTIONARIES
# # USE cases: when we need logical association between the data and the lable
# users = {"alice": {"age": 25, "email": "alice@example.com"},
#          "bob": {"age": 30, "email": "bob@example.com"}}
#
# users.update({"jon": {"age"}})
#

# position = input(f" enter the position (x y) or 'q': ")
# move = position.split()
# move = [int(move[0]), int(move[1])]
# print(move)

# players = {"Player1": "X", "Player2": "Y"}
# print(players["Player1"])

# table = []
# for x in range(3):
#     table.append([])
#     for y in range(3):
#         table[x].append("{")
# # print(len(''join.(table[0]))
# print(table)
# print(len(''.join(table[0])))
# print(len(''.join(table[0]).split()))

list_my = [["1","2","3"],["4","5","6"],["7","8","9"]]
print(''.join(''.join(list_my)))
# for horizontal in range(3):
#     print(list_my[-horizontal-1][horizontal])

# ''.join(list_my[0])
# list_my = ["1"," ","3"]
# print(list_my)
# print(''.join(list_my).replace(' ',''))

# print(''.join(''.join(list_my)))

# " ".join("".join(chars).split())