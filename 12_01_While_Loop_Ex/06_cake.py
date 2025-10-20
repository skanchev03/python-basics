cake_length = int(input())
cake_width = int(input())
cake_size = cake_length * cake_width

pieces_counter = 0

while True:
    pieces = input()

    if pieces != "STOP":
        pieces_counter += int(pieces)

    if pieces_counter >= cake_size:
        print(f"No more cake left! You need {pieces_counter - cake_size} pieces more.")
        break

    if pieces == "STOP":
        print(f"{cake_size - pieces_counter} pieces are left.")
        break
