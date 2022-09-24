change = float(input())
change *= 100
coins_counter = 0

while change > 0:
    if change - 200 >= 0:
        coins_counter += 1
        change -= 200
    elif change - 100 >= 0:
        coins_counter += 1
        change -= 100
 # и така нататък