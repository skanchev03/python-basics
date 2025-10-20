juniors = int(input())
seniors = int(input())
racetrack = input()

donation = 0
racers = juniors + seniors

if racetrack == "trail":
    donation = (juniors * 5.5 + seniors * 7) * 0.95
elif racetrack == "cross-country":
    if racers < 50:
        donation = (juniors * 8 + seniors * 9.5) * 0.95
    else:
        donation = (juniors * 8 + seniors * 9.5) * 0.75 * 0.95
elif racetrack == "downhill":
    donation = (juniors * 12.25 + seniors * 13.75) * 0.95
elif racetrack == "road":
    donation = (juniors * 20 + seniors * 21.5) * 0.95

print(f"{donation:.2f}")
