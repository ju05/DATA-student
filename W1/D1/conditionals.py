# CONDITIONALS : IF STATEMENTS

# if condition:
#     <block of code>:
# elif
# else:


# secret_number = 55
# user_number = int(input("Guss a number "))
# if user_number == secret_number:
#     print("Cool")
# elif user_number == 7:
#     print("You\" very close")
# else:
#     print("Sorry you lose")


take_number = int(input("Print number between 1 to 100 "))

if take_number%3 == 0:
    if take_number%5 == 0:
        print("FizzBuzz")
    else: print("Fizz")
elif take_number%5 == 0:
    print("Buzz")

if take_number%3 == 0:
    print("Fizz", end='')
if take_number%5 == 0:
    print("Buzz")
