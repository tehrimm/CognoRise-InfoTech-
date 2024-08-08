import random
import string


def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation


    password = ''.join(random.choice(characters) for i in range(length))

    return password


def password_generator():
    print("Password Generator")

    while True:

        length_input = input("Enter the desired password length (or 0 to exit): ")

        try:
            length = int(length_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if length == 0:
            print("Exiting the password generator. Goodbye!")
            break
        elif length < 6:
            print("Password length should be at least 6 characters for security.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print(f"Generated Password: {password}")


# Run the password generator function
password_generator()
