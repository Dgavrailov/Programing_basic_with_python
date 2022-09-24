#We use a for loop when we want to
# repeat a code block a fixed number of times.

#In Python, the for loop is used to iterate over a sequence
# such as a list, string, tuple, other iterable objects such as range.

sum = 0
for i in range(2, 22, 2): #Use to get all even numbers from 2 to 20.
    #Here a step value is 2 to get the even number
    sum = sum + i   #In each iteration add the current number to the
                    # sum variable using the arithmetic operator.
print(sum)