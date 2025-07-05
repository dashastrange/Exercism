import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Enter name: ")
        names.append(name)
        print()
    except EOFError:
        print(f"Adieu, adieu, to", p.join(names))
        break


