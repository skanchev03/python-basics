bad_grades_limit = int(input())

average_grade = 0
grades_counter = 0
last_problem = " "
bad_grade_counter = 0

while True:
    task_name = input()

    if task_name == "Enough":
        print(f"Average score: {average_grade / grades_counter:.2f}")
        print(f"Number of problems: {grades_counter}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    average_grade += grade
    grades_counter += 1
    last_problem = task_name

    if grade <= 4:
        bad_grade_counter += 1
        if bad_grade_counter == bad_grades_limit:
            print(f"You need a break, {bad_grades_limit} poor grades.")
            break
