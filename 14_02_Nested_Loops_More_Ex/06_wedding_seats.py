last_sector = input()
first_rows = int(input())
odd_seats = int(input())

r_rows = first_rows - 1
counter = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    r_rows = r_rows + 1
    for rows in range(1, r_rows + 1):
        if rows % 2 == 0:
            s_seats = odd_seats + 2
        else:
            s_seats = odd_seats
        for seats in range(1, s_seats + 1):
            print(f"{chr(sector)}{rows}{chr(seats + 96)}")
            counter += 1
print(counter)
