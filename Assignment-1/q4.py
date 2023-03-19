import random
import string


def generate(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=length))
    return password


length = int(input("Enter password length: "))
no_of_password = int(input("Enter number of passwords to generate: "))
passwords = [generate(length) for i in range(no_of_password)]
for password in passwords:
    print(password)