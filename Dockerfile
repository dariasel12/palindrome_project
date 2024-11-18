# Python image
FROM python:3.12-slim

# Upgrade pip
RUN python -m pip install --upgrade pip

# Set the working directory inside the container
WORKDIR /palindrom_project

# Copy project files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .[dev]

# Expose Flask's default port
EXPOSE 5000

# Default command to run the Flask app
CMD ["run-palindrome"]



