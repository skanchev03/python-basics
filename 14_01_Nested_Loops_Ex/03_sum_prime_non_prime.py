non_prime_sum = 0
prime_sum = 0

while True:
    num = input()
    counter = 0

    if num == "stop":
        break

    if int(num) < 0:
        print("Number is negative.")

    if int(num) < 0:
        continue

    for i in range(1, int(num) + 1):
        if int(num) % i == 0:
            counter += 1

    if counter >= 3:
        non_prime_sum += int(num)
    else:
        prime_sum += int(num)

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
