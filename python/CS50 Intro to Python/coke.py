allowed_coins = ['25', '10', '5']
all_money = 0

while all_money < 50:
    inserted = input("Insert Coin: ")
    if inserted in allowed_coins:
        all_money = all_money + int(inserted)
        amount_due = 50 - all_money
        if amount_due > 0:
            print("Amount Due:", amount_due)
        elif amount_due == 0:
            print("Change Owed:", amount_due)
        elif amount_due < 0:
            print("Change Owed:", amount_due * -1)
        else:
            break
        continue
    else:
        print("Amount Due: 50")

