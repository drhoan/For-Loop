def check_number(number):
    # TODO: Implement the logic to check if the number is positive, negative, or zero
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == "__main__":
    print(check_number(10))  # Expected output: Positive
    print(check_number(-5))  # Expected output: Negative
    print(check_number(0))  # Expected output: Zero
