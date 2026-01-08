# LOOPS^ FOR AND WHILE

# FOR LOOP

# fruits = ['apple', 'banana', 'kiwi', 'pear']
# for each_fruit in fruits:
#     print(f"I love {each_fruit}")
#
# # for i in range(1, 5):
# #     print(i)
#
# for i in range(1, len(fruits)+1):
#     print(i)

# odd_nums = list(range(1, 11, 2))
# print(odd_nums)
# print(min(odd_nums))
# print(max(odd_nums))
# print(sum(odd_nums))


# WHILE LOOP: condition

# num = 1
# while num <= 10:
#     if num == 5:
#         break
#     print(num)
#     num += 1

# print(num)


secreet_number = 777
user_number = 0

while int(user_number) != secreet_number:
    user_number = input("try a number ")
    if user_number == "q":
        print("Exiting the game")
        break
    print("not number, try again or type 'q' to quit")
else:
    print("Congrets you won!")