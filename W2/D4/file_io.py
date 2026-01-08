# FILE I/O INPUT/OUTPUT
# import os.path
# import os
# dir_path = os.path.dirname(os.path.realpath(__file__))

# OLD SCHOOL WAY OF OPENING A FILE WITH PYTHON
#
# file_object = open(r"C:\Users\avdiz\OneDrive\Рабочий стол\Илья\Обучение\developers "
#                    r"institute\BooTcamp\DI-Bootcamp\W2\D4\secreets.txt")
# print(file_object.read())

# MODERN PYTHON WAY (AUTOMATICALLY CLOSED)

# with open(r"./starwars.txt", encoding= "utf-8") as file_obj:
    # print(file_obj.read())
    # output - file.obj.read() # returns the whole content of the file
    # output - file.obj.readline() # returns one line
    # output - file.obj.readlines() # returns a list where each line is an element
    # print(file_obj.read())
    # for line in range(5):
    #     print(line)
    #     print(file_obj.readline())
    # print(file_obj.readline())
    # print(file_obj.readlines()[5])

#     # WRITING on the file
# with open(f"{dir_path}/starwars.txt", "a+", encoding= "utf-8") as file_obj:
#     # we can define the mode :'w' to write and delete what in the file before
#     # 'a' to append a new line to the file
#     # nammes = ["Frodo","Pippin", "Sam"]
#     # file_obj.writelines("Hellow Python I/O")
#     # file_obj.writelines(nammes)
#     # print("file_obj")
#     # print("Новая строка в файле", file=file_obj)
#     # print(file_obj.readline())
#     while True:
#         line = file_obj.readline()
#         if not line:
#             break


# dir_path = os.path.dirname()
# dir_path = os.path.dirname(os.path.realpath(__file__))

# import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
# with open(f"{dir_path}/secreets.txt", "a+", encoding= "utf-8") as file_obj:
#     file_obj.seek(0)
#     list_str = file_obj.readlines()
#     # print(list_str)
#     a=0
#     while True:
#         a =+ 1
#         if line == "Line 4\n":
#             list_str.insert()
#         if not line:
#             break
#
