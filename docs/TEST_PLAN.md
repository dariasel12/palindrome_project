# Test Plan: Palindrome Generator API

## Project Name
Palindrome Generator API

## Environment
- **Application**: 
  - Flask app must be running during tests. 
  - Automatically managed by the `start_flask_app` fixture.
- **Local Environment**:
  - Python 3.10+
  - Flask Framework
  - SQLite Database
- **Optional Dockerized Environment**:
  - Docker and Docker Compose for containerized execution.

---

## Features to be Tested

### 1. Generate String Endpoint (`POST /palindrome/generate-string`)
This endpoint generates a string (palindrome or non-palindrome) based on user-provided parameters.

### 2. Retrieve String Endpoint (`GET /palindrome/retrieve-string/<id>`)
This endpoint retrieves a previously generated string using its unique identifier.

---

## Test Approach
- Automated tests are written using `pytest` and utilize fixtures for efficient test setup.
- The `start_flask_app` fixture ensures the Flask app is running throughout the test session.
- For retrieval tests, the `generate_sample_string` fixture pre-generates data for consistency.

---

## Test Cases

### Feature 1: Generate String Endpoint (`POST /palindrome/generate-string`)

| Test ID  | Test Name                          | Prerequisites | Test Steps                                                                                  | Expected Result                                                                                          |
|----------|-----------------------------------|---------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| TC-001   | Generate Palindrome String         | None          | Send a valid request with `palindrome=true` and `length=5`.                                 | Response status: `200 OK`. Response body contains `id` and a palindrome string of length `5`.            |
| TC-002   | Generate Non-Palindrome String     | None          | Send a valid request with `palindrome=false` and `length=10`.                               | Response status: `200 OK`. Response body contains `id` and a non-palindrome string of length `10`.       |
| TC-003   | Generate String with Default Length | None          | Send a request without the `length` field but with `palindrome=true`.                       | Response status: `200 OK`. Response body contains a palindrome string of default length `6`.             |
| TC-004   | Invalid Length: Zero               | None          | Send a request with `length=0` and `palindrome=true`.                                       | Response status: `400 Bad Request`. Response body contains an error message: "Invalid 'length' parameter, must be a positive integer".|
| TC-005   | Invalid Length: Exceeds Max        | None          | Send a request with `length=31` and `palindrome=false`.                                     | Response status: `400 Bad Request`. Response body contains an error message: "'length' must not exceed 30 characters".|
| TC-006   | Missing Required Field: Palindrome | None          | Send a request without the required `palindrome` field.                                     | Response status: `400 Bad Request`. Response body contains an error message: "Missing or invalid 'palindrome' parameter".|
| TC-007   | Invalid Field Type for Length      | None          | Send a request with `palindrome=true` and a non-integer value for `length` (e.g., `length="abc"`). | Response status: `400 Bad Request`. Response body contains an error message: "Invalid 'length' parameter, must be a positive integer".|

---

### Feature 2: Retrieve String Endpoint (`GET /palindrome/retrieve-string/<id>`)

| Test ID  | Test Name                          | Prerequisites                                    | Test Steps                                                                                  | Expected Result                                                                                          |
|----------|-----------------------------------|------------------------------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| TC-008   | Retrieve Existing String           | A valid string pre-generated via `generate_sample_string`. | Retrieve the generated string using the `id` from the `generate_sample_string` fixture.     | Response status: `200 OK`. Response body contains the correct string matching the `id`.                 |
| TC-009   | Retrieve Non-Existent ID           | None                                            | Attempt to retrieve a string using an invalid `id` (e.g., `id="non-existent-id"`).          | Response status: `404 Not Found`. Response body contains an error message: "ID not found".              |
| TC-010   | Retrieve with Empty ID             | None                                            | Attempt to retrieve a string using an empty `id`.                                           | Response status: `404 Not Found`. Response body contains an error message: "ID not found".              |

---

## Fixtures Used

### 1. `start_flask_app`
- **Purpose**: Automatically start and stop the Flask app for testing.
- **Implementation**:
  ```python
  import pytest
  import subprocess
  import time

  @pytest.fixture(scope="session", autouse=True)
  def start_flask_app():
      flask_process = subprocess.Popen(["run-palindrome"])
      time.sleep(3)  # Wait for the app to start
      yield
      flask_process.terminate()  # Stop the app after tests
  ```
- **Scope**: Session-wide; the app starts once for all tests and terminates after the test session.

### 2. `generate_sample_string`
- **Purpose**: Pre-generate a sample string for use in retrieval tests.
- **Implementation**:
  ```python
  @pytest.fixture
  def generate_sample_string():
      response = requests.post(f"{BASE_URL}/generate-string", json={"palindrome": True, "length": 6})
      data = response.json()
      return {"id": data["id"], "result": data["result"]}
  ```
- **Scope**: Test-specific; a new string is generated for each retrieval test.

---

## Execution Flow
1. **Environment Setup**:
   - The Flask app is automatically launched using the `start_flask_app` fixture.
   - No manual app start is required.

2. **Test Priority**:
   - High Priority:
     - Validation tests for required fields and invalid inputs.
     - Retrieval of existing strings.
   - Medium Priority:
     - Default parameter handling.
     - Boundary conditions (e.g., minimum and maximum lengths).
   - Low Priority:
     - Retrieval with non-existent or empty IDs.

3. **Run Tests**:
   ```bash
   pytest
   ```

4. **Generate and View Allure Report**:
   - Run:
     ```bash
     allure serve allure-results
     ```

---

## Notes

### Tools
- **Manual Testing**: Use Postman or Swagger UI for manual validation.
- **Automated Testing**: Use `pytest` with Allure for automated testing and reporting.

---
