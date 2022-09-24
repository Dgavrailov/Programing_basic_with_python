# kolko litra boq e nujna

# za stenite zelena. 1lityr = 3.4kv.m,

# za pokriva chervena 1l = 4.3 kv.m

x = float(input())
y = float(input())
h = float(input())
# ЗЕЛЕНА БОЯ СТЕНИ
front_wall = x * x - (1.2 * 2)
back_wall = x * x
left_and_right_wall = 2 * x * y - (2 * 1.5 * 1.5)
# ЧЕРВЕНА БОЯ ПОКРИВ
roof_left_and_right = 2 * x * y
roof_front_and_back =2 * x * h / 2

green_paint = (front_wall + back_wall + left_and_right_wall) / 3.4
red_paint = (roof_front_and_back + roof_left_and_right) / 4.3
print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')