sum_of_prime_number = 0
sum_of_non_prime_number = 0
command = input() #komanda stop)
while command != "stop":
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
    else:
        current_number_is_prime = True
        for number in range(2, current_number): # dali e prosto ili ne
            if current_number % number == 0: # tova pokazva che chisloto ne e prosto
                current_number_is_prime = False
                break
        if current_number_is_prime: #   if current_number_is_prime == True:
            sum_of_prime_number += current_number #chisloto e prosto
        else:
            sum_of_non_prime_number += current_number

    command = input
print (f'Sum of all prime numbers is: {sum_of_prime_number}')
print(f"Sum of all non prime numbers is: {sum_of_non_prime_number}")