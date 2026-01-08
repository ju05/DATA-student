import random

user_string = input("Input string 10 characters long: ")
a = ""
if len(user_string) == 10:
    print("Perfect string")
    print(user_string[0] + user_string[-1])
    for num in user_string:
        a = (f"{a}{num}")
        print(a)
    b = list(user_string)
    random.shuffle(b)
    print(''.join(b))

elif len(user_string) > 10:
    print("String too long.")

elif len(user_string) < 10:
    print("String not long enough.")

