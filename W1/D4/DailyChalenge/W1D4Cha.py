# This is the input data
MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''
# Declare variables as empty lists
step = []
matrix = []
# Declare a variable as an empty string
new_matrix = ""

# Split the input string by line breaks to create a list of strings
new_list = MATRIX_STR.split("\n")
# Start a loop to convert each string into a list of characters
for line in new_list:
    # Loop through each character in the current line
    for character in line:
        # Add each character to the temporary list
        step.append(character)
    # If the temporary list is not empty, add a copy of it to the matrix
    if step:
        matrix.append(step.copy())
    # Clear the temporary list for the next line
    step.clear()


# Start a loop to collect characters from the matrix and place them in the correct position in the final string
# This loop takes each character and calculates its correct index in the final string based on its row and column
for line_num, lane_matrix in enumerate(matrix, start=1):
    for index, cahr_lane in enumerate(lane_matrix):
        # Position in string is be how many characters are before character which we want to add
        # Calculate the position in the final string for the current character
        a = line_num*index + line_num - 1
        # If the character is not a letter, replace it with a space
        if not cahr_lane.isalpha():
            cahr_lane = " "
        # Use slicing to insert the character into the final string at the correct position
        new_matrix = new_matrix[:a] + cahr_lane + new_matrix[a:]
# To remove extra spaces, split the string into words and rejoin them with a single space
print(new_matrix)

# new_matrix = " ".join(new_matrix.split())
# # Print our final result
# print(new_matrix)

# print(matrix)
# def matrix_2d():
#     matrix = []
#     for line in new_list:
#         matrix.append(list(line))
#         print("matrix", matrix)
#     return matrix

# max_cols = max(len(row) for row in matrix)

# chars = []
# for col in range(max_cols):
#     for row in range(len(matrix)):
#         if col < len(matrix[row]):
#             char = matrix[row][col]
#             chars.append(char if char.isalpha() else " ")
#
# new_matrix = " ".join("".join(chars).split())
#
# print(new_matrix)

def decode_matrix_string(matrix_str: str) -> str:
    matrix = [list(line) for line in matrix_str.strip().split('\n')]
    max_cols = max(len(row) for row in matrix)
    chars = []
    for col in range(max_cols):
        for row in range(len(matrix)):
            if col < len(matrix[row]):
                char = matrix[row][col]
                chars.append(char if char.isalpha() else " ")
    return " ".join("".join(chars).split())

print(decode_matrix_string(matrix_str=MATRIX_STR))


max(value for value in nasd)
