# Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
# Write a loop that prints each number and its square on a new line. For example
# 12 144
# 10 100
# …
# Hint: You can use f-string.
def print_squares():
    numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    for number in numbers:
        print(f'{number} {number**2}')

if __name__ == "__main__":
    print_squares()