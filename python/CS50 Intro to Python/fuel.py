
def main():
    print(gauge(convert(input("Enter level as x/y: "))))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
        except ValueError:
            raise

        if x > y or type(x) != int or type(y) != int:
            raise ValueError

        if y == 0:
            raise ZeroDivisionError

        try:
            return round((x / y) * 100) #mistakenly return a str instead of an int
        except (ZeroDivisionError, ValueError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        p_str = str(percentage) + '%' #mistakenly omit a % in the resulting str
        return p_str


if __name__ == "__main__":
    main()