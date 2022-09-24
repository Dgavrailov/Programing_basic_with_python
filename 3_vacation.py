needed_money = float(input()) # Пари, които са и нужни за екскурзия
money_in_hand = float(input()) # пари в нея
spending_counter = 0
total_days_counter = 0 #колко дни
spending_too_many_days = False
while money_in_hand < needed_money: # докато парите в нея не станат достатъчни за екскурзията
    action = input() #•	Вид действие – текст с две възможности: "spend" или "save"
    current_sum = float(input()) #	Сумата, която ще спести/похарчи - реално число.
    total_days_counter += 1
    if action == "spend":
        spending_counter += 1 # ден + ден в който тя харчи
        if spending_counter == 5: #ако дните, които тя харчи станат 5
            spending_too_many_days = True
            break
            #Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и
            # ще ѝ останат 0 лева
        money_in_hand -= current_sum
        if money_in_hand < 0:
            money_in_hand = 0
    else: #action == save
        money_in_hand += current_sum # ако парите стигат, то тогава
        spending_counter = 0 # ако досега са се насъбрали в spending_counter поредни дни в action = "spend" то
        # така зануляваме брояча до получаване на пет поредни думи spend Или Save
if spending_too_many_days:         #•	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише
       print("You can't save the money.")
       print(f"{total_days_counter}")
else:
    print(f"You saved the money for {total_days_counter} days.")
