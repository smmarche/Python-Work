#This program calculates the Kronecker product to get a random barcode
# This could be used as a barcode system to keep track of all books to manage the inventory.

import random
valid_matrix_input_A = False
valid_matrix_input_B = False
#Set up a while loop so if the input is not valid the program will ask again for a valid input.
while not valid_matrix_input_A:
    matrix_dimensions_A = input("Enter matrix A rows and columns: ")

    split_matrix_input_A = matrix_dimensions_A.split()
    #Turns the inputs from string into integers
    rows_of_A = int(split_matrix_input_A[0])
    columns_of_A = int(split_matrix_input_A[1])
#Checking that now rows/columns are not less than 1.
# Checking to see that there are no rows or columns that
# exceeds 10.
    if 0 >= rows_of_A or rows_of_A > 10 or 0 >= columns_of_A or columns_of_A > 10:
        print("Invalid matrix size. Try again.")
    else:
        valid_matrix_input_A = True
        print("")
while not valid_matrix_input_B:
#Next, this asks for the dimensions of matrix B.

    matrix_dimensions_B = input("Enter matrix B rows and columns: ")
    #make sure to check that the input was a space
    split_matrix_input_B = matrix_dimensions_B.split()
    rows_of_B = int(split_matrix_input_B[0])
    columns_of_B = int(split_matrix_input_B[1])
#This checks that the rows/and columns are not less than 0 or greater than 10 in B.
    if 0 >= rows_of_B or rows_of_B > 10 or 0 >= columns_of_B or columns_of_B > 10:
        print("Invalid matrix size. Try again.")
    else:
        valid_matrix_input_B = True

#Creating and printing matrix A
print("\n")
print("Random matrix A: ")
matrix_A = []
for row_A in range(rows_of_A):
#Random number between 1 and 99 not inclusive are printed in matrix A
    line = [random.randrange(0, 99, 2) for number in range(columns_of_A)]
    matrix_A.append(line)
for row in range(rows_of_A):
    print()
    for col in range(columns_of_A):
        print(f"{matrix_A[row][col]:<6}", end="")
#Creating and printing matrix B
print("\n")
print("Random matrix B: ")
matrix_B = []
for row_B in range(rows_of_B):
# Random number between 1 and 99 inclusive are printed in matrix A
    line = [random.randrange(1, 100, 2) for number in range(columns_of_B)]
    matrix_B.append(line)
for row in range(rows_of_B):
    print()
    for col in range(columns_of_B):
        print(f"{matrix_B[row][col]:<6}", end="")
print("\n")
#Computing the Kronecker Product
print("Matrix C:")
matrix_C = []
for rowa in range(rows_of_A):
    for rowb in range(rows_of_B):
        line = []
        for columna in range(columns_of_A):
            for columnb in range(columns_of_B):
                line.append(matrix_A[rowa][columna] * matrix_B[rowb][columnb])
        matrix_C.append(line)
for row in range(rows_of_A*rows_of_B):
    print()
    for col in range(columns_of_A*columns_of_B):
        print(f"{matrix_C[row][col]:<6}", end="")
print("\n")

print("Transpose matrix T: ")
#Transpose matrix-simply switch row space and column space
for col in range(columns_of_A*columns_of_B):
    print()
    for row in range(rows_of_A*rows_of_B):
        print(f"{matrix_C[row][col]:<6}", end="")

#Takes the sum of the rows in C to make the barcode
print("\n")
print("Barcode string: ")
sum_of_barcode = [sum(tup) for tup in zip(*matrix_C)]
#This takes the numbers in the list out
sum_of_barcode = " ".join(str(num) for num in sum_of_barcode)
print(sum_of_barcode)

# sum_of_columns = []
# for i in range()




