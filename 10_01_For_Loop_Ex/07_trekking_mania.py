groups_amount = int(input())

total_hikers = 0
counter_1 = 0
counter_2 = 0
counter_3= 0
counter_4 = 0
counter_5 = 0

for i in range(1, groups_amount + 1):
    group_size = int(input())
    total_hikers += group_size

    if group_size <= 5:
        counter_1 += group_size
    elif group_size <= 12:
        counter_2 += group_size
    elif group_size <= 25:
        counter_3 += group_size
    elif group_size <= 40:
        counter_4 += group_size
    elif group_size > 40:
        counter_5 += group_size

print(f"{counter_1 / total_hikers * 100:.2f}%")
print(f"{counter_2 / total_hikers * 100:.2f}%")
print(f"{counter_3 / total_hikers * 100:.2f}%")
print(f"{counter_4 / total_hikers * 100:.2f}%")
print(f"{counter_5 / total_hikers * 100:.2f}%")
