import hw3_10

# Define the function to test is_leap_year
def test_is_leap_year():
    assert hw3_10.is_leap_year(2000) == True, "Failed test case 1 for is_leap_year"
    assert hw3_10.is_leap_year(1900) == False, "Failed test case 2 for is_leap_year"
    assert hw3_10.is_leap_year(2024) == True, "Failed test case 3 for is_leap_year"
    assert hw3_10.is_leap_year(2023) == False, "Failed test case 4 for is_leap_year"
    assert hw3_10.is_leap_year(1600) == True, "Failed test case 5 for is_leap_year"
    assert hw3_10.is_leap_year(1700) == False, "Failed test case 6 for is_leap_year"
    assert hw3_10.is_leap_year(2020) == True, "Failed test case 7 for is_leap_year"
    assert hw3_10.is_leap_year(2019) == False, "Failed test case 8 for is_leap_year"
    print("test_is_leap_year passed all tests")

if __name__ == "__main__":
    test_is_leap_year()
    # Call more test functions as needed