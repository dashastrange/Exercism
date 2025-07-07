
def main():
    greet = input("Say hello: ").strip().lower()
    print(value(greet))

def value(greeting):
    if greeting.startswith("hello"):
        return 100
    elif greeting.startswith("h") and greeting.startswith("hello") == False:
        return 20
    else:
        return 0


if __name__ == "__main__":
    main()