import hw3_8

# Define the function to test check_even_odd
def test_check_even_odd():
    assert hw3_8.check_even_odd(2) == "Even", "Failed test case 1 for check_even_odd"
    assert hw3_8.check_even_odd(3) == "Odd", "Failed test case 2 for check_even_odd"
    assert hw3_8.check_even_odd(0) == "Even", "Failed test case 3 for check_even_odd"
    assert hw3_8.check_even_odd(-2) == "Even", "Failed test case 4 for check_even_odd"
    assert hw3_8.check_even_odd(-3) == "Odd", "Failed test case 5 for check_even_odd"
    print("test_check_even_odd passed all tests")

if __name__ == "__main__":
    test_check_even_odd()
    # Call more test functions as needed