import random
import string

def generate_password(len):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if len < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(len))
    return password

def main():
    print("Password Generator")
    len = int(input("Enter the desired length of the password (at least 8 characters): "))
    password = generate_password(len)
    if password:
        print("Generated Password: ", password)

if __name__ == "__main__":
    main()