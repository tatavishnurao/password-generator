import string
import random

def generate_password(length, chars):
    characters = ''
    if 'letters' in chars:
        characters += string.ascii_letters
    if 'numbers' in chars:
        characters += string.digits
    if 'symbols' in chars:
        characters += string.punctuation
    if 'letters' and 'numbers' in chars:
        characters += string.ascii_letters + string.digits
    if 'letters' and 'symbols' in chars:
        characters += string.ascii_letters + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

chars = input("Enter the types of characters to use in the password (letters, numbers, symbols or letters and numbers and letters and symbols ): ").lower()
length = int(input("Enter the length of the password: "))
password = generate_password(length, chars)
print("Your password is: " + password)