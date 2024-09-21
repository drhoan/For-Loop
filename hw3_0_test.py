import hw3_0

def test_print_numbers(capsys):
    hw3_0.print_numbers()
    captured = capsys.readouterr()
    assert captured.out == "0\n1\n2\n3\n4\n", "Failed"
    print("passed")

# To run this test, you need to type into the terminal: pytest hw3_0_test.py