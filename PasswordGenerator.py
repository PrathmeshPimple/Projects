import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            # Prompt user for password length
            length = int(input("Enter the desired length of the password: "))
            
            # Generate and display the password
            password = generate_password(length)
            print("Generated Password:", password)
            
            # Ask the user if they want to generate another password
            another_password = input("Do you want to generate another password? (yes/no): ").lower()
            if another_password != "yes":
                break  # Exit the loop if the user enters anything other than "yes"
        except ValueError:
            print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()

