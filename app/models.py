"""
models.py: Database models.

This module defines the database model used in the Palindrome API.

Author: Daria S
"""

from app.database import db


class Palindrome(db.Model):
    """
    Represents a palindrome or non-palindrome entry in the database.

    Attributes:
        id (str): Unique identifier (UUID) for the entry.
        result (str): The generated palindrome or non-palindrome string.
    """
    id: str = db.Column(db.String, primary_key=True)  # Unique identifier
    result: str = db.Column(db.String, nullable=False)  # Generated string
