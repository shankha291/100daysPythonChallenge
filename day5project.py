#password generator
import string
import random
letter= list(string.ascii_lowercase+string.ascii_uppercase)


digit=list(string.digits)
special_char=['@','$','&','_','*','!']
user_letter=int(input("How many letters do you want in the password::"))
password=""
for i in range(1,user_letter+1):
    password+=random.choice(letter)
user_digits=int(input("How many digits do you want in the password:"))
for i in range(1,user_digits+1):
    password+=random.choice(digit)
user_special=int(input("How many special characters do you want in the password:"))
for i in range(1,user_special+1):
    password+=random.choice(special_char)
print("Passsword in the ordered way:",password)
total_range=user_digits+user_letter+user_special
final_list=[]
for i in password:
    final_list.append(i)
random.shuffle(final_list)#shuffle() function
final_password_string=""
for i in final_list:
    final_password_string+=i
print("Password in the radom order:",final_password_string)