kg_vegetables_price = float(input())
kg_fruits_price = float(input())
sum_kg_vegetable = int(input())
sum_kg_fruits = int(input())
sum_price_vegetables = sum_kg_vegetable * kg_vegetables_price / 1.94
sum_price_fruits = sum_kg_fruits * kg_fruits_price / 1.94
price = sum_price_fruits + sum_price_vegetables

print(f'{price:.2f}')


