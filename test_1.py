

#for hours in range(0, 24):
#    for minutes in range(0, 60):
#        for seconds in range(0, 60):
#            print(f'{hours}:{minutes:02d}:{seconds:02d}')
#            if hours == 5:
#            break # nqma da printira minutite ot 5 chasa do 6
#        if hours == 5:
#        break#

flag = False
for h in range(0, 24):
    for m in range(0, 60):
        print(f'{h}:{m}')
        if h == 5:
            flag - True
            break
    if h == 5:
        flag = True
        break # колкото фор-а имаме толкова брейкове трябва да има
        
