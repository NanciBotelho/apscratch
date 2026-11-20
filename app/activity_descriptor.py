import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"


def _load_json(filename):
    # Lê um ficheiro JSON da pasta data
    with open(DATA_DIR / filename, encoding="utf-8") as file:
        return json.load(file)


def get_config_params():
    # Parâmetros de configuração (json_params_url)
    return _load_json("APScratch_params.json")


def get_analytics_contract():
    # Lista de analytics disponibilizados (analytics_list_url)
    return _load_json("APScratch_analytics.json")