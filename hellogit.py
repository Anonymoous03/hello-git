import random 

upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower =  "qwertyuiopasdfghjklzxcvbnm"
number = "1234567890"
special = ".,/;'@#!$%^&*"

key = upper + lower + number + special
range = 8

password = random.sample(key,range)

print(password)