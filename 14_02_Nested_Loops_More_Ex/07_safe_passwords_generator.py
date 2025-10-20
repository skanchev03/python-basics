a = int(input())
b = int(input())
max_pass = int(input())

leave = False
first_symbol = 35
second_symbol = 64
pass_counter = 0

while True:
    for i in range(1, a + 1):
        if leave:
            break
        for j in range(1, b + 1):
            if pass_counter >= max_pass:
                leave = True
                break
            if first_symbol > 55:
                first_symbol = 35
            if second_symbol > 96:
                second_symbol = 64

            print(f"{chr(first_symbol)}{chr(second_symbol)}{i}{j}{chr(second_symbol)}{chr(first_symbol)}",end="|")
            first_symbol += 1
            second_symbol += 1
            pass_counter +=1
    break
