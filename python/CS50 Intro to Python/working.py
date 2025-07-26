import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regular expression to match the various allowed time formats
    pattern = r"^(1[0-2]|0?[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|0?[1-9])(?::([0-5][0-9]))? (AM|PM)$"
    
    match = re.search(pattern, s)
    
    if not match:
        raise ValueError("Invalid format")
    
    # Extract components from the regex match
    hour1, minute1, meridiem1, hour2, minute2, meridiem2 = match.groups()
    
    # Convert to integers (handling None case for minutes)
    hour1 = int(hour1)
    minute1 = int(minute1) if minute1 else 0
    hour2 = int(hour2)
    minute2 = int(minute2) if minute2 else 0
    
    # Validate hours and minutes
    if not (0 < hour1 <= 12 and 0 < hour2 <= 12 and 0 <= minute1 < 60 and 0 <= minute2 < 60):
        raise ValueError("Invalid time")
    
    # Convert to 24-hour format
    hour1_24 = convert_to_24_hour(hour1, meridiem1)
    hour2_24 = convert_to_24_hour(hour2, meridiem2)
    
    # Format the result as HH:MM to HH:MM
    return f"{hour1_24:02d}:{minute1:02d} to {hour2_24:02d}:{minute2:02d}"


def convert_to_24_hour(hour, meridiem):
    """Convert a 12-hour format hour to 24-hour format"""
    if meridiem == "AM":
        return 0 if hour == 12 else hour
    else:  # PM
        return 12 if hour == 12 else hour + 12


if __name__ == "__main__":
    main()