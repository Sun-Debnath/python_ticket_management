num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))

# Initialize an empty 2D list based on user input
matrix = []

# Populate the 2D list with user input or default values
for i in range(num_rows):
    row = []  # Initialize an empty row
    for j in range(num_cols):
        element = input(f"Enter the value for element at position ({i+1}, {j+1}): ")
        row.append(element)
    matrix.append(row)

# Display the 2D list
print("The 2D List:")
for row in matrix:
    print(row)