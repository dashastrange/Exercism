def is_valid(isbn):
    isbn = isbn.replace('-', '')  # Remove hyphens
    if len(isbn) != 10:  # Check length
        return False

    num_list = []
    for i, char in enumerate(isbn):
        if char.isdigit():
            num_list.append(int(char))
        elif char == 'X' and i == 9:  # 'X' is only valid in the last position
            num_list.append(10)
        else:
            return False

    # Compute the ISBN-10 checksum
    sum_num = sum(num_list[i] * (10 - i) for i in range(10))

    return sum_num % 11 == 0  # Valid if divisible by 11
