from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    import portfolio

    app.register_blueprint(portfolio.bp)

    return app