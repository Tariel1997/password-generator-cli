import random
import string

LOWERCASE_CHARS = string.ascii_lowercase
UPPERCASE_CHARS = string.ascii_uppercase
DIGITS = string.digits
PUNCTUATION_CHARS = string.punctuation


def get_user_input():
    """Obtaining data from the user to generate a password."""

    while True:
        try:
            length = int(input("Enter the desired password length (minimum 6): "))
            if length >= 6:
                break
            else:
                print("The password length must be at least 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nSelect character types (y - yes, n - no):")

    use_upper = input("Use uppercase letters (A-Z)? (y/n): ").lower() == "y"
    use_lower = input("Use lowercase letters (a-z)? (y/n): ").lower() == "y"
    use_digits = input("Use numbers (0-9)? (y/n): ").lower() == "y"
    use_punctuation = input("Use special characters (!@#$%)? (y/n): ").lower() == "y"

    if not any([use_upper, use_lower, use_digits, use_punctuation]):
        print(
            "\n**Warning:** You must select at least one character type. Lowercase letters and numbers will be used automatically."
        )
        use_lower = True
        use_digits = True

    return length, use_upper, use_lower, use_digits, use_punctuation


def generate_password(length, use_upper, use_lower, use_digits, use_punctuation):
    """Generate a password based on the parameters selected by the user."""

    all_chars = ""

    if use_lower:
        all_chars += LOWERCASE_CHARS
    if use_upper:
        all_chars += UPPERCASE_CHARS
    if use_digits:
        all_chars += DIGITS
    if use_punctuation:
        all_chars += PUNCTUATION_CHARS

    if not all_chars:
        return "Error: No character type selected."

    password = ""
    for _ in range(length):
        random_char = random.choice(all_chars)
        password += random_char

    required_chars = []
    if use_lower:
        required_chars.append(random.choice(LOWERCASE_CHARS))
    if use_upper:
        required_chars.append(random.choice(UPPERCASE_CHARS))
    if use_digits:
        required_chars.append(random.choice(DIGITS))
    if use_punctuation:
        required_chars.append(random.choice(PUNCTUATION_CHARS))

    if len(required_chars) <= length:
        temp_password_list = list(password)
        for i, char in enumerate(required_chars):
            if i < length:
                temp_password_list[i] = char

        random.shuffle(temp_password_list)
        password = "".join(temp_password_list)

    return password


def main():
    print("--- Python Password Generator (CLI) ---")

    length, use_upper, use_lower, use_digits, use_punctuation = get_user_input()

    password = generate_password(
        length, use_upper, use_lower, use_digits, use_punctuation
    )

    print("\n-------------------------------------------")
    print(f"Your generated password is: **{password}**")
    print("-------------------------------------------")


if __name__ == "__main__":
    main()
