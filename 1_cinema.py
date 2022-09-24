type_of_projekciq = input()
rows = int(input())
columns = int(input())
total_places = rows * columns
price = 0
if type_of_projekciq == "Premiere":
    price = 12
elif type_of_projekciq == "Normal":
    price = 7.5
elif type_of_projekciq == "Discount":
    price = 5

total_sum = total_places * price
print(f'{total_sum:.2f} leva')
