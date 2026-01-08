# # Try and Except block
#
#
# # hello = "Hello world"
# #
# # if hello == "Hello world":
# #     print("That is right")
# #
# #
# # board = [[-,-,-],
# #          [-,-,-],
# #          [-,-,-]]
#
# def player_input(current_playes):
#     valid = False
#     while not valid:
#         position = input("enter position 1-9: ")
#         try:
#             if 0 <= position < 9 and board[position] == "-":
#                 board[position - 1] = current_playes
#                 print(board)
#         except:
#             print("something")
#
#
# board = ["-", "-", "-",
#          "-", "-", "-",
#          "-", "-", "-"]
#
# # player_input("X")


my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]
try:
    print(f"From main block{sum(my_list)}")
except:
    clean_list = []
    for element in my_list:
        if isinstance(element, int):
            clean_list.append(element)
        output = sum(clean_list)
    print(f"From main block {output}")

    # raise TypeError("There are string in the list")
