"""
database.py: Database setup and configuration.

This module initializes the SQLAlchemy instance and connects it to the Flask
application. It also ensures that database tables are created.

Author: Daria S
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy instance for database interactions
db: SQLAlchemy = SQLAlchemy()


def init_db(app: Flask) -> None:
    """
    Configure the Flask app with database settings and initialize the database.

    :param app: Flask application instance
    :return: None
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///palindromes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
