size_of_eggs = input()
color_of_eggs = input()
number_of_batch = int(input())

total_sum = 0

if size_of_eggs == "Large":
    if color_of_eggs == "Red":
        total_sum = number_of_batch * 16
    elif color_of_eggs == "Green":
        total_sum = number_of_batch * 12
    elif color_of_eggs == "Yellow":
            total_sum = number_of_batch * 9
elif size_of_eggs == "Medium":
    if color_of_eggs == "Red":
        total_sum = number_of_batch * 13
    elif color_of_eggs == "Green":
        total_sum = number_of_batch * 9
    elif color_of_eggs == "Yellow":
            total_sum = number_of_batch * 7

elif size_of_eggs == "Small":
    if color_of_eggs == "Red":
        total_sum = number_of_batch * 9
    elif color_of_eggs == "Green":
        total_sum = number_of_batch * 8
    elif color_of_eggs == "Yellow":
            total_sum = number_of_batch * 5
taxes = total_sum * 0.35
total_sum -= taxes
print(f'{total_sum:.2f} leva.')
