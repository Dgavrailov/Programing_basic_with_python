# x * 1.1 = x + 10% ot x
#y * 1.2 = y + 20% ot y
# [1...10] ot 1 do 10
# [1...10 ot 1 do 9

nailon_quantity = int(input())
paint_quantity = int(input())
razreditel_quantity = int(input())
hours = int(input())
nailon_price = 1.50
paint_price = 14.50
razreditel_price = 5
bags_price = 0.40
materials_price = (nailon_quantity + 2) * nailon_price \
    + paint_quantity * 1.1 * paint_price   \
    + razreditel_quantity * razreditel_price \
    + bags_price
salary = materials_price * 0.3 + hours
all_sum = materials_price + salary
print(all_sum)