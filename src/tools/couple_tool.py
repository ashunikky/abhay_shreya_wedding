import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "couple.json"


def get_couple_info():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)