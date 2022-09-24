old_record_in_secundes = float(input())
distance = float(input())
time_per_meter = float(input())
delay = (distance // 15) * 12.5
total_time = (distance * time_per_meter) + delay

if total_time < old_record_in_secundes:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    seconds = total_time - old_record_in_secundes
    print(f'No, he failed! He was {seconds:.2f} seconds slower.')

