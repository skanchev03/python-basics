men = int(input())
women = int(input())
tables = int(input())

tables_counter = 0
full = False

for i in range(1, men + 1):
    for j in range(1, women + 1):
        print(f"({i} <-> {j})",end=" ")
        tables_counter += 1

        if tables_counter >= tables:
            full = True
            break
    if full:
        break
