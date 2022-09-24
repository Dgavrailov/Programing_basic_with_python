number_of_breads = int(input())
best_baker = ""
best_baker_score = 0


for count in range(number_of_breads):
    name_of_baker = input()
    current_score = 0
    while True:
        command = input()
        if command == "Stop":
           print(f"{name_of_baker} has {current_score} points.")
           break
        points = int(command)
        current_score += points
    if current_score > best_baker_score:
        best_baker_score = current_score
        best_baker = name_of_baker
        print(f"{name_of_baker} is the new number 1!")
print(f'{best_baker} won competition with {best_baker_score} points!')
