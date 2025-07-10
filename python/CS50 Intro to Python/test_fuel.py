import fuel
import pytest
from fuel import convert, gauge

def main():
    test_gauge()
    test_convert()

def test_convert():
    assert convert("3/4") == 75

    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("-1/-6")

    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge():
    assert gauge(3) == '3%'

    assert gauge(1) == 'E'

    assert gauge(99) == 'F'


if __name__ == "__main__":
    main()