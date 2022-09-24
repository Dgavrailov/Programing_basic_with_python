city = input()
type_of_packet = input()
vip_sale = input()
number_of_days = int(input())

value = 0
if city == "Bansko" or city == "Borovets":
    if type_of_packet == "withEquipment":
        value = 100 * number_of_days
        if vip_sale == "yes":
            value *= 0.9
    elif type_of_packet == "noEquipment":
        value = 80 * number_of_days
        if vip_sale == "yes":
            value *= 0.95

if city == "Varna" or "Burgas":
    if type_of_packet == "noBreakfast":
        value = 100 * number_of_days
        if vip_sale == "yes":
            value *= 0.93
    elif type_of_packet == "withBreakfast":
        value = 130 * number_of_days
        if vip_sale == "yes":
            value *= 0.88


if number_of_days < 1:
    print(f'Days must be positive number!')
elif city != 'Bansko' and city != 'Borovets' and city != 'Varna' and city != 'Burgas':
    print(f'Invalid input!')

else:
    print(f"The price is {value:.2f}lv! Have a nice time!")