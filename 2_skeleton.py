minutes_of_control = int(input())
seconds_of_control = int(input())
the_lenght_of_the_chute_in_meters = float(input())
seconds_to_go_100_meters = int(input())

control_in_seconds = minutes_of_control * 60 + seconds_of_control
number_of_times_reduction = the_lenght_of_the_chute_in_meters / 120
total_time_reduction = number_of_times_reduction * 2.5

time_of_marin = (the_lenght_of_the_chute_in_meters / 100 * seconds_to_go_100_meters - total_time_reduction)

if control_in_seconds >= time_of_marin:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_of_marin:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(time_of_marin - control_in_seconds):.3f} second slower.")
