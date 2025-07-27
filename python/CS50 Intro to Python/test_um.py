from um import count


def test_single_um():
    """Test that a single 'um' is counted correctly."""
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("uM") == 1


def test_multiple_um():
    """Test that multiple 'um's are counted correctly."""
    assert count("um um um") == 3
    assert count("um, um, um") == 3
    assert count("um? um! um.") == 3
    assert count("Um, thanks, UM, for the, um, help.") == 3


def test_substring_um():
    """Test that 'um' is not counted when part of another word."""
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrage") == 0
    assert count("circumvent") == 0


def test_mixed_cases():
    """Test cases with both valid and invalid 'um's."""
    assert count("um is in umami and album") == 1
    assert count("Um, this is an umbrella, um.") == 2
    assert count("YUMMY, UM, ALBUM") == 1


def test_edge_cases():
    """Test edge cases like punctuation, empty strings, etc."""
    assert count("") == 0
    assert count("um.") == 1
    assert count(".um") == 1
    assert count("um?!") == 1
    assert count("um-um") == 2


def test_complex_sentences():
    """Test complex sentences with various patterns."""
    assert count("Um, I, um, don't, um, know, um...") == 4
    assert count("Yummy mummy, um, dummy, um, crummy!") == 2
    assert count("Um...um...um...") == 3
    assert count("Um? Umm? Ummm?") == 1