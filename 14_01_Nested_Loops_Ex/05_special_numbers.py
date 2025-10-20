n = int(input())

for num in range(1111, 10000):
    num_str = str(num)
    valid = False

    for index, digit in enumerate(num_str):
        if int(digit) == 0 or n % int(digit) != 0:
            valid = True
            break
    if not valid:
        print(num, end=" ")
