number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())
chicken_price = 10.35
fish_price = 12.40
vegetarian_price = 8.15
sum_menu = number_chicken_menu * chicken_price \
+ number_fish_menu * fish_price + \
number_vegetarian_menu * vegetarian_price

dessert = sum_menu * 0.2
all_price = sum_menu + dessert + 2.5
print(all_price)
