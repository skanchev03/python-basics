start = int(input())
end = int(input())
magic_num = int(input())

counter = 0
valid = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        counter += 1
        if i + j == magic_num:
            print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
            valid = True
            break
    if valid:
        break

if not valid:
    print(f"{counter} combinations - neither equals {magic_num}")
