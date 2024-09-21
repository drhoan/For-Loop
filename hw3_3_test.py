import hw3_3

def test_print_squares(capsys):
    hw3_3.print_squares()
    captured = capsys.readouterr()
    assert captured.out == "12 144\n10 100\n32 1024\n3 9\n66 4356\n17 289\n42 1764\n99 9801\n20 400\n", f'Different from expected output'

# To run this test, you need to type into the terminal: pytest hw3_3_test.py