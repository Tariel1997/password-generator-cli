# Python Password Generator (CLI)

A simple, secure command-line tool for generating random passwords based on user-defined criteria. This script ensures that the generated password meets the selected complexity requirements.

## Features

* **Customizable Length:** Choose any password length (minimum 6 characters).
* **Character Set Selection:** Include or exclude:
    * Uppercase letters (A-Z)
    * Lowercase letters (a-z)
    * Numbers (0-9)
    * Special characters (e.g., `!@#$%&`)
* **Guaranteed Complexity:** The generator ensures that **at least one** character from *each* selected character type is included in the final password.
* **Input Validation:** Provides feedback for invalid inputs (e.g., non-numeric length, length less than 6).
* **Safety Fallback:** If no character types are selected, the script defaults to using lowercase letters and numbers to avoid errors.

## Requirements

* Python 3.x
* Core development and test dependencies are installed via `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

* No external libraries are required to run the main script; tests use `pytest` (already included in `requirements.txt`).

## How to Use

1.  Ensure you have Python 3 installed.
2.  (Recommended) Install dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

3.  Save the main script as `password_generator.py`.
4.  Run the script from your terminal:

    ```bash
    python password_generator.py
    ```

5.  Follow the on-screen prompts to configure your password:

    ```
    --- Python Password Generator (CLI) ---
    Enter the desired password length (minimum 6): 12

    Select character types (y - yes, n - no):
    Use uppercase letters (A-Z)? (y/n): y
    Use lowercase letters (a-z)? (y/n): y
    Use numbers (0-9)? (y/n): y
    Use special characters (!@#$%)? (y/n): n

    -------------------------------------------
    Your generated password is: **g7P4kL9qV2bE**
    -------------------------------------------
    ```

## Running Tests

This project includes a test suite using `pytest` to verify the generator's functionality.

1.  Install dependencies (includes `pytest`):

    ```bash
    pip install -r requirements.txt
    ```

2.  Save the test code as `test_password_generator.py` in the same directory as `password_generator.py`.

3.  Run the tests from your terminal:

    ```bash
    pytest
    ```

    You should see output indicating that the tests have passed.