import hw3_6

# Define the function to test max_of_three
def test_max_of_three():
    assert hw3_6.max_of_three(1, 2, 3) == 3, "Failed test case 1 for max_of_three"
    assert hw3_6.max_of_three(3, 2, 1) == 3, "Failed test case 2 for max_of_three"
    assert hw3_6.max_of_three(1, 3, 2) == 3, "Failed test case 3 for max_of_three"
    assert hw3_6.max_of_three(-1, -2, -3) == -1, "Failed test case 4 for max_of_three"
    assert hw3_6.max_of_three(0, 0, 0) == 0, "Failed test case 5 for max_of_three"
    assert hw3_6.max_of_three(5, 5, 5) == 5, "Failed test case 6 for max_of_three"
    assert hw3_6.max_of_three(1, 2, 2) == 2, "Failed test case 7 for max_of_three"
    print("test_max_of_three passed all tests")

if __name__ == "__main__":
    test_max_of_three()
    # Call more test functions as needed