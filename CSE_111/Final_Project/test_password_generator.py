from password_generator import letter_only_password, letters_and_numbers_password, letters_and_numbers_and_symbols_password
import pytest

def test_letter_only_password():
    password = letter_only_password()
    assert len(password) == 16
    assert password.isalpha()

def test_letters_and_numbers_password():
    password = letters_and_numbers_password()
    assert len(password) == 16
    assert password.isalnum()

def test_letters_and_numbers_and_symbols_password():
    password = letters_and_numbers_and_symbols_password()
    assert len(password) == 16
    assert any(char.isdigit() for char in password)
    assert any(char.isalpha() for char in password)
    assert any(not char.isalnum() for char in password)

pytest.main(["-v", "--tb=line", "-rN", __file__])