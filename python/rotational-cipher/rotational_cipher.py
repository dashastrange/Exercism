def rotate(text, key):
    result = []

    for char in text:
        if char.isalpha():
            # Determine ASCII offset (uppercase or lowercase)
            offset = ord('A') if char.isupper() else ord('a')
            # Rotate character and wrap around using modulo 26
            rotated = chr((ord(char) - offset + key) % 26 + offset)
            result.append(rotated)
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)

    return ''.join(result)
