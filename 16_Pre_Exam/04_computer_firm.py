n = int(input())

average_rating = 0
total_sales = 0

for i in range(1, n + 1):
    number = int(input())
    str_number = str(number)
    rating = int(str_number[2])
    average_rating += rating
    sales = 0

    if rating == 2:
        possible_sales = str_number[0] + str_number[1]
        possible_sales = int(possible_sales)
        sales = 0
    elif rating == 3:
        possible_sales = str_number[0] + str_number[1]
        possible_sales = int(possible_sales)
        sales = 0.5 * possible_sales
    elif rating == 4:
        possible_sales = str_number[0] + str_number[1]
        possible_sales = int(possible_sales)
        sales = 0.7 * possible_sales
    elif rating == 5:
        possible_sales = str_number[0] + str_number[1]
        possible_sales = int(possible_sales)
        sales = 0.85 * possible_sales
    elif rating == 6:
        possible_sales = str_number[0] + str_number[1]
        possible_sales = int(possible_sales)
        sales = possible_sales

    total_sales += sales

print(f"{total_sales:.2f}")
print(f"{average_rating / n:.2f}")
