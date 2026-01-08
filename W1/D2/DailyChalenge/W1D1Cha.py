# Challenge 1: Multiples of a Number
Declair a new variable, ask the user to enter a number, convert it from a string to an integer
This will be our base number
first_number = int(input("Input the first number: "))
# Declair a new variable, ask the user to inter the number of multiples to generate, convert it to an integer
# This will be the length of our list
length_list = int(input("Input length of list: "))
# Create an empty list to store the results
list_numbers = []
# Start a for loop from 1 to entered number
# Multiply the base number by the current loop number and append the result to the list
for num in range(1, length_list + 1):
    list_numbers.append(first_number * num)
# Shou the final list
print(list_numbers)

# Challenge 2: Remove Consecutive Duplicate Letters
# Declare a new variable, ask the user to inter a string (it will remain a string type)
users_string = input("Input string: ")
# Creat the empty string to store the result
result_string = ""
# Creat an integer variable and set it to zero
# It will be used as the index for iterating through the string
index = 0
# Start a while loop that runs until we reach the end of the input string
while index < len(users_string):
    # Add the current character to the result string
    result_string += users_string[index]
    # Start another while loop that continues if the next character is the same,and we are not at the end of the string
    while index + 1 < len(users_string) and users_string[index] == users_string[index + 1]:
        # Skip all consecutive duplicate characters by increasing the index
        index += 1
    # Move to the next character
    index += 1

print(result_string)
