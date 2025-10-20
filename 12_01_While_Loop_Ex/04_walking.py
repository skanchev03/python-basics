steps_counter = 0

while True:
    steps = input()
    if steps == "Going home":
        pass
    else:
        steps_counter += int(steps)

    if steps_counter >= 10000:
        print("Goal reached! Good job!")
        print(f"{steps_counter - 10000} steps over the goal!")
        break

    if steps == "Going home":
        steps = input()
        steps_counter += int(steps)

        if steps_counter >= 10000:
            print("Goal reached! Good job!")
            print(f"{steps_counter - 10000} steps over the goal!")
        else:
            print(f"{10000 - steps_counter} more steps to reach goal.")
        break
