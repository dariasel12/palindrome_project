# Palindrome Generator API

## Overview
The Palindrome Generator API is a RESTful service that allows users to:
1. Generate strings (palindromes or non-palindromes) of customizable lengths.
2. Retrieve previously generated strings using unique identifiers.

This project includes Swagger documentation, database integration, and a comprehensive test suite with Allure reporting.

---

## Features
- Generate palindrome or non-palindrome strings based on user input.
- Validate input parameters, ensuring compliance with length and type requirements.
- Retrieve strings using a unique identifier.
- Detailed Swagger documentation for API exploration.
- Thorough automated testing with pytest and Allure.

---

## Installation

### Prerequisites
- Python 3.12 or higher (strict requirement)
- Virtual environment setup (recommended)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd palindrome_project
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```
   
3. **Update pip**:
    ```
   python -m pip install --upgrade pip
    ```

4. **Install the Application only**: (app only)
   ```bash
   pip install -e .
   ```

5. **Install Development and Testing Dependencies** (app + testing tools):
   ```bash
   pip install -e .[dev]
   ```

---

## Running the Application

### Manually
Start the Flask application manually:
```bash
python app.py
```

Access the API and Swagger documentation at:
```
http://127.0.0.1:5000/
```

### Using Console Script
If installed correctly, use the console command to start the app:
```bash
run-palindrome
```

---

## API Documentation

### Overview
The API is documented using Swagger. You can access the interactive documentation at:
```
http://127.0.0.1:5000/
```

Refer to the `API_SPEC.md` file for detailed API documentation, including endpoints, parameters, and error responses.

---

## Running Tests Locally

### Prerequisites
- Ensure the application is installed (see the Installation section).
- All test dependencies are included during installation.

### Run All Tests
1. Execute the tests:
   ```bash
   pytest 
   ```

2. View Allure Report:
   ```bash
   allure serve allure-results
   ```

## Running Tests Using Docker

To execute tests and generate reports in the Docker environment, follow these steps:

### 1. Build and Start Services

Before running tests, ensure that your Docker services are built and ready:

1. **Build the Services**:
   ```bash
   docker-compose build
   ```

2. **Start Allure Service** (optional if you want to pre-run Allure):
   ```bash
   docker-compose up -d allure
   ```
   - This starts the Allure report server on `http://localhost:5050`.

### 2. Run Tests

To execute the tests and generate Allure-compatible results:

1. **Run Tests Service**:
   ```bash
   docker-compose run tests
   ```
   - This runs the test suite inside the `tests` service container.
   - Test results will be saved in the `allure-results` volume.

2. **Re-run Tests if Needed**:
   You can re-run the tests anytime with the same command:
   ```bash
   docker-compose run tests
   ```

### 3. View Allure Reports

After running the tests, follow these steps to view the Allure report:

1. **Start the Allure Service**:
   If it’s not already running, start the `allure` service:
   ```bash
   docker-compose up -d allure
   ```

2. **Access Allure Report**:
   Open the following URL in your browser:
   ```
   http://localhost:5050/allure-docker-service/latest-report?project_id=default
   ```
   - Replace `default` with your custom `PROJECT_ID` if configured.

### 4. Clean Up Docker Resources

Once testing is complete, clean up the Docker resources:

1. **Stop All Running Services**:
   ```bash
   docker-compose down
   ```

2. **Remove Orphan Containers**:
   ```bash
   docker-compose down --remove-orphans
   ```

3. **Optional: Remove Docker Volumes**:
   To free up space, you can remove unused Docker volumes:
   ```bash
   docker volume prune
   ```

### 5. Troubleshooting Commands

For debugging or troubleshooting, use the following commands:

1. **Inspect Test Results Volume**:
   ```bash
   docker volume inspect allure_results
   ```

2. **Enter the Tests Container for Debugging**:
   ```bash
   docker run -it --rm palindrom_project-tests sh
   ```
   - Replace `palindrom_project-tests` with the actual tests service image name.

3. **Check Allure Logs**:
   ```bash
   docker-compose logs allure
   ```

### Key URLs

- **Allure Reports**:
  ```
  http://localhost:5050/allure-docker-service/latest-report?project_id=default
  ```

- **Allure API**:
  ```
  http://localhost:5050/allure-docker-service/projects  


## Test Coverage
The test suite includes:
- Unit tests for services and logic.
- API tests for endpoints with validation and edge cases.

---

## Development Workflow

1. **Add Features or Fix Bugs**:
   - Make changes to the `app/` directory.
2. **Run Tests**:
   - Ensure all tests pass:
     ```bash
     pytest
     ```
3. **Update Documentation**:
   - Modify `README.md`, `TEST_PLAN.md`, or `API_SPEC.md` as needed.

---

