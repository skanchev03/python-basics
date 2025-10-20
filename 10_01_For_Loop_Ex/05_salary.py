tabs_open = int(input())
salary = int(input())

for i in range(1, tabs_open + 1):
    site = input()

    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "Reddit":
        salary -= 50
    else:
        pass

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
