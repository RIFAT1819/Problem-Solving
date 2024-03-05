import re

def count_passwords(string):
    passwords = 0
    lowercase_found = False
    uppercase_found = False
    digit_found = False
    
    for char in string:
        if char.islower():
            lowercase_found = True
        elif char.isupper():
            uppercase_found = True
        elif char.isdigit():
            digit_found = True
        
        if lowercase_found and uppercase_found and digit_found:
            passwords += 1
            lowercase_found = uppercase_found = digit_found = False
    
    return passwords

# Reading input till EOF
while True:
    try:
        string = input()
        print(count_passwords(string))
    except EOFError:
        break
