import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    # Check if password meets certain criteria
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Define password strength based on criteria
    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 6 and (has_upper or has_lower) and (has_digit or has_special):
        return "Moderate"
    else:
        return "Weak"

# Example usage
password = generate_password()
print("Generated Password:", password)
print("Password Strength:", check_password_strength(password))
