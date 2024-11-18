"""
app.py: Entry point for the Palindrome API.

This script initializes the Flask application, configures the database, and
sets up the API routes.

Author: Daria S
"""

from flask import Flask
from app.database import init_db
from app.routes import configure_routes


# Initialize Flask application
app: Flask = Flask(__name__)

# Initialize the database
init_db(app)

# Configure API routes
configure_routes(app)


def main():
    """Entry point for running the Flask app."""
    app.run(debug=True)


if __name__ == "__main__":
    """
    Run the Flask application.

    The application will start a development server, handle incoming requests,
    and provide detailed error messages during development.
    """
    main()
