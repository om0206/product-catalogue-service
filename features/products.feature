Feature: Product Catalogue API

  Background:
    Given the following products
      | name          | description       | price  | available | category    |
      | Laptop        | Business laptop  | 999.99 | true      | Electronics |
      | Phone         | Smart phone      | 699.99 | true      | Electronics |
      | Python Book   | Programming book | 49.99  | true      | Books       |
      | Old Camera    | Used camera      | 199.99 | false     | Electronics |

  Scenario: Read a product
    When I request the product with id "1"
    Then the API response should contain "Laptop"

  Scenario: Update a product
    When I update product "1" with name "Updated Laptop"
    Then the API response should contain "Updated Laptop"

  Scenario: Delete a product
    When I delete product "1"
    Then I should see a message "Product deleted"

  Scenario: List all products
    When I list all products
    Then the API response should contain "Laptop"
    And the API response should contain "Phone"

  Scenario: Search products by category
    When I search products by category "Books"
    Then the API response should contain "Python Book"

  Scenario: Search products by availability
    When I search products by availability "true"
    Then the API response should contain "Laptop"

  Scenario: Search products by name
    When I search products by name "Phone"
    Then the API response should contain "Phone"
