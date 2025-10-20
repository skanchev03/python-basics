months = int(input())

electricity_price = 0
water_price = months * 20
internet_price = months * 15
others_price = 0

for i in range(1, months + 1):
    electricity = float(input())

    electricity_price += electricity

    others_price += (electricity + 35) * 1.2

average_price = (electricity_price + water_price + internet_price + others_price) / months

print(f"Electricity: {electricity_price:.2f} lv")
print(f"Water: {water_price:.2f} lv")
print(f"Internet: {internet_price:.2f} lv")
print(f"Other: {others_price:.2f} lv")
print(f"Average: {average_price:.2f} lv")
