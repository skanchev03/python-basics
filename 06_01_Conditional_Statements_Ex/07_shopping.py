budget = float(input())
video_card_amount = int(input())
processor_amount = int(input())
ram_amount = int(input())

video_card_price = 250
processor_price = video_card_amount * video_card_price * 0.35
ram_price = video_card_amount * video_card_price * 0.10

total_price = video_card_amount * video_card_price + processor_amount * processor_price + ram_amount * ram_price

if video_card_amount > processor_amount:
    total_price = total_price * 0.85

if budget >= total_price:
    print(f'You have {abs(budget - total_price):.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(budget - total_price):.2f} leva more!')
