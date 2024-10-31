
import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"

upper, lower, digits = True, True, True #set to true / false

all = ""

if upper:
    all += upper_case
    if lower:
        all += lower_case
        if digits:
           all += number
            

length = 16  # how long u want it to be
amount = 50  # amount of password u wanna generate

for x in range(amount):
    password = "".join(random.sample(all, length))
    print (password)


