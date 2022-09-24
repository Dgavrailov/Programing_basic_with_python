numbers = int(input())
even_num = 0
odd_num = 0


for i in range(1, numbers + 1):
    element = int(input())
    if i % 2 == 0:
        even_num += element
    else:
        odd_num += element
if even_num == odd_num:
    print("Yes")
    print(f"Sum = {even_num}")
else:
    diff = abs(even_num -odd_num)
    print("No")
    print(f"Diff = {diff}")
