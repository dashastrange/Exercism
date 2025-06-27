groceries = {}
num = 0

while True:
    try:
        item = input().upper()
    except EOFError:
        break
    else:
        if item in groceries:
            num = num + 1
            groceries.update({item : num})
        else:
            num = 1
            groceries.update({item : num})


for key, val in sorted(groceries.items()):
    print(val, key)