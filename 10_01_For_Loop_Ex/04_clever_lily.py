age = int(input())
laundry_machine_price = float(input())
one_toy_price = int(input())

toys_price = 0
birthday_counter = 0
money = 0

for i in range(1,age + 1):
    if i % 2 != 0:
        toys_price += one_toy_price
    else:
        birthday_counter += 1

for i in range(1,birthday_counter + 1):
    money += 10 * i - 1

budget = toys_price + money

if budget >= laundry_machine_price:
    print(f"Yes! {budget - laundry_machine_price:.2f}")
else:
    print(f"No! {laundry_machine_price - budget:.2f}")
