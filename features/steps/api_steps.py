"""API step definitions used by products.feature."""
from behave import given, when, then


@when('I request the product with id "{product_id}"')
def step_request_product(context, product_id):
    context.response = context.app.test_client().get(f"/products/{product_id}")


@when('I update product "{product_id}" with name "{name}"')
def step_update_product(context, product_id, name):
    context.response = context.app.test_client().put(
        f"/products/{product_id}",
        json={
            "name": name,
            "description": "Updated product",
            "price": 999.99,
            "available": True,
            "category": "Electronics",
        },
    )


@when('I delete product "{product_id}"')
def step_delete_product(context, product_id):
    context.response = context.app.test_client().delete(f"/products/{product_id}")
    context.response_text = "Product deleted" if context.response.status_code == 204 else ""


@when("I list all products")
def step_list_all(context):
    context.response = context.app.test_client().get("/products")


@when('I search products by category "{category}"')
def step_search_category(context, category):
    context.response = context.app.test_client().get(
        "/products", query_string={"category": category}
    )


@when('I search products by availability "{available}"')
def step_search_availability(context, available):
    context.response = context.app.test_client().get(
        "/products", query_string={"available": available}
    )


@when('I search products by name "{name}"')
def step_search_name(context, name):
    context.response = context.app.test_client().get(
        "/products", query_string={"name": name}
    )


@then('I should see "{text}"')
def step_response_contains(context, text):
    assert text in context.response.get_data(as_text=True)


@then('I should see a message "{message}"')
def step_response_message(context, message):
    assert message in context.response_text
