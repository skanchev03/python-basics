money_needed = float(input())
capital = float(input())

days_counter = 0
days_spend_counter = 0

while True:
    action = input()
    money_used = float(input())
    days_counter +=1

    if action == "spend":
        days_spend_counter += 1
        if money_used >= capital:
            capital = 0
        else:
            capital -= money_used

    if action == "save":
        days_spend_counter = 0
        capital += money_used

    if days_spend_counter == 5:
        print("You can't save the money.")
        print(days_counter)
        break

    if capital >= money_needed:
        print(f"You saved the money for {days_counter} days.")
        break
