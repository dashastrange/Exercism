from datetime import date, timedelta
import pytest
from seasons import return_diff, convert_to_words


def test_return_diff():
    # Test with today's date (should be 0 days)
    today = date.today().isoformat()
    diff = return_diff(today)
    assert diff.days == 0
    
    # Test with yesterday (should be 1 day)
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    diff = return_diff(yesterday)
    assert diff.days == 1
    
    # Test with one year ago (365 days)
    one_year_ago = (date.today() - timedelta(days=365)).isoformat()
    diff = return_diff(one_year_ago)
    assert diff.days == 365


def test_convert_to_words():
    # Test with timedelta objects (as the function expects)
    zero_diff = timedelta(days=0)
    assert convert_to_words(zero_diff) == "zero minutes"
    
    one_day_diff = timedelta(days=1)
    assert convert_to_words(one_day_diff) == "one thousand, four hundred forty minutes"
    
    # Test with 365 days (one year)
    year_diff = timedelta(days=365)
    assert convert_to_words(year_diff) == "five hundred twenty-five thousand, six hundred minutes"


def test_invalid_date_format():
    # Test that invalid date formats cause system exit
    with pytest.raises(SystemExit):
        return_diff("February 6th, 1998")
    
    with pytest.raises(SystemExit):
        return_diff("02/06/1998")
    
    with pytest.raises(SystemExit):
        return_diff("invalid date")