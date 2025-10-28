from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  

    from app.users import users_bp
    from app.products import products_bp
    from app.auth import auth_bp 

    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(auth_bp)

    from app.routes import register_routes
    register_routes(app)

    return app
