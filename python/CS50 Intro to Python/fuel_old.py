while True:
    level = input("Enter level as x/y: ")

    try:
        x, y = level.split("/")
        x = int(x)
        y = int(y)
    except ValueError:
        continue

    try:
        percentage = round((x / y) * 100)
    except ZeroDivisionError:
        continue
    else:
        if x > y:
            continue
        elif percentage <= 1:
            print("E")
            break
        elif percentage >=99:
            print("F")
            break
        else:
            print(str(percentage)+'%')
            break

