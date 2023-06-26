import random
import string

def generator(length, lc, uc, spec, numbs):
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    special_chars = string.punctuation
    numbers = string.digits

    password = ""

    for _ in range(lc):
        password += random.choice(lower_letters)

    for _ in range(uc):
        password += random.choice(upper_letters)

    for _ in range(spec):
        password += random.choice(special_chars)

    for _ in range(numbs):
        password += random.choice(numbers)

    remaining_length = length - (lc + uc + spec + numbs)
    for _ in range(remaining_length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password
length = int(input("What length? "))
lc = int(input("How many lower case letters? "))
uc = int(input("How many upper case letters? "))
spec = int(input("How many special characters? "))
numbs = int(input("How many numbers? "))

password = generator(length, lc, uc, spec, numbs)
print("Password:", password)
