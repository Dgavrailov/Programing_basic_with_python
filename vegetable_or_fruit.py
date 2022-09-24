type_of_product = input().lower()

# kogato e .lower, pri izpylnenie na zadachata vsichki bukvi shte gi izkara
# sys malyk znak S = s ...

if type_of_product == 'banana' or type_of_product == 'apple' \
    or type_of_product == 'kiwi' or type_of_product == 'cherry' \
    or type_of_product == 'lemon' or type_of_product == 'grapes':
    print('fruit')
elif type_of_product == 'tomato' or type_of_product == 'cucumber' or \
     type_of_product == 'pepper' or type_of_product == 'carrot':
    print('vegetable')
else:
    print('unknown')

#if type_of_product == ['banana','apple', 'kiwi', 'cherry']
# print(fruit)
# i taka stava


