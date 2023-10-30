#Password geneartion

import random
import string
def gen(len):
    low = string.ascii_lowercase
    up= string.ascii_uppercase
    dig = string.digits
    pun = string.punctuation
    letter = low+ up +dig+ pun
    var = random.sample(letter,len)
    passwrd = "".join(var)
    return(passwrd)

print("Welcome to Password generator!")
len= int(input("\nEnter the length of password to Generate: "))
password=gen(len)
print(password)