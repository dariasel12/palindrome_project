"""
routes.py: API endpoints for the Palindrome API with integrated Swagger documentation.

This module defines the routes for generating and retrieving palindrome or
non-palindrome strings with descriptive endpoint names, including Swagger
support via Flask-RESTx.

Author: Daria S
"""

import uuid
from flask import Flask, request
from flask_restx import Api, Resource, fields
from typing import Dict, Any, Tuple
from app.models import Palindrome
from app.database import db
from app.services import generate_string


def configure_routes(app: Flask) -> None:
    """
    Configure API routes for the Flask application.

    :param app: Flask application instance
    :return: None
    """
    # Initialize Flask-RESTx API
    api = Api(app, title="Palindrome Generator API", description="API for generating and retrieving strings.")

    # Define request model for generating strings
    generate_request_model = api.model('GenerateStringRequest', {
        'palindrome': fields.Boolean(required=True, description='Indicates whether to generate a palindrome.'),
        'length': fields.Integer(required=False, default=6, description='Length of the string (default: 6, max: 30).')
    })

    # Define response model for generated strings
    generate_response_model = api.model('GenerateStringResponse', {
        'id': fields.String(description='Unique identifier for the generated string.'),
        'result': fields.String(description='The generated string (palindrome or non-palindrome).')
    })

    # API namespace
    palindrome_ns = api.namespace('palindrome', description='Operations related to palindrome generation and retrieval')

    @palindrome_ns.route('/generate-string')
    class GenerateString(Resource):
        @api.expect(generate_request_model)
        @api.response(200, 'Success', generate_response_model)
        @api.response(400, 'Bad Request')
        def post(self) -> Tuple[Dict[str, Any], int]:
            """
            Generate a palindrome or non-palindrome string.

            :return: JSON response with the unique ID and generated string, and an HTTP status code.
            """
            data: Dict[str, Any] = request.get_json()

            # Validate 'palindrome' parameter
            if "palindrome" not in data or not isinstance(data["palindrome"], bool):
                return {"error": "Missing or invalid 'palindrome' parameter"}, 400

            # Validate 'length' parameter
            length: int = data.get("length", 6)
            if not isinstance(length, int) or length <= 0:
                return {"error": "Invalid 'length' parameter, must be a positive integer"}, 400
            if length > 30:
                return {"error": "'length' must not exceed 30 characters"}, 400

            # Generate and store the result
            palindrome: bool = data["palindrome"]
            result: str = generate_string(palindrome, length)
            new_entry: Palindrome = Palindrome(id=str(uuid.uuid4()), result=result)
            db.session.add(new_entry)
            db.session.commit()

            return {"id": new_entry.id, "result": result}, 200

    @palindrome_ns.route('/retrieve-string/<string:entry_id>')
    class RetrieveString(Resource):
        @api.response(200, 'Success', fields.String(description='The retrieved string (palindrome or non-palindrome).'))
        @api.response(404, 'Not Found')
        def get(self, entry_id: str) -> Tuple[Dict[str, Any], int]:
            """
            Retrieve a generated string by its unique ID.

            :param entry_id: Unique identifier for the string.
            :return: JSON response with the string or an error message, and an HTTP status code.
            """
            entry: Palindrome = Palindrome.query.get(entry_id)
            if not entry:
                return {"error": "ID not found"}, 404

            return {"string": entry.result}, 200

    # Add namespace to API
    api.add_namespace(palindrome_ns)
