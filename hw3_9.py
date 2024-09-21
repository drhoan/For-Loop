def calculate_grade(score):
    # TODO: Implement logic to assign a grade based on the score
    # 90-100: A, 80- <90: B, 70- <80: C, 60- <70: D, 0- <60: F
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    # Test the function
    print(calculate_grade(95))  # Expected output: A
    print(calculate_grade(85))  # Expected output: B
    print(calculate_grade(75))  # Expected output: C
    print(calculate_grade(65))  # Expected output: D
    print(calculate_grade(50))  # Expected output: F
