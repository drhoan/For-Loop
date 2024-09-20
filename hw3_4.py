# Define the function to add two numbers
def add_numbers(a, b):
    # TODO: Implement addition
    return a + b

# Define the function to subtract two numbers
def subtract_numbers(a, b):
    # TODO: Implement subtraction
    return a - b

# Define the function to multiply two numbers
def multiply_numbers(a, b):
    # TODO: Implement multiplication
    return a * b

# Define the function to divide two numbers
def divide_numbers(a, b):
    # TODO: Implement division with error handling for division by zero
    try:
        #put your code here
        return a / b
    except ZeroDivisionError:
        return ZeroDivisionError

if __name__ == "__main__":
    # Test the functions
    print(add_numbers(5, 3))  # Expected output: 8
    print(subtract_numbers(5, 3))  # Expected output: 2
    print(multiply_numbers(5, 3))  # Expected output: 15
    print(divide_numbers(10, 0))  # Expected output: Cannot divide by zero