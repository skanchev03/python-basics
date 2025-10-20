floors = int(input())
rooms = int(input())

max_floor = floors + 1

for i in range(floors, 0, -1):
    max_floor -= 1
    print()
    for j in range(0, rooms):
        if max_floor == floors:
            print(f"L{i}{j}", end=" ")
        else:
            if i % 2 == 0:
                print(f"O{i}{j}", end=" ")
            else:
                print(f"A{i}{j}", end=" ")
