def check_even_odd(number):
    # TODO: Implement logic to check if the number is even or odd
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    print(check_even_odd(4))  # Expected output: Even
    print(check_even_odd(7))  # Expected output: Odd
    print(check_even_odd(0))  # Expected output: Even