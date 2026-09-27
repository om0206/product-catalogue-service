"""Product database model and persistence/search operations."""
from service.app import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    price = db.Column(db.Float, nullable=False, default=0.0)
    available = db.Column(db.Boolean, nullable=False, default=True)
    category = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "available": self.available,
            "category": self.category,
        }

    def deserialize(self, data):
        try:
            self.name = data["name"]
            self.description = data.get("description")
            self.price = float(data["price"])
            self.available = self._to_bool(data.get("available", True))
            self.category = data["category"]
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError("Invalid product data") from exc
        return self

    @staticmethod
    def _to_bool(value):
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ("true", "1", "yes")
        return bool(value)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find(cls, product_id):
        return cls.query.get(product_id)

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter(cls.name.ilike(f"%{name}%")).all()

    @classmethod
    def find_by_category(cls, category):
        return cls.query.filter(cls.category.ilike(category)).all()

    @classmethod
    def find_by_availability(cls, available):
        value = cls._to_bool(available)
        return cls.query.filter_by(available=value).all()
