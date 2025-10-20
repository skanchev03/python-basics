bottles_of_cleaner = int(input())

cleaner_amount = bottles_of_cleaner * 750

type_of_dishes_counter = 0
plates_counter = 0
pans_counter = 0
dishes_counter = 0

while True:
    dishes = input()
    type_of_dishes_counter += 1

    if type_of_dishes_counter < 3:
        if dishes != "End":
            dishes_counter += int(dishes) * 5
            plates_counter += int(dishes)

    if type_of_dishes_counter == 3:
        type_of_dishes_counter = 0
        if dishes != "End":
            dishes_counter += int(dishes) * 15
            pans_counter += int(dishes)

    if dishes == "End":
        print("Detergent was enough!")
        print(f"{plates_counter} dishes and {pans_counter} pots were washed.")
        print(f"Leftover detergent {cleaner_amount - dishes_counter} ml.")
        break

    if cleaner_amount < dishes_counter:
        print(f"Not enough detergent, {dishes_counter - cleaner_amount} ml. more necessary!")
        break
