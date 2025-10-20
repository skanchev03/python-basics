budget = float(input())
ticket_category = input()
fans_amount = int(input())

if 1 <= fans_amount <= 4:
    budget *= 0.25
elif 5 <= fans_amount <= 9:
    budget *= 0.4
elif 10 <= fans_amount <= 24:
    budget *= 0.5
elif 25 <= fans_amount <=49:
    budget *= 0.6
elif fans_amount > 50:
    budget *= 0.75

ticket_price = 0

if ticket_category == "VIP":
    ticket_price = fans_amount * 499.99
elif ticket_category == "Normal":
    ticket_price = fans_amount * 249.99

if budget >= ticket_price:
    print(f"Yes! You have {budget - ticket_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {ticket_price - budget:.2f} leva.")
