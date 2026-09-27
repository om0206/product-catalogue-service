"""BDD background data loading steps."""
from behave import given

from service.models import Product


@given("the following products")
def step_load_products(context):
    for row in context.table:
        product = Product(
            name=row["name"],
            description=row.get("description", ""),
            price=float(row["price"]),
            available=row.get("available", "true").lower() == "true",
            category=row["category"],
        )
        product.create()
