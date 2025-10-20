first_pair_start = int(input())
second_pair_start = int(input())
first_pair_diff = int(input())
second_pair_diff = int(input())

divisor = 1
first_pair_counter = 0
first_pair_primal = False
second_pair_counter = 0
second_pair_primal = False

for i in range(first_pair_start, first_pair_start + first_pair_diff + 1):
    for j in range(second_pair_start, second_pair_start + second_pair_diff + 1):
        for div_one in range(1, i + 1):
            if i % div_one == 0:
                first_pair_counter += 1

        if first_pair_counter <= 2:
            first_pair_primal = True

        for div_two in range(1, j + 1):
            if j % div_two == 0:
                second_pair_counter += 1

        if second_pair_counter <= 2:
            second_pair_primal = True

        if first_pair_primal and second_pair_primal:
            print(f"{i}{j}")

        first_pair_counter = 0
        first_pair_primal = False
        second_pair_counter = 0
        second_pair_primal = False
