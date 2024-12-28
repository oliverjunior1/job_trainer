def strength(password):
    # Check if the password is 8 or more characters
    if len(password) < 8:
        return "Weak Password"

    # Check if the password has at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Weak Password"

    # Check if the password has at least one digit
    if not any(char.isdigit() for char in password):
        return "Weak Password"

    # If all conditions are met, return "Strong Password"
    return "Strong Password"


print(strength(input('Enter the password: ')))
