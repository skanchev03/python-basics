days_stay = int(input())
type_of_room = input()
rating = input()

days_stay -= 1

room_for_one_person_price = 18
apartment_price = 25
president_apartment_price = 35

if days_stay < 10:
    apartment_price *= 0.7
    president_apartment_price *= 0.9
elif 10 <= days_stay <= 15:
    apartment_price *= 0.65
    president_apartment_price *= 0.85
elif days_stay > 15:
    apartment_price *= 0.5
    president_apartment_price *= 0.8

room_for_one_person_price *= days_stay
apartment_price *= days_stay
president_apartment_price *= days_stay

if rating == "positive":
    room_for_one_person_price *= 1.25
    apartment_price *= 1.25
    president_apartment_price *= 1.25
elif rating == "negative":
    room_for_one_person_price *= 0.9
    apartment_price *= 0.9
    president_apartment_price *= 0.9

if type_of_room == "room for one person":
    print(f"{room_for_one_person_price:.2f}")
elif type_of_room == "apartment":
    print(f"{apartment_price:.2f}")
elif type_of_room == "president apartment":
    print(f"{president_apartment_price:.2f}")
