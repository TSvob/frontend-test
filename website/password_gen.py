import string
import random


chars = list(string.ascii_letters + string.digits + "!@#$%&")
password_list = []

def new_password_generator():
    length = 15
    for i in range(length):
        password_list.append(random.choice(chars))
    random.shuffle(password_list)
    new_password= "".join(password_list)
    return new_password

