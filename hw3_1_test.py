import hw3_1

def test_print_hello(capsys):
    hw3_1.print_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"*10, "Failed to print 10 lines of Hello"
    
# To run this test, you need to type into the terminal: pytest hw3_1_test.py