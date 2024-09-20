import hw3_4

# Define the function to subtract two numbers
def test_subtract_numbers():
    assert hw3_4.subtract_numbers(30, 7) == 23, "Failed when subtracting 7 from 30, expecting 23"
    assert hw3_4.subtract_numbers(10, 5) == 5, "Failed when subtracting 5 from 10, expecting 5"
    print("test_subtract_numbers passed all tests")

# Define the function to multiply two numbers
def test_multiply_numbers():
    assert hw3_4.multiply_numbers(5, 5) == 25, "Failed when multiplying 5 and 5, expecting 25"
    assert hw3_4.multiply_numbers(3, 4) == 12, "Failed when multiplying 3 and 4, expecting 12"
    print("test_multiply_numbers passed all tests")

# Define the function to divide two numbers
def test_divide_numbers():
    assert hw3_4.divide_numbers(10, 2) == 5, "Failed when dividing 10 by 2, expecting 5"
    assert hw3_4.divide_numbers(10, 0) == ZeroDivisionError, "Failed when dividing 10 by 0, expecting ZeroDivisionError"
    print("test_divide_numbers passed all tests")

if __name__ == "__main__":
    test_subtract_numbers()
    test_multiply_numbers()
    test_divide_numbers()