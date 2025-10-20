n = int(input())

counter = 1
valid = False

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if counter > n:
            valid = True
            break
        print((str(counter)), end=" ")
        counter += 1
    if valid:
        break
    print()
