import random
from string import digits, punctuation, ascii_lowercase, ascii_uppercase

all_comninations_from_digits_letters_punctuations = digits + punctuation + ascii_lowercase + ascii_uppercase
password_lenght = int(input('enter the password by lenght'))

password = ''.join(random.sample(all_comninations_from_digits_letters_punctuations))