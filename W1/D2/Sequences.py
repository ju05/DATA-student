# LISTS order sequence
#
# # A lists are sequence of elements
# # Syntax
some_list = list("Item 1") #to convert other sequence in a list
# other_list = ["Item 1"] #the best way to create an empty list
#
# print(some_list)
# print(other_list)
#
# print(len(some_list))
# print(len(other_list))
#
# print(some_list[1])
#
# # methods for list
# some_list.append("A")
# print(some_list)
#
# some_list.extend(["B","C","D"])
# print(some_list)

# names = []
# print(names)
# names.extend(["Ammy","Sheldon","leonard","Raj"])
# print(names)
#
# a=""
# names_mor = []
# for num in range(4):
#     a = input("Add name ")
#     names_mor.append(a)
# print(names_mor)

# print(list(range(1,8,2)))
# print(range(1,8,2))
#
# num_list = list(range(1,8))
# print(num_list[:6])
#
# copy_list = num_list
#
# print(copy_list)
# print(num_list)
#
# num_list.append("8")
# print(copy_list)
# print(num_list)

#other methods
# insert(where, what)
# remove(what) , removes  the first occurence of the element
# deleting some element

# print(num_list)
# del num_list[3]
# print(num_list)
#
# num_list.pop()
# print(num_list)
#
# poped_el = num_list.pop()
#
# print(poped_el)
# print(num_list)

# sorted()
# print(sorted(num_list))

# names = []
# print(names)
# names.extend(["Ammy","Sheldon","leonard","Raj"])
# print(sorted(names))
# print(names)

# sort()
# names = []
# print(names)
# names.extend(["Ammy","Sheldon","leonard","Raj"])
# print(names.sort())
# print(names)

# index(element) and it return you the index of this element

# Given this list:
# list1 = [5, 10, 15, 20, 25, 50, 20]
# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
#
# list1 = [20, 5, 10, 15, 20, 25, 50, 20]
# # print(list1)
# # x = list1.index(20)
# # del list1[x]
# # list1.insert(x,200)
# # print(list1)
#
# if list1.index(20) or list1.index(20) == 0:
#     index_found = list1.index(20)
#     list1.remove(20)
#     list1.insert(index_found, 200)
# print(list1)
#
# if 20 in list1:
#     index_found = list1.index(20)
#     list1.remove(20)
#     list1.insert(index_found, 200)
# print(list1)