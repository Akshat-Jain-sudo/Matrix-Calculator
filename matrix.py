import numpy as np

def take_matrix_input(name):
    print(f"\nEnter values for {name}:")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter the elements row-wise (space separated):")

    matrix = []
    for i in range(rows):
        row_input=input(f"Row {1+i}: ").split()
        
        if len(row_input) != cols:
            print("Incorrect number of elements! Try again.")
            return take_matrix_input(name)
        row=[]
        for j in range(len(row_input)):
            row.append(int(j))
        matrix.append(row)

    return np.array(matrix)

def menu():
    print()
    print("Matrix Calculator Menu:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        A = take_matrix_input("Matrix A")
        B = take_matrix_input("Matrix B")
        if (A.shape == B.shape):
            print("\nResult of A + B:")
            print(A + B)
        else:
            print("Matrix dimensions must be the same for addition.")

    elif choice == '2':
        A = take_matrix_input("Matrix A")
        B = take_matrix_input("Matrix B")
        if A.shape == B.shape:
            print("\nResult of A - B:")
            print(A - B)
        else:
            print("Matrix dimensions must be the same for subtraction.")

    elif choice == '3':
        A = take_matrix_input("Matrix A")
        B = take_matrix_input("Matrix B")
        if A.shape[1] == B.shape[0]:
            print("\nResult of A x B:")
            print(np.dot(A, B))
        else:
            print("Number of columns of A must equal number of rows of B for multiplication.")

    elif choice == '4':
        A = take_matrix_input("Matrix")
        print("\nTranspose of the Matrix:")
        print(A.T)

    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
