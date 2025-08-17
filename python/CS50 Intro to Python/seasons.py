from datetime import date
from datetime import timedelta
import inflect
import sys
p = inflect.engine()


def main():
    birthday = input("Date of birth yyyy-mm-dd: ")
    diff = return_diff(birthday)
    print(convert_to_words(diff))

def return_diff(birthday):
    try:
        birthday = date.fromisoformat(birthday)
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    diff = today - birthday 
    return diff

def convert_to_words(diff):
    minutes = diff.days * 24 * 60
    words = p.number_to_words(minutes, andword='')
    return words + " minutes"


if __name__ == "__main__":
    main()
