import random

def main():
    rounds = 0
    score = 0
    tries = 2

    lvl = get_level()

    while rounds != 10:

        x = generate_integer(lvl)
        y = generate_integer(lvl)

        result = int(x + y)
        rounds += 1

        while True:
            guess = int(input(f"{x} + {y} = "))

            if tries > 0:
                if result == guess:
                    score += 1
                    break
                if result != guess:
                    tries -= 1
                    print("EEE")
                    continue
            else:
                print(f"{x} + {y} = {result}")
                tries = 2
                break
    print("Score: ", score)


def get_level():
    levels = [1, 2, 3]

    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level in levels:
            return level
        else:
            continue

def generate_integer(l):
    if l == 1:
        rand = random.randint(0, 9)
    elif l == 2:
        rand = random.randint(10, 99)
    elif l == 3:
        rand = random.randint(100, 999)
    return rand


if __name__ == "__main__":
    main()