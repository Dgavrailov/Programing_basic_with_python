#[2, 3, 4, 5] # ( tova e list of objects)

def multiply(*numbers): # ako iskame da umnojim poveche ot 2 chisla
    #ako iskame 2 - def multiply(x, y):
    total = 1
    for number in numbers:
        total = total * number
    return(total)



print(multiply(2, 3, 4, 5))
