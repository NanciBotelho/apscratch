from flask import Blueprint

# Porta única de entrada para os pedidos da Inven!RA
invenra_api_bp = Blueprint("invenra_api", __name__)

from . import routes