import plates
from plates import is_valid

def main():
    test_length()
    test_end_numeric()
    test_start_alpha()
    test_non_alpha_num()
    test_num_not_zero()
    test_no_num_middle()


def test_length():
    assert is_valid("abc") == True
    assert is_valid("asdfghjklkk") == False

def test_start_alpha():
    assert is_valid("aa123") == True
    assert is_valid("123asd") == False
    assert is_valid("a123") == False
    assert is_valid("0aa0") == False
    assert is_valid("aawqe") == True

def test_end_numeric():
    assert is_valid("abc123") == True
    assert is_valid("asd123a") == False
    assert is_valid("asdqweqweqwe123") == False
    assert is_valid("aa000rt") == False
    assert is_valid("a123") == False

def test_no_num_middle():
    assert is_valid("asd123a") == False
    assert is_valid("as10") == True
    assert is_valid("12") == False
    assert is_valid("0000as") == False
    assert is_valid("as1223") == True
    assert is_valid("a1") == False
    assert is_valid("a1a2") == False
    assert is_valid("aaa22a") == False

def test_num_not_zero():
    assert is_valid("aa123") == True
    assert is_valid("aa012") == False
    assert is_valid("aa0") == False
    assert is_valid("aa10") == True

def test_non_alpha_num():
    assert is_valid("!@##") == False
    assert is_valid("aa!@##") == False

if __name__ == "__main__":
    main()
