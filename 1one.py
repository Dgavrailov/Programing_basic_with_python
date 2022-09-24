import math

number_of_people = int(input())
entry_tax = float(input())
price_of_1_shezlong = float(input())
price_of_1_chadyr = float(input())

entry_total = entry_tax * number_of_people


sum_shezlong = number_of_people * 0.75
shezlong_total = (math.ceil(sum_shezlong)) * price_of_1_shezlong


chadur = number_of_people * 0.5
chadur_total = math.ceil(chadur) * price_of_1_chadyr

total = entry_total + shezlong_total + chadur_total
print(f'{total:.2f}')
