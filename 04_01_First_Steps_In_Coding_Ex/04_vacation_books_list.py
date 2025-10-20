amount_of_pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

days_needed = ((amount_of_pages // pages_per_hour) // days_to_read)
print(days_needed)
