dep_sum = float(input())
dead_end_deposit = int(input())
year_interest_percentage = float(input())
year_interest_percentage = dep_sum * year_interest_percentage / 100
monthly_interest = year_interest_percentage / 12
sum = dep_sum + dead_end_deposit * monthly_interest
print(sum)
