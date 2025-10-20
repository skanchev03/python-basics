money_per_day = float(input())
sales_per_day = float(input())
expenses = float(input())
gift_price = float(input())

daily_money = 5 * money_per_day
sales_money = 5 * sales_per_day
total_money = daily_money + sales_money - expenses

if total_money >= gift_price:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {gift_price - total_money:.2f} BGN.")
