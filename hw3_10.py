"""Every year that is exactly divisible by four is a leap year,
except for years that are exactly divisible by 100,
but these centurial years are leap years if they are exactly divisible by 400.
For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are."""

def is_leap_year(year):
    # TODO: Implement leap year checking logic
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    print(is_leap_year(2000))  # Expected output: True
    print(is_leap_year(1900))  # Expected output: False
    print(is_leap_year(2024))  # Expected output: True
    print(is_leap_year(2023))  # Expected output: False
    # Call more test functions as needed
