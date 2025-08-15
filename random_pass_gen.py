import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters  
    if use_numbers:
        characters += string.digits         
    if use_symbols:
        characters += string.punctuation    
    if not characters:
        return "Error: No character types selected."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- Main Program ---
print("=== Random Password Generator ===")
length = int(input("Enter password length: "))

letters = input("Include letters? (yes/no): ").lower() == "yes"
numbers = input("Include numbers? (yes/no): ").lower() == "yes"
symbols = input("Include symbols? (yes/no): ").lower() == "yes"

print("\nYour generated password is:")
print(generate_password(length, letters, numbers, symbols))
