# API Specification: Palindrome Generator API

## Overview
The Palindrome Generator API allows users to:
1. **Generate Strings**: Create palindrome or non-palindrome strings of customizable lengths.
2. **Retrieve Strings**: Access previously generated strings using unique identifiers.

The API follows RESTful principles and supports JSON-based communication.

---

## Features
- **Generate Palindromes or Non-Palindromes**:
  - Specify whether the string should be a palindrome or not.
  - Optionally set the string length (default: 6; max: 30).
- **Retrieve Generated Strings**:
  - Retrieve strings using unique IDs.

---

## Endpoints

### **1. Generate String**
- **Endpoint**: `POST /palindrome/generate-string`
- **Description**: Generates a palindrome or non-palindrome string based on the input parameters.

#### Request Fields
| Field       | Type    | Required | Default | Description                               |
|-------------|---------|----------|---------|-------------------------------------------|
| `palindrome`| Boolean | Yes      | -       | Whether to generate a palindrome.         |
| `length`    | Integer | No       | 6       | Length of the string (1 ≤ length ≤ 30).   |

#### Response
| Field       | Type    | Description                                     |
|-------------|---------|-------------------------------------------------|
| `id`        | String  | Unique identifier for the generated string.     |
| `result`    | String  | The generated string (palindrome or non-palindrome). |

#### Example Request
```json
{
    "palindrome": true,
    "length": 6
}
```

#### Example Response
```json
{
    "id": "unique-id",
    "result": "abcba"
}
```

#### Error Responses
| Status Code | Message                                | Description                                |
|-------------|----------------------------------------|--------------------------------------------|
| `400`       | `Missing or invalid 'palindrome' parameter` | When the `palindrome` field is missing or invalid. |
| `400`       | `Invalid 'length' parameter, must be a positive integer`          | When `length` is not a positive integer.   |
| `400`       | `'length' must not exceed 30 characters` | When `length` exceeds the maximum limit.   |

---

### **2. Retrieve String**
- **Endpoint**: `GET /palindrome/retrieve-string/<id>`
- **Description**: Retrieves a previously generated string using its unique identifier.

#### Path Parameters
| Field | Type   | Required | Description                                |
|-------|--------|----------|--------------------------------------------|
| `id`  | String | Yes      | Unique identifier for the string.          |

#### Response
| Field       | Type    | Description                                     |
|-------------|---------|-------------------------------------------------|
| `string`    | String  | The retrieved string (palindrome or non-palindrome). |

#### Example Request
```bash
GET /palindrome/retrieve-string/unique-id
```

#### Example Response
```json
{
    "string": "abcba"
}
```

#### Error Responses
| Status Code | Message                  | Description                            |
|-------------|--------------------------|----------------------------------------|
| `404`       | `ID not found`           | The provided ID does not exist.        |

---

## Swagger Documentation
The API includes Swagger-like documentation for easy exploration and testing of endpoints. Swagger is implemented using **Flask-RESTx**.

### How to Access Swagger UI
1. Start the application locally:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Use the interactive UI to:
   - View endpoint details.
   - Test requests and responses directly from the browser.

---

## Constraints
1. **Length**:
   - Minimum: 1
   - Maximum: 30
2. **Required Fields**:
   - `palindrome` is mandatory for the `/generate-string` endpoint.
3. **Data Validation**:
   - Invalid `length` values (non-integers or out of range) will return a `400 Bad Request`.
   - Non-existent `id` values in `/retrieve-string/<id>` will return a `404 Not Found`.

---

## Testing Notes
- **Manual Testing**:
  - Use Swagger UI or Postman to validate endpoint behavior.
- **Automated Testing**:
  - Run the test suite using `pytest`:
    ```bash
    pytest --alluredir=allure-results
    ```
  - View the Allure report for detailed test results:
    ```bash
    allure serve allure-results
    ```

---

## Dependencies
Refer to the `requirements.txt` file for a list of dependencies required to run this API.

---

