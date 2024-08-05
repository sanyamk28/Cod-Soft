import random
import string

def generate_password(length):
    # Define the character sets to use for the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine all character sets
    all_chars = lower + upper + digits + special

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")

    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            if length >= 4:
                break
            else:
                print("Password length should be at least 4.")
        except ValueError:
            print("Please enter a valid number.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {password}")

# Run the main function
if __name__ == "__main__":
    main()
