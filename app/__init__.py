from flask import Flask

app = Flask(__name__)

# Імпорт Blueprint'а
from app.users import users_bp

# Реєстрація Blueprint
app.register_blueprint(users_bp)

# Імпорт головних маршрутів
from app import routes
