actor_name = input()
academy_points = float(input())
number_of_jury = int(input())
total_points = academy_points

#На следващите n-на брой реда:
#	Име на оценяващия - текст
#	Точки от оценяващия - реално число в интервала [1.0... 50.0]

for current_grade in range(number_of_jury):
    current_jury_name = input()
    current_points = float(input())
    current_final_points = len(current_jury_name) * current_points / 2
    total_points += current_final_points
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")