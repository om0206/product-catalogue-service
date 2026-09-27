"""Common helpers for REST routes."""
from flask import jsonify


def error_response(message, status=400):
    return jsonify(error=message), status


def json_list(products):
    return jsonify([product.serialize() for product in products])
