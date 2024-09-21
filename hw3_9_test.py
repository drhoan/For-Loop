import hw3_9

# Define the function to test calculate_grade
def test_calculate_grade():
    assert hw3_9.calculate_grade(95) == "A", "Failed test case 1 for calculate_grade"
    assert hw3_9.calculate_grade(85) == "B", "Failed test case 2 for calculate_grade"
    assert hw3_9.calculate_grade(75) == "C", "Failed test case 3 for calculate_grade"
    assert hw3_9.calculate_grade(65) == "D", "Failed test case 4 for calculate_grade"
    assert hw3_9.calculate_grade(55) == "F", "Failed test case 5 for calculate_grade"
    assert hw3_9.calculate_grade(100) == "A", "Failed test case 6 for calculate_grade"
    assert hw3_9.calculate_grade(0) == "F", "Failed test case 7 for calculate_grade"
    assert hw3_9.calculate_grade(89.5) == "B", "Failed test case 8 for calculate_grade"
    print("test_calculate_grade passed all tests")

if __name__ == "__main__":
    test_calculate_grade()
    # Call more test functions as needed
