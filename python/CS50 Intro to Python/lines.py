import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    path = sys.argv[1]
    count = 0


try:
    f = open(path)
except FileNotFoundError:
    sys.exit("File does not exist.")
else:
    lines = f.readlines()

    for line in lines:
        if line.strip().startswith("#") or line.isspace() or line == "":
            continue
        else:
            count = count + 1
            f.close()


    print(count)
