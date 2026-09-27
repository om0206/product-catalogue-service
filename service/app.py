"""Flask application factory."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        SQLALCHEMY_DATABASE_URI="sqlite:///products.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        TESTING=False,
    )
    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    from service.routes import products_bp
    app.register_blueprint(products_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()
