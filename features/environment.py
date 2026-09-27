from service.app import create_app, db


def before_all(context):
    context.app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })
    context.app_context = context.app.app_context()
    context.app_context.push()
    db.create_all()


def after_all(context):
    db.session.remove()
    db.drop_all()
    context.app_context.pop()


def before_scenario(context, scenario):
    db.drop_all()
    db.create_all()
