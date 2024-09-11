import hashlib

# Password ko hash karne ka function (MD5, SHA1, SHA256 ke liye)
def hash_password(password, algorithm='sha256'):
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    else:
        return hashlib.sha256(password.encode()).hexdigest()

# Wordlist-based password cracking function
def crack_password(hash_to_crack, algorithm='sha256', wordlist_file='wordlist.txt'):
    try:
        with open(wordlist_file, 'r') as file:
            for word in file:
                word = word.strip()  # Remove extra spaces or newline
                hashed_word = hash_password(word, algorithm)
                
                if hashed_word == hash_to_crack:
                    print(f"[+] Password found: {word}")
                    return word
        print("[-] Password not found in wordlist.")
    except FileNotFoundError:
        print("[-] Wordlist file not found. Please provide a valid wordlist.")
    return None

# Main function
def main():
    # User input ke liye hashed password aur algorithm ko input liya jaa raha hai
    hash_to_crack = input("Enter the hashed password to crack: ")
    algorithm = input("Enter the hashing algorithm (md5, sha1, sha256): ").lower()
    wordlist_file = input("Enter the wordlist file path (default: wordlist.txt): ") or 'wordlist.txt'
    
    print(f"\n[+] Trying to crack the {algorithm.upper()} hash: {hash_to_crack}")
    
    # Crack password
    cracked_password = crack_password(hash_to_crack, algorithm, wordlist_file)
    
    if cracked_password:
        print(f"\n[+] Successfully cracked: {cracked_password}")
    else:
        print("\n[-] Could not crack the password.")

if __name__ == "__main__":
    main()
