from flask import Flask

def create_app():
    app = Flask(__name__)

    # Імпорт і реєстрація блюпрінтів
    from app.users import users_bp
    from app.products import products_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)

    # Імпорт і реєстрація головних маршрутів
    from app.routes import register_routes
    register_routes(app)

    return app
