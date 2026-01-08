# Exercise 1
# print("Hello world\n" * 4 + "I love python\n" * 4)

# Exercise 2
month = input("Input number of month 1 to 12 ")
if month.isnumeric():
    month=int(month)
    if month>=3 and month<=5:
        print("Spring")
    elif month>=6 and month<=8:
        print("Summer")
    elif month>=9 and month<=11:
        print("Autumn")
    elif (month>=1 and month<=2) or month==12:
        print("Winter")
    else: print("You did wrong")
else: print("You did wrong")

