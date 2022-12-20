import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!£$%^&*()."

string = lower + upper + numbers + symbols
length = 10
password = "".join(random.sample(string,length))

print("Your new password is:"+ password)
