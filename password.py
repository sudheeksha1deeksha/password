# -*- coding: utf-8 -*-
"""Password.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N6GBYfL8dpyqkJPdkXHb-E9HlreKpWta
"""

import re

# Function to check the strength of a password
def password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Score based on how many criteria the password meets
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Return a strength message based on the score
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

# Main function to take user input and check password strength
def main():
    password = input("Enter your password to check its strength: ")
    strength = password_strength(password)
    print(f"The strength of your password is: {strength}")

# Call the main function
if __name__ == "__main__":
    main()