sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]

profit_per_unit = 1.5

sun_day = input('Sales on Sunday?')
sales_w2.append(int(sun_day))

sales = sales_w1 + sales_w2
best_day = max(sales)
worst_day = min(sales)

sum_week_1 = sum(sales_w1)
sum_week_2 = sum(sales_w2)
sum_all = sum_week_1 + sum_week_2

print(f'Best day: {best_day}')
print(f'Worst day: {worst_day}')
print(f'Sum of week 1: {sum_week_1}')
print(f'Sum of week 2: {sum_week_2}')
print(f'Sum of all weeks: {sum_all}')




