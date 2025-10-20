student_counter = 0
standard_counter = 0
kid_counter = 0
total_counter = 0

while True:
    movie = input()
    counter = 0

    if movie == "Finish":
        break

    capacity = int(input())

    for i in range(1, capacity + 1):
        ticket = input()

        if ticket == "End":
            break
        if ticket == "student":
            student_counter += 1
        if ticket == "standard":
            standard_counter += 1
        if ticket == "kid":
            kid_counter +=1

        counter += 1
        total_counter += 1

    print(f"{movie} - {counter / capacity * 100:.2f}% full.")

print(f"Total tickets: {total_counter}")
print(f"{student_counter / total_counter * 100:.2f}% student tickets.")
print(f"{standard_counter / total_counter * 100:.2f}% standard tickets.")
print(f"{kid_counter / total_counter * 100:.2f}% kids tickets.")
