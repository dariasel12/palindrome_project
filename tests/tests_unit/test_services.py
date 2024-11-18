"""
Unit tests for services.py.

Covers the `generate_string` function, including standard, edge, and border cases.
Tests include Allure features, stories, tags, and pytest marks.

Author: Daria S
"""

import pytest
import allure
from app.services import generate_string


@allure.feature("Palindrome Generation")
@allure.story("Generate valid palindrome")
@allure.tag("unit", "palindrome")
@pytest.mark.unit
def test_generate_palindrome() -> None:
    """
    Test case: Generate a palindrome string of length 5.
    Expected: The result is a valid palindrome.
    """
    result = generate_string(palindrome=True, length=5)
    assert result == result[::-1], "Generated string is not a palindrome"
    assert len(result) == 5, "Palindrome length mismatch"


@allure.feature("Palindrome Generation")
@allure.story("Generate valid non-palindrome")
@allure.tag("unit", "non-palindrome")
@pytest.mark.unit
def test_generate_non_palindrome() -> None:
    """
    Test case: Generate a non-palindrome string of length 5.
    Expected: The result is not a palindrome.
    """
    result = generate_string(palindrome=False, length=5)
    assert result != result[::-1], "Generated string is unexpectedly a palindrome"
    assert len(result) == 5, "Non-palindrome length mismatch"


@allure.feature("Input Validation")
@allure.story("Check maximum allowed length")
@allure.tag("unit", "validation", "length")
@pytest.mark.unit
def test_maximum_length() -> None:
    """
    Test case: Generate a palindrome string with the maximum allowed length.
    Expected: The result is a valid palindrome of length 30.
    """
    result = generate_string(palindrome=True, length=30)
    assert result == result[::-1], "Generated string is not a palindrome"
    assert len(result) == 30, "Palindrome length mismatch"


@allure.feature("Input Validation")
@allure.story("Check minimum allowed length")
@allure.tag("unit", "validation", "length")
@pytest.mark.unit
def test_minimum_length() -> None:
    """
    Test case: Generate a palindrome string with the minimum allowed length.
    Expected: The result is a valid palindrome of length 1.
    """
    result = generate_string(palindrome=True, length=1)
    assert result == result[::-1], "Generated string is not a palindrome"
    assert len(result) == 1, "Palindrome length mismatch"


@allure.feature("Input Validation")
@allure.story("Handle invalid length input")
@allure.tag("unit", "validation")
@pytest.mark.unit
def test_invalid_length() -> None:
    """
    Test case: Handle invalid input length for palindrome generation.
    Expected: ValueError is raised for invalid length.
    """
    with pytest.raises(ValueError):
        generate_string(palindrome=True, length=0)
    with pytest.raises(ValueError):
        generate_string(palindrome=True, length=31)


@allure.feature("Default Parameters")
@allure.story("Handle default length parameter")
@allure.tag("unit", "default", "length")
@pytest.mark.unit
def test_default_length_with_required_palindrome() -> None:
    """
    Test case: Generate a palindrome string without specifying the length.
    Expected: Default length of 6 is used.
    """
    result = generate_string(palindrome=True)  # Default length = 6
    assert result == result[::-1], "Generated string is not a palindrome"
    assert len(result) == 6, "Default length mismatch"


@allure.feature("Input Validation")
@allure.story("Handle missing required palindrome parameter")
@allure.tag("unit", "validation", "missing-parameter")
@pytest.mark.unit
def test_missing_palindrome_parameter() -> None:
    """
    Test case: Handle missing `palindrome` parameter.
    Expected: TypeError is raised due to missing required parameter.
    """
    with pytest.raises(TypeError):
        generate_string()  # Missing required `palindrome` argument


