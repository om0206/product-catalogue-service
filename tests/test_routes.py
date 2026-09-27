"""Unit tests for Product REST routes."""
import pytest

from service.app import create_app, db
from tests.factories import ProductFactory


@pytest.fixture
def client():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })
    with app.app_context():
        db.drop_all()
        db.create_all()
        with app.test_client() as test_client:
            yield test_client
        db.session.remove()
        db.drop_all()


def payload(name="Phone", category="Electronics", available=True):
    return {
        "name": name,
        "description": "Test product",
        "price": 499.99,
        "available": available,
        "category": category,
    }


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_create_product(client):
    response = client.post("/products", json=payload())
    assert response.status_code == 201
    assert response.get_json()["name"] == "Phone"


def test_read_product(client):
    product = ProductFactory()
    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200
    assert response.get_json()["id"] == product.id


def test_read_missing_product(client):
    response = client.get("/products/99999")
    assert response.status_code == 404


def test_update_product(client):
    product = ProductFactory(name="Old")
    response = client.put(
        f"/products/{product.id}",
        json=payload(name="Updated"),
    )
    assert response.status_code == 200
    assert response.get_json()["name"] == "Updated"


def test_delete_product(client):
    product = ProductFactory()
    response = client.delete(f"/products/{product.id}")
    assert response.status_code == 204


def test_list_all_products(client):
    ProductFactory.create_batch(3)
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.get_json()) == 3


def test_list_by_name(client):
    ProductFactory(name="Gaming Laptop")
    response = client.get("/products?name=Laptop")
    assert response.status_code == 200
    assert len(response.get_json()) == 1


def test_list_by_category(client):
    ProductFactory(category="Books")
    response = client.get("/products?category=Books")
    assert response.status_code == 200
    assert len(response.get_json()) == 1


def test_list_by_availability(client):
    ProductFactory(available=False)
    response = client.get("/products?available=false")
    assert response.status_code == 200
    assert len(response.get_json()) == 1
