month = input()
nights = int(input())
type_of_room = str
price = 0

if month == "May" or month == "October":
    if type_of_room == "studio":
        price = 50
        if nights > 7:
            nights_price = price * nights
    elif type_of_room == "apartment":
        price = 65
        if nights > 7:


elif month == "June" or month == "September":
    if type_of_room == "studio":
        price = 75.2
    elif type_of_room == "apartment":
        price = 68.7

elif month == "July" or month == "August":
    if type_of_room == "studio":
        price = 76
    elif type_of_room == "apartment":
        price = 77

nights_price = price * nights

