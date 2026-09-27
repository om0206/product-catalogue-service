# cURL Examples

Start the service with:

    flask --app service.app run

Create a product:

    curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d "{\"name\":\"Laptop\",\"description\":\"Business laptop\",\"price\":999.99,\"available\":true,\"category\":\"Electronics\"}"

List all products:

    curl http://127.0.0.1:5000/products

Read product 1:

    curl http://127.0.0.1:5000/products/1

Update product 1:

    curl -X PUT http://127.0.0.1:5000/products/1 -H "Content-Type: application/json" -d "{\"name\":\"Updated Laptop\",\"description\":\"Updated product\",\"price\":1099.99,\"available\":true,\"category\":\"Electronics\"}"

Delete product 1:

    curl -X DELETE http://127.0.0.1:5000/products/1

Search by name:

    curl "http://127.0.0.1:5000/products?name=Laptop"

Search by category:

    curl "http://127.0.0.1:5000/products?category=Electronics"

Search by availability:

    curl "http://127.0.0.1:5000/products?available=true"
