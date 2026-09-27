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
    Then I should see "Laptop"

  Scenario: Update a product
    When I update product "1" with name "Updated Laptop"
    Then I should see "Updated Laptop"

  Scenario: Delete a product
    When I delete product "1"
    Then I should see a message "Product deleted"

  Scenario: List all products
    When I list all products
    Then I should see "Laptop"
    And I should see "Phone"

  Scenario: Search products by category
    When I search products by category "Books"
    Then I should see "Python Book"

  Scenario: Search products by availability
    When I search products by availability "true"
    Then I should see "Laptop"

  Scenario: Search products by name
    When I search products by name "Phone"
    Then I should see "Phone"
