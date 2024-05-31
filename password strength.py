import re

def assess_password_strength(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[\W_]', password))

    # Feedback messages
    feedback = []
    if length_criteria:
        feedback.append("✔ Good length (8 or more characters)")
    else:
        feedback.append("❌ Password should be at least 8 characters long")

    if uppercase_criteria:
        feedback.append("✔ Contains uppercase letter(s)")
    else:
        feedback.append("❌ Add uppercase letter(s)")

    if lowercase_criteria:
        feedback.append("✔ Contains lowercase letter(s)")
    else:
        feedback.append("❌ Add lowercase letter(s)")

    if number_criteria:
        feedback.append("✔ Contains number(s)")
    else:
        feedback.append("❌ Add number(s)")

    if special_criteria:
        feedback.append("✔ Contains special character(s)")
    else:
        feedback.append("❌ Add special character(s)")

    # Assessing overall strength
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Display results
    print("Password Strength: " + strength)
    print("\nFeedback:")
    for msg in feedback:
        print(msg)

# Example usage:
password = input("Enter your password: ")
assess_password_strength(password)
