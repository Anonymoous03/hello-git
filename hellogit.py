import random 

upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower =  "qwertyuiopasdfghjklzxcvbnm"
number = "1234567890"
special = ".,/;'@#!$%^&*"

key = upper + lower + number + special
range = 8

password_list= random.sample(key,range)
password = ''.join(map(str,password_list))
print("Your new password is: " + password)