starting_num = int(input())

counter = 0

while True:
    num = int(input())
    counter += num

    if counter >= starting_num:
        print(counter)
        break
