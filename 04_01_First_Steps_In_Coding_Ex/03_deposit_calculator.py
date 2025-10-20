deposited_sum = float(input())
duration_of_deposit = int(input())
yearly_interest = float(input())

final_sum = deposited_sum + duration_of_deposit * ((deposited_sum * (yearly_interest / 100)) / 12)
print(final_sum)
