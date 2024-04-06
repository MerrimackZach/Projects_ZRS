import random 

print("Your Password: ")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[];':,./<>?"

password = ''
for i in range(16):
    password += random.choice(chars)
    
print(password)

