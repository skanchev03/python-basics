n = int(input())

for num in range(1000,10000):
    num_str = str(num)
    valid = True
    sum_1 = 0
    sum_2 = 0

    for index, digit in enumerate(num_str):
        if int(digit) == 0:
            valid = False
            continue

        if int(index) < 2:
            sum_1 += int(digit)
        else:
            sum_2 += int(digit)

    if n % sum_1 == 0 and sum_1 == sum_2 and valid:
        print(num, end=" ")
