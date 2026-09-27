"""REST API routes for the Product Catalogue."""
from flask import Blueprint, jsonify, request

from service.models import Product

products_bp = Blueprint("products", __name__)


@products_bp.get("/health")
def health():
    return jsonify(status="OK"), 200


@products_bp.get("/")
def index():
    return jsonify(message="Product Catalogue Service"), 200


@products_bp.post("/products")
def create_product():
    product = Product()
    try:
        product.deserialize(request.get_json() or {})
        product.create()
    except ValueError as exc:
        return jsonify(error=str(exc)), 400
    return jsonify(product.serialize()), 201


@products_bp.get("/products")
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name is not None:
        products = Product.find_by_name(name)
    elif category is not None:
        products = Product.find_by_category(category)
    elif available is not None:
        products = Product.find_by_availability(available)
    else:
        products = Product.all()

    return jsonify([product.serialize() for product in products]), 200


@products_bp.get("/products/<int:product_id>")
def read_product(product_id):
    product = Product.find(product_id)
    if product is None:
        return jsonify(error="Product not found"), 404
    return jsonify(product.serialize()), 200


@products_bp.put("/products/<int:product_id>")
def update_product(product_id):
    product = Product.find(product_id)
    if product is None:
        return jsonify(error="Product not found"), 404

    try:
        product.deserialize(request.get_json() or {})
        product.update()
    except ValueError as exc:
        return jsonify(error=str(exc)), 400

    return jsonify(product.serialize()), 200


@products_bp.delete("/products/<int:product_id>")
def delete_product(product_id):
    product = Product.find(product_id)
    if product is None:
        return jsonify(error="Product not found"), 404

    product.delete()
    return "", 204
