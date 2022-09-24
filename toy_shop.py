needed_money = float(input())
puzzles = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

total_sum = puzzles * 2.6 + doll * 3 + \
    bear * 4.10 + minion * 8.20 + truck * 2

total_toys = puzzles + doll + bear + minion + truck

if total_toys >= 50:
    total_sum = total_sum * 0.75
total_sum = total_sum * 0.9
differennce = abs(total_sum - needed_money)  # abs - abstact demek kakwoto i da e chisloto shte go vyrne polojitelno
if total_sum >= needed_money:
    print(f'Yes! {differennce:.2f} lv left.')
else:
    print(f"Not enough money! {differennce:.2f} lv needed.")