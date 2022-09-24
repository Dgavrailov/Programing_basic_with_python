sum_of_balls = int(input())

red = 0
orange = 0
yellow = 0
white = 0
black = 0
other_color = 0

total_points = 0
for _ in range(sum_of_balls):
    color_of_ball = input()
    if color_of_ball == "red":
        red += 1
        total_points += 5
    elif color_of_ball == "orange":
        orange += 1
        total_points += 10
    elif color_of_ball == "yellow":
        yellow += 1
        total_points += 15
    elif color_of_ball == "white":
        white += 1
        total_points += 20
    elif color_of_ball == "black":
        black += 1
        total_points = int(total_points / 2)
    else:
        other_color += 1

print(f"Total points: {total_points}")

print(f"Red balls: {red}")

print(f"Orange balls: {orange}")

print(f"Yellow balls: {yellow}")

print(f"White balls: {white}")

print(f"Other colors picked: {other_color}")

print(f"Divides from black balls: {black}")