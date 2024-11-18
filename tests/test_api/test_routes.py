"""
API Tests for Palindrome Generator API.

Covers all test cases for the `/generate-string` and `/retrieve-string/<id>` endpoints.

Author: Daria S
"""

import pytest
import requests
import allure

BASE_URL = "http://127.0.0.1:5000/palindrome"


@allure.feature("Generate String Endpoint")
@allure.story("Generate palindrome string")
@allure.tag("api", "generate", "palindrome")
@pytest.mark.api
def test_generate_palindrome():
    """
    Test case: Generate a palindrome string of length 5.
    """
    response = requests.post(f"{BASE_URL}/generate-string", json={"palindrome": True, "length": 5})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and "result" in data
    assert len(data["result"]) == 5
    assert data["result"] == data["result"][::-1], "Generated string is not a palindrome"


@allure.feature("Generate String Endpoint")
@allure.story("Generate non-palindrome string")
@allure.tag("api", "generate", "non-palindrome")
@pytest.mark.api
def test_generate_non_palindrome():
    """
    Test case: Generate a non-palindrome string of length 10.
    """
    response = requests.post(f"{BASE_URL}/generate-string", json={"palindrome": False, "length": 10})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and "result" in data
    assert len(data["result"]) == 10
    assert data["result"] != data["result"][::-1], "Generated string is unexpectedly a palindrome"


@allure.feature("Generate String Endpoint")
@allure.story("Generate string with default length")
@allure.tag("api", "generate", "default")
@pytest.mark.api
def test_generate_default_length():
    """
    Test case: Generate a palindrome string without specifying length (default length = 6).
    """
    response = requests.post(f"{BASE_URL}/generate-string", json={"palindrome": True})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and "result" in data
    assert len(data["result"]) == 6
    assert data["result"] == data["result"][::-1], "Generated string is not a palindrome"


@allure.feature("Generate String Endpoint")
@allure.story("Invalid input: Length is zero")
@allure.tag("api", "generate", "validation")
@pytest.mark.api
def test_generate_invalid_length_zero():
    """
    Test case: Attempt to generate a string with length = 0.
    """
    response = requests.post(f"{BASE_URL}/generate-string", json={"palindrome": True, "length": 0})
    assert response.status_code == 400
    data = response.json()
    assert data["error"] == "Invalid 'length' parameter, must be a positive integer"


@allure.feature("Generate String Endpoint")
@allure.story("Invalid input: Length exceeds maximum")
@allure.tag("api", "generate", "validation")
@pytest.mark.api
def test_generate_invalid_length_exceeds_max():
    """
    Test case: Attempt to generate a string with length = 31.
    """
    response = requests.post(f"{BASE_URL}/generate-string", json={"palindrome": True, "length": 31})
    assert response.status_code == 400
    data = response.json()
    assert data["error"] == "'length' must not exceed 30 characters"


@allure.feature("Generate String Endpoint")
@allure.story("Invalid input: Missing required 'palindrome' field")
@allure.tag("api", "generate", "validation")
@pytest.mark.api
def test_generate_missing_palindrome():
    """
    Test case: Attempt to generate a string without the required 'palindrome' field.
    """
    response = requests.post(f"{BASE_URL}/generate-string", json={"length": 5})
    assert response.status_code == 400
    data = response.json()
    assert data["error"] == "Missing or invalid 'palindrome' parameter"


@allure.feature("Generate String Endpoint")
@allure.story("Invalid input: Non-integer length")
@allure.tag("api", "generate", "validation")
@pytest.mark.api
def test_generate_invalid_length_type():
    """
    Test case: Attempt to generate a string with a non-integer value for length.
    """
    response = requests.post(f"{BASE_URL}/generate-string", json={"palindrome": True, "length": "abc"})
    assert response.status_code == 400
    data = response.json()
    assert data["error"] == "Invalid 'length' parameter, must be a positive integer"


@allure.feature("Retrieve String Endpoint")
@allure.story("Retrieve existing string")
@allure.tag("api", "retrieve", "existing")
@pytest.mark.api
def test_retrieve_existing_string(generate_sample_string):
    """
    Test case: Retrieve an existing string using its ID.
    """
    string_data = generate_sample_string
    response = requests.get(f"{BASE_URL}/retrieve-string/{string_data['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["string"] == string_data["result"]


@allure.feature("Retrieve String Endpoint")
@allure.story("Retrieve non-existent ID")
@allure.tag("api", "retrieve", "not-found")
@pytest.mark.api
def test_retrieve_non_existent_id():
    """
    Test case: Attempt to retrieve a string using a non-existent ID.
    """
    response = requests.get(f"{BASE_URL}/retrieve-string/non-existent-id")
    assert response.status_code == 404
    data = response.json()
    assert data["error"] == "ID not found"


@allure.feature("Retrieve String Endpoint")
@allure.story("Retrieve with empty ID")
@allure.tag("api", "retrieve", "not-found")
@pytest.mark.api
def test_retrieve_empty_id():
    """
    Test case: Attempt to retrieve a string using an empty ID.
    """
    response = requests.get(f"{BASE_URL}/retrieve-string/")
    assert response.status_code == 404
