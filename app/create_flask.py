from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True  # Включаем режим тестирования

    @app.route('/')
    def home():
        return "Hello, World!"

    return app
