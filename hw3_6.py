# Define a function to return the maximum of three numbers
def max_of_three(a, b, c):
    # TODO: Implement logic to find the largest of three numbers
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == "__main__":
    # Test the function
    print(max_of_three(1, 5, 3))  # Expected output: 5
    print(max_of_three(7, 2, 9))  # Expected output: 9
    print(max_of_three(7, 7, 2))  # Expected output: 7
    print(max_of_three(5, 5, 5))  # Expected output: 5
    print(max_of_three(1, 2, 2))  # Expected output: 2
    print(max_of_three(0, 0, 0))  # Expected output: 7
