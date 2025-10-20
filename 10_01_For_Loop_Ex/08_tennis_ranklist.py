from math import floor

tournaments_amount = int(input())
starting_points = int(input())

final_points = starting_points

wins = 0

for i in range (1, tournaments_amount + 1):
    stage = input()

    if stage == "W":
        final_points += 2000
        wins += 1
    elif stage == "F":
        final_points += 1200
    elif stage == "SF":
        final_points += 720

print(f"Final points: {final_points}")
print(f"Average points: {floor((final_points - starting_points) / tournaments_amount)}")
print(f"{wins / tournaments_amount * 100:.2f}%")
