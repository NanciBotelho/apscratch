from flask import Flask


def create_app():
    # Cria e configura a aplicação
    app = Flask(__name__)

    from .invenra_api import invenra_api_bp
    app.register_blueprint(invenra_api_bp)

    return app