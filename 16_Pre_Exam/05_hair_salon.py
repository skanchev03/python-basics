goal = int(input())
earned = 0

while True:
    if earned >= goal:
        break

    service = input()

    if service == "closed":
        break

    elif service == "haircut":
        kind_of_haircut = input()

        if kind_of_haircut == "mens":
            earned += 15
        elif kind_of_haircut == "ladies":
            earned += 20
        elif kind_of_haircut == "kids":
            earned += 10

    elif service == "color":
        color = input()

        if color == "touch up":
            earned += 20
        elif color == "full color":
            earned += 30

if earned >= goal:
    print("You have reached your target for the day!")
    print(f"Earned money: {earned}lv.")
else:
    print(f"Target not reached! You need {goal - earned}lv. more.")
    print(f"Earned money: {earned}lv.")
