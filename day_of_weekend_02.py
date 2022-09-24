day_of_week = input()


if day_of_week == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday':
    print('Working day')
elif day_of_week == 'Saturday' or 'Sunday':
    print('Weekend')

else:
    print('Error')