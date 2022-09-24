first_time = int(input())
second_time = int(input())
third_time = int(input())
sum_time = first_time + second_time + third_time
minutes = sum_time // 60 # naprimer 350 sekundi - 350/60 = 300 (ostatuk 50) => taka poluchavame minutite
seconds = sum_time % 60 # napr 350 sek - 350 / 60 = 300 + ostatyk 50 i ot tuk vzimame sekundite

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')