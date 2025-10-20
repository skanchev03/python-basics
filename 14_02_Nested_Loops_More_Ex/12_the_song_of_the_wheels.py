magic_num = int(input())

password_counter = 0
four_combinations = False
password = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and a*b + c*d == magic_num:
                    print(f"{a}{b}{c}{d}",end=" ")
                    password_counter += 1
                    if password_counter == 4:
                        four_combinations = True
                        password = a * 1000 + b * 100 + c * 10 + d

if not four_combinations:
    print()
    print("No!")
else:
    print()
    print(f"Password: {password}")
