import random
import string
import hashlib
from itertools import product

# Generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Check password strength
def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 6 and (has_upper or has_lower) and (has_digit or has_special):
        return "Moderate"
    else:
        return "Weak"

# Hash a password using the specified algorithm
def hash_password(password, algorithm='sha256'):
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    else:
        return hashlib.sha256(password.encode()).hexdigest()

# Crack the password using a wordlist
def password_crack(wordlist, hashed_password, algorithm='sha256'):
    for word in wordlist:
        if hash_password(word, algorithm) == hashed_password:
            return word
    return None

# Brute force password cracking
def brute_force_crack(hashed_password, algorithm='sha256', max_length=5):
    characters = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for guess in product(characters, repeat=length):
            guess = ''.join(guess)
            if hash_password(guess, algorithm) == hashed_password:
                return guess
    return None

# Generate a strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if check_password_strength(password) == "Strong":
            return password

# Main function to demonstrate the tool's functionality
def main():
    # Generate password
    password = generate_password()
    print("Generated Password:", password)
    print("Password Strength:", check_password_strength(password))

    # Hash the password
    hashed_password = hash_password(password, 'sha256')
    print("Hashed Password (SHA-256):", hashed_password)

    # Wordlist for cracking
    wordlist = ['password', '123456', 'admin', 'qwerty', password]

    # Attempt to crack the password using wordlist
    cracked_password = password_crack(wordlist, hashed_password)
    print("Cracked Password (Wordlist):", cracked_password if cracked_password else "Not Found")

    # Attempt brute force cracking
    brute_forced_password = brute_force_crack(hashed_password)
    print("Cracked Password (Brute Force):", brute_forced_password if brute_forced_password else "Not Found")

if __name__ == "__main__":
    main()
