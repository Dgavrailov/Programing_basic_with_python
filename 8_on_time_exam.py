time_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

time_of_exam = time_of_exam * 60 + minutes_of_exam
time_of_arrival = hour_of_arrival * 60 + minutes_of_arrival

if time_of_arrival > time_of_exam:
    print('Late')

elif time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print("On time")
else:
    print("Early")
difference = abs(time_of_exam - time_of_arrival)

hours = difference // 60
minutes = difference % 60

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f'{minutes} minutes before the start')
elif time_of_arrival < time_of_exam:
    time_of_arrival <= time_of_exam - 60
    # if minutes < 10
    #   print (f' {hours}:0{minutes}...
        #else:
        # print (f' {hours}:{minutes} ho
    print(f'{hours}:{minutes:02d} hours before the start')
elif time_of_exam < time_of_arrival < time_of_exam + 60:
    print(f'{minutes}minutes after the start')
elif time_of_exam + 60 <= time_of_arrival:
        print(f'{hours}:{minutes:02d} after the start')