jury = int(input())
average = 0
presentation_amount = 0

while True:
    presentation_name = input()
    grades_counter = 0

    if presentation_name == "Finish":
        break

    for i in range(1, jury+1):
        grade = float(input())
        grades_counter += grade
        average += grade

    print(f"{presentation_name} - {grades_counter / jury:.2f}.")
    presentation_amount += 1

print(f"Student's final assessment is {average / (presentation_amount * jury):.2f}.")
