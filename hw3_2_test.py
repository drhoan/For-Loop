import hw3_2

def test_print_months(capsys):
    hw3_2.print_months()
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == "One of the months of the year is January\nOne of the months of the year is February\nOne of the months of the year is March\nOne of the months of the year is April\nOne of the months of the year is May\nOne of the months of the year is June\nOne of the months of the year is July\nOne of the months of the year is August\nOne of the months of the year is September\nOne of the months of the year is October\nOne of the months of the year is November\nOne of the months of the year is December\n"

# To run this test, you need to type into the terminal: pytest hw3_2_test.py