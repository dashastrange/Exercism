def is_armstrong_number(number):
    x = 0
    num = str(number)
    power = len(num)  # The number of digits

    for n in num:
        x += int(n) ** power  # Raise each digit to the power of the number of digits and sum them

    return x == number  # Returns True if Armstrong, False otherwise


