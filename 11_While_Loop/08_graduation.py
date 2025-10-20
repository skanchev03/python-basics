name = input()

good_year_counter = 0
bad_year_counter = 0
average_grade = 0

while True:
    grade = float(input())

    if grade < 4:
        bad_year_counter += 1

        if bad_year_counter == 2:
            print(f"{name} has been excluded at {good_year_counter + 1} grade")
            break
    else:
        good_year_counter += 1
        average_grade += grade

    if good_year_counter == 12:
        break

if bad_year_counter != 2:
    print(f"{name} graduated. Average grade: {average_grade / 12:.2f}")
