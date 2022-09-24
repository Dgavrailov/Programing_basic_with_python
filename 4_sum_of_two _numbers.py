start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
flag = False
combination = 0
for num1 in range(start_interval, end_interval + 1):
    for num2 in range(start_interval, end_interval + 1):
        combination += 1
        if num1 + num2 == magic_number:
            flag = True
            print(f"Combination N:{combination} ({num1} + {num2} = {magic_number})")
            break
    if flag:
        break
if not flag:
    print(f'{combination} combinations - neither equals {magic_number}')