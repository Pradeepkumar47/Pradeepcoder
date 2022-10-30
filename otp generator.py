import random
otp=int(input("enter the length of otp:"))
o="0123456789"
p =  "".join(random.sample(o,otp ))
print(p)
