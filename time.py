import math

first_time = int(input())
second_time = int(input())
third_time = int(input())

sum_time = first_time + second_time + third_time
minutes = sum_time // 60
seconds = sum_time % 60

minutes = math.floor(minutes) # rounds a number # DOWN to the nearest
# integer, if necessary, and returns the result
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print((f'{minutes}:{seconds}'))
