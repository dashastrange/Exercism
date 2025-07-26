from numb3rs import validate

def main():
    test_dots()

def test_dots():
    assert validate("23.123.123.123") == True
    assert validate("1.1.1.1") == True
    assert validate("23.123.") == False
    assert validate("666.123.123.123") == False

if __name__ == "__main__":
    main()