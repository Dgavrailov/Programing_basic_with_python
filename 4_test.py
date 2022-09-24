#Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си. Напишете програма,
# която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато постигне целта си да
# се изписва "Goal reached! Good job!" и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
#Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките,
# които е извървяла докато се прибира. След което, ако не е успяла да постигне целта си,
# на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."


target_steps = 10000
total_steps = 0
while total_steps < target_steps:
    current_steps = input()
    if current_steps != "Going home":
        command = int(current_steps)
        total_steps += command
    else:
        last_steps = int(input())
        total_steps += last_steps
        break
diff = abs(total_steps - target_steps)

if target_steps > total_steps:
    print(f"{diff} more steps to reach goal.")
else:
    print("Goal reached! Good job!" )
    print(f"{diff} steps over the goal!")