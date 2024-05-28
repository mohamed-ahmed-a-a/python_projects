print("\t\t" + "=" * 41)
print("\t\t" + "=====>^" , "Password Generator App :)" , "^<=====")
print("\t\t" + "=" * 41)

import random
import string


user_input = int(input("\nPlease Enter The Number Of Character Of Your Password : "))

special_chars1 = ['!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '-' , '_']
special_chars2 = ['!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '-' , '_']
special_chars3 = ['!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '-' , '_']
special_chars4 = ['!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '-' , '_']

def generate_password(lenght):

    password_chars = string.ascii_letters + string.digits + random.choice(special_chars4) \
    + random.choice(special_chars1) + random.choice(special_chars2) + random.choice(special_chars3)

    password = ''.join(random.choice(password_chars) for _ in range(lenght))

    return password

password = generate_password(user_input)

print(f"\nYour Generated Password : \'{password}\'")

print("\n====>" , "Thank You For Using My Application ^_^" ,"<=====")
