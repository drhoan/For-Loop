import hw3_0

def test_print_numbers(capsys):
    hw3_0.print_numbers()
    captured = capsys.readouterr()
    assert captured.out == "0\n1\n2\n3\n4\n", "Failed"
    print("passed")
