import hw3_5

# Define the function to test is_even
def test_is_even():
    assert hw3_5.is_even(2) == True, "Failed test case 1 for is_even"
    assert hw3_5.is_even(3) == False, "Failed test case 2 for is_even"
    assert hw3_5.is_even(0) == True, "Failed test case 3 for is_even"
    assert hw3_5.is_even(-2) == True, "Failed test case 4 for is_even"
    assert hw3_5.is_even(-3) == False, "Failed test case 5 for is_even"
    print("test_is_even passed all tests")

if __name__ == "__main__":
    test_is_even()
    # Call more test functions as needed