weight = int(input("weight: "))
unit = str(input("(K)g or (L)bs: "))

if unit.upper() == "K":
    converted = weight / 0.45
    print('weight in Lbs = ' + str(converted))
else:
    converted = weight * 0.45
    print('weight in Kg =' + str(converted))