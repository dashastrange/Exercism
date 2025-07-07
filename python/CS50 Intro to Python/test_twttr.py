import twttr
from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("Hello, world") == "Hll, wrld"
    assert shorten("He11o, wo2ld") == "H11, w2ld"
    assert shorten("AWW") == "WW"

if __name__ == '__main__':
    main()