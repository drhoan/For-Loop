import hw3_7

# Define the function to test check_number
def test_check_number():
    assert hw3_7.check_number(10) == "Positive", "Failed test case 1 for check_number"
    assert hw3_7.check_number(-5) == "Negative", "Failed test case 2 for check_number"
    assert hw3_7.check_number(0) == "Zero", "Failed test case 3 for check_number"
    assert hw3_7.check_number(100) == "Positive", "Failed test case 4 for check_number"
    assert hw3_7.check_number(-100) == "Negative", "Failed test case 5 for check_number"
    print("test_check_number passed all tests")

if __name__ == "__main__":
    test_check_number()
    # Call more test functions as needed