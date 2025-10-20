students = int(input())

average_counter = 0
fail_counter = 0
three_counter = 0
four_counter = 0
top_counter = 0

for i in range(1, students + 1):
    grade = float(input())

    average_counter += grade

    if grade < 3:
        fail_counter += 1
    elif grade < 4:
        three_counter += 1
    elif grade < 5:
        four_counter += 1
    else:
        top_counter += 1

print(f"Top students: {top_counter / students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {four_counter / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {three_counter / students * 100:.2f}%")
print(f"Fail: {fail_counter / students * 100:.2f}%")
print(f"Average: {average_counter / students:.2f}")
