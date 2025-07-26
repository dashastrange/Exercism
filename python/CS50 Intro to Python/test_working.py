import pytest
from working import convert

def test_standard_time_format():
    # Test standard format with minutes
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:30 PM to 1:30 PM") == "12:30 to 13:30"
    assert convert("10:15 AM to 11:45 AM") == "10:15 to 11:45"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_abbreviated_time_format():
    # Test formats without minutes
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"
    assert convert("10 AM to 11 AM") == "10:00 to 11:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_mixed_time_formats():
    # Test mixed formats (with and without minutes)
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 11:59 PM") == "00:00 to 23:59"

def test_overnight_shifts():
    # Test time ranges that cross midnight
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("11:30 PM to 12:30 AM") == "23:30 to 00:30"

def test_invalid_format():
    # Test invalid formats
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")  # Missing spaces before AM/PM
    
    with pytest.raises(ValueError):
        convert("9:00 am to 5:00 pm")  # Lowercase am/pm
    
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")  # Using hyphen instead of "to"
    
    with pytest.raises(ValueError):
        convert("9:00 to 17:00")  # Missing AM/PM

def test_invalid_times():
    # Test invalid times
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")  # Hour > 12
    
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")  # Minute > 59
    
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")  # Hour > 12
    
    with pytest.raises(ValueError):
        convert("0:00 AM to 5:00 PM")  # Hour < 1