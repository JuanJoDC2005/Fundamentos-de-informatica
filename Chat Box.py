# Simple Chatbot

def get_user_input(prompt):

    while True:
        try:
            # Asking the user input
            response = input(prompt)
            # When input is empty, raise an exception
            if not response.strip():
                raise ValueError("Input cannot be empty. Please try again.")
            return response
        except ValueError as ve:
            print(ve)  # Print the error message


def main():
    print("Welcome to the Chatbot! Let's get to know you.")

    # Get the user's name
    name = get_user_input("What is your name? ")

    # Get the user's date of birth
    dob = get_user_input("What is your date of birth? (Format: YYYY-MM-DD) ")

    # Get the user's hobbies
    hobbies = get_user_input(
        "What are your hobbies? (Please list them separated by commas) ")

    # Display the gathered information
    print("\nThank you for sharing!")
    print(f"Name: {name}")
    print(f"Date of Birth: {dob}")
    print(f"Hobbies: {hobbies}")


# Entry point of the program
if __name__ == "__main__":
    main()
