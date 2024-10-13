import random
import string


def gen_pass(length):
    if length < 8:
        return "Password Length Must be At Least 8 Characters long!!"


    lowerCase_Char = string.ascii_lowercase
    upperCase_Char = string.ascii_uppercase
    digits = string.digits
    specialch = string.punctuation 
    
    
    password = [random.choice(lowerCase_Char), random.choice(upperCase_Char), random.choice(digits), random.choice(specialch)]
        
    allCharTogether = lowerCase_Char + upperCase_Char + digits + specialch
    
    
    password = password + random.choices(allCharTogether, k = length - len(password))
    random.shuffle(password)
    return ''.join(password)


password_length = random.randint(8,12)

password = gen_pass(password_length)

print(f" Generated Password is: {password} ")