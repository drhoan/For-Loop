import hw3_1

def test_print_hello(capsys):
    hw3_1.print_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"*10, f"Expected output was {'Hello\n'*10} but got {captured.out}"
    