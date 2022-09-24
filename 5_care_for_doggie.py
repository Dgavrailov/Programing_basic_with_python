buyed_food_for_the_dog_kg = int(input())
buyed_food_for_the_dog_gr = buyed_food_for_the_dog_kg * 1000

while True:
    eaten_food = input()
    if eaten_food == 'Adopted':
        break
    total = int(eaten_food)
    buyed_food_for_the_dog_gr -= total
if buyed_food_for_the_dog_gr >= 0:
    print(f"Food is enough! Leftovers: {buyed_food_for_the_dog_gr} grams.")
else:
    print(f"Food is not enough. You need {abs(buyed_food_for_the_dog_gr)} grams more.")
