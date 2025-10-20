money_needed = int(input())

price_counter = 0
cash_counter = 0
cash_payments_counter = 0
card_counter = 0
card_payments_counter = 0
transaction_counter = 0

while True:
    price = input()

    if price == "End":
        print("Failed to collect required money for charity.")
        break

    transaction_counter += 1

    if transaction_counter == 1:
        if int(price) > 100:
            print("Error in transaction!")
        else:
            if price != "End":
                price_counter += int(price)
                cash_counter += int(price)
                cash_payments_counter += 1
                print("Product sold!")

    if transaction_counter == 2:
        transaction_counter = 0

        if int(price) < 10:
            print("Error in transaction!")
        else:
            if price != "End":
                price_counter += int(price)
                card_counter += int(price)
                card_payments_counter += 1
                print("Product sold!")

    if price_counter >= money_needed:
        print(f"Average CS: {cash_counter / cash_payments_counter:.2f}")
        print(f"Average CC: {card_counter / card_payments_counter:.2f}")
        break
