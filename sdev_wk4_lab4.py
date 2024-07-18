"""
This Python module facilitates matrix operations 
(addition, subtraction, matrix multiplication, and element-by-element multiplication) 
on 3x3 matrices, with input validation for phone numbers and zip codes. 
It uses NumPy for matrix operations and provides an interactive user interface for 
continuous matrix computation until user exit.
"""
import re # Regular expression module used for input validation
import numpy as np # NumPy module used for matrix operations


def is_valid_phone(phone):
    """Checks if a phone number is in the correct format (XXX-XXX-XXXX)."""
    return re.match(r'^\d{3}-\d{3}-\d{4}$', phone)


def is_valid_zip(zip_code):
    """Checks if a zip code is in the correct format (XXXXX-XXXX)."""
    return re.match(r'^\d{5}-\d{4}$', zip_code)


def get_matrix():
    """Prompts the user to enter a 3x3 matrix and returns it as a numpy array."""
    while True:
        try:
            # Get the matrix row by row
            row1 = input().strip().split()
            row2 = input().strip().split()
            row3 = input().strip().split()
            # Convert the matrix to a numpy array
            matrix = np.array([row1, row2, row3], dtype=int)
            return matrix
        except ValueError:  # Raised when the matrix contains non-numeric values
            print("Invalid matrix. Please enter numeric values only.")


def perform_operation(a, b):
    """Prompts the user to select a matrix operation and returns the result."""
    print("Select a Matrix Operation from the list below:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Matrix Multiplication")
    print("d. Element by element multiplication")
    choice = input().strip().lower()

    # Perform the operation based on the user's choice
    if choice == 'a':
        result = np.add(a, b)
    elif choice == 'b':
        result = np.subtract(a, b)
    elif choice == 'c':
        result = np.matmul(a, b)
    elif choice == 'd':
        result = np.multiply(a, b)
    else:
        print("Invalid choice.")
        return None

    return result


def print_matrix(matrix):
    """Prints a matrix in a formatted way."""
    # Join each row with a space and each row with a new line
    formatted = '\n'.join(' '.join(str(cell) for cell in row) for row in matrix)
    print(formatted)


def print_means(matrix):
    """Prints the row and column means of a matrix."""
    # Round each mean value to 2 decimal places
    row_mean = ', '.join(str(round(val, 2)) for val in np.mean(matrix, axis=1))
    col_mean = ', '.join(str(round(val, 2)) for val in np.mean(matrix, axis=0))

    print("\nThe row mean values of the results are:")
    print("Row: ", row_mean)
    print("The column mean values of the results are:")
    print("Column: ", col_mean)


def print_results(result):
    """Prints the results of the matrix operation."""
    print("\nThe results are:")
    print_matrix(result)
    print("\nThe Transpose is:")
    print_matrix(np.transpose(result))
    print_means(result)


def main():
    """Main function that runs the program."""
    print("\n****** Welcome to the Python Matrix Application ******")
    prompt = "\nDo you want to play the Matrix Game? Enter Y for Yes or N for No: "
    while input(prompt).strip().lower() == 'y': # Loop until the user enters 'n'
        phone = input("Enter your phone number (XXX-XXX-XXXX): ")
        # Validate the phone number
        while not is_valid_phone(phone):
            phone = input("Your phone number is not in correct format. Please re-enter: ")

        zip_code = input("Enter your zip code+4 (XXXXX-XXXX): ")
        # Validate the zip code
        while not is_valid_zip(zip_code):
            zip_code = input("Your zip code is not in correct format. Please re-enter: ")

        print("Enter your first 3x3 matrix:")
        matrix_a = get_matrix()
        print("Your first 3x3 matrix is:")
        print_matrix(matrix_a)

        print("Enter your second 3x3 matrix:")
        matrix_b = get_matrix()
        print("Your second 3x3 matrix is:")
        print_matrix(matrix_b)

        result = perform_operation(matrix_a, matrix_b)
        # Print the results if the operation is valid
        if result is not None:
            print_results(result)

    print("\n****** Thanks for playing Python Numpy ******\n")


main()
