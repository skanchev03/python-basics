n = int(input())

counter = 0
sum_1 = 0
sum_2 = 0
diff = 0
max_diff = 0

for i in range(1, n * 2 + 1):
    num = int(input())

    counter += 1

    if counter == 1 or counter == 2:
        sum_1 += num

    if counter == 3 or counter == 4:
        sum_2 += num
        if counter == 4:
            counter = 2

            if sum_1 == sum_2:
                sum_2 = 0
            else:
                diff = abs(sum_1 - sum_2)
                sum_1 = sum_2
                sum_2 = 0

                if diff > max_diff:
                    max_diff = diff
                else:
                    pass

if diff == 0:
    print(f"Yes, value={sum_1}")
else:
    print(f"No, maxdiff={max_diff}")
