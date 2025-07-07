def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    for i in range(2):
        if s[i].isnumeric():
            return False

    for char in s:
        if not (char.isalpha() or char.isnumeric()):
            return False

    if s.isalpha():
        return True

    first_numb = -1
    for i in range(len(s)):
        if s[i].isnumeric():
            first_numb = i
            break

    if first_numb != -1:
        if s[first_numb] == '0':
            return False

    for i in range(first_numb + 1, len(s)):
        if not s[i].isnumeric():
            return False

    return True


if __name__ == "__main__":
    main()
