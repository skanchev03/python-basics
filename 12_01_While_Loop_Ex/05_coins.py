change = float(input())
change *= 100

coins_counter = 0

while change >= 200:
    change -= 200
    coins_counter += 1

while change >= 100:
    change -= 100
    coins_counter += 1

while change >= 50:
    change -= 50
    coins_counter += 1

while change >= 20:
    change -= 20
    coins_counter += 1

while change >= 10:
    change -= 10
    coins_counter += 1

while change >= 5:
    change -= 5
    coins_counter += 1

while change >= 2:
    change -= 2
    coins_counter += 1

while change >= 1:
    change -= 1
    coins_counter += 1

print(coins_counter)
