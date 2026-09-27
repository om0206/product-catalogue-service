"""Factory Boy factory for Product test data."""
import factory
from factory.fuzzy import FuzzyFloat

from service.models import Product


class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: f"Product {n}")
    description = factory.Faker("sentence")
    price = FuzzyFloat(1.0, 1000.0, precision=2)
    available = True
    category = "Electronics"
