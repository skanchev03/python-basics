n1 = int(input())
n2 = int(input())
operator = input()

result = 0

if operator == "+":
    result = n1 + n2

    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")

if operator == "-":
    result = n1 - n2

    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")

if operator == "*":
    result = n1 * n2

    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")

if operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} / {n2} = {n1 / n2:.2f}" )

if operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} % {n2} = {n1 % n2}")
