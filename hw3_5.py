# Define a function to check if a number is even
def is_even(n):
    # TODO: Implement even check
    if n % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    # Test the function
    print(is_even(4))  # Expected output: True
    print(is_even(7))  # Expected output: False