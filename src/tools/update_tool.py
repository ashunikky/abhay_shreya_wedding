import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "updates.json"


def get_updates():

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)