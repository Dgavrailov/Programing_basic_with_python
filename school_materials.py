number_of_pens = int(input())
number_of_markers = int(input())
liters_of_detergent = int(input())
percest_discount = int(input())
price_of_pen = 5.8
price_of_markers = 7.2
price_of_liters_detergent = 1.2
needed_sum = number_of_pens * price_of_pen + \
             number_of_markers * price_of_markers \
             + liters_of_detergent * price_of_liters_detergent
needed_sum = needed_sum - needed_sum * (percest_discount / 100)
print(needed_sum)
