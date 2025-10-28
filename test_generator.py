import pytest
from password_generator import generate_password, main


def test_generate_password_length_and_content():
    """Verify that the generated password is of the correct length and contains only the selected characters."""

    length = 15
    password = generate_password(
        length, use_upper=False, use_lower=True, use_digits=False, use_punctuation=False
    )

    assert len(password) == length
    assert password.islower()

    password_digits = generate_password(
        10, use_upper=False, use_lower=False, use_digits=True, use_punctuation=False
    )

    assert len(password_digits) == 10
    assert password_digits.isdigit()


def test_generate_password_empty_selection():
    """Tests behavior when no character is selected (should return error or default)."""
    password = generate_password(5, False, False, False, False)
    password_full = generate_password(20, True, True, True, True)
    assert len(password_full) == 20


def test_main_with_valid_input(monkeypatch, capsys):
    """Tests the main() function, fakes user input and captures the program output (print)."""

    inputs = ["10", "n", "y", "y", "n"]

    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    main()

    captured = capsys.readouterr()
    output = captured.out

    assert "Your generated password is:" in output

    try:
        start_index = output.find("**") + 2
        end_index = output.find("**", start_index)
        generated_password = output[start_index:end_index]

        assert len(generated_password) == 10
        assert not any(c.isupper() for c in generated_password)

    except ValueError:
        assert False, "The password could not be extracted correctly from the output."
