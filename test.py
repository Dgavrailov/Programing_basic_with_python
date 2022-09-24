#x = 11
#while x > 1: x -= 1; print(x)


#ДВОЙКАТА ИЗЧЕЗВА:
#counter = 0

#while counter < 5:
#    counter += 1
#    if counter == 2:
#       continue

#    print(counter)

#НАПРИМЕР КОГАТО ИСКАМЕ ДА НЕ ПРИНТИРАМЕ ЧЕТНИ ЧИСЛА:
counter = 0

while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print(counter)