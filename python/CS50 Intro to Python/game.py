import random

while True:
    try:
        number = int(input("Level: "))
        break
    except ValueError:
        continue

random_num = random.randint(1, number)

while True:
    try:
        quess_num = int(input("Guess: "))
    except ValueError:
        continue

    if quess_num > 0:
        if quess_num < random_num:
            print("Too small!")
            continue
        if quess_num > random_num:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
    else:
        continue