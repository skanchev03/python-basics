fuel_type = input()
fuel_amount = float(input())
club_card = input()

diesel_price = 2.33
gasoline_price = 2.22
gas_price = 0.93
price = 0

if club_card == 'Yes':
    diesel_price -= 0.12
    gasoline_price -= 0.18
    gas_price -= 0.08

if fuel_type == 'Diesel':
    price = diesel_price * fuel_amount

if fuel_type == 'Gasoline':
    price = gasoline_price * fuel_amount

if fuel_type == 'Gas':
    price = gas_price * fuel_amount

if 20 <= fuel_amount <= 25:
    price *= 0.92
elif fuel_amount > 25:
    price *= 0.9

print(f'{price:.2f} lv.')
