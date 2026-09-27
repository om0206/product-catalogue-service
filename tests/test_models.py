"""Unit tests for the Product model."""
import pytest

from service.app import create_app, db
from service.models import Product
from tests.factories import ProductFactory


@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def session(app):
    return db.session


def test_create_product(session):
    product = ProductFactory(name="Phone")
    assert product.id is not None
    assert product.name == "Phone"


def test_read_product(session):
    product = ProductFactory(name="Laptop")
    found = Product.find(product.id)
    assert found.name == "Laptop"


def test_update_product(session):
    product = ProductFactory(name="Old Name")
    product.name = "New Name"
    product.update()
    assert Product.find(product.id).name == "New Name"


def test_delete_product(session):
    product = ProductFactory()
    product_id = product.id
    product.delete()
    assert Product.find(product_id) is None


def test_list_all_products(session):
    ProductFactory.create_batch(3)
    assert len(Product.all()) == 3


def test_find_by_name(session):
    ProductFactory(name="Red Phone")
    ProductFactory(name="Blue Laptop")
    assert len(Product.find_by_name("Phone")) == 1


def test_find_by_category(session):
    ProductFactory(category="Books")
    ProductFactory(category="Electronics")
    assert len(Product.find_by_category("Books")) == 1


def test_find_by_availability(session):
    ProductFactory(available=True)
    ProductFactory(available=False)
    assert len(Product.find_by_availability(True)) == 1


def test_serialize(session):
    product = ProductFactory(name="Tablet", price=499.99)
    data = product.serialize()
    assert data["name"] == "Tablet"
    assert data["price"] == 499.99


def test_deserialize(session):
    product = Product()
    product.deserialize({
        "name": "Camera",
        "description": "Digital camera",
        "price": 799.99,
        "available": True,
        "category": "Electronics",
    })
    assert product.name == "Camera"
    assert product.price == 799.99
