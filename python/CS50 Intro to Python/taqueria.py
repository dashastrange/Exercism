menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        order = input("Item: ").title()
    except EOFError:
        print('$'+ f'{total:.2f}')
        break
    else:
        if order in menu.keys():
            item = menu.get(order)
            total = total + item
            print('$'+ f'{total:.2f}')