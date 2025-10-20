actor_name = input()
point_from_academy = float(input())
jury_amount = int(input())

points_awarded = 0
final_score = point_from_academy

for i in range(1, jury_amount + 1):
    jury_name = input()
    jury_points = float(input())

    points_awarded = len(jury_name) * jury_points / 2

    final_score += points_awarded

    if final_score > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {final_score:.1f}!")
        break
    else:
        pass

if final_score <= 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - final_score:.1f} more!")
