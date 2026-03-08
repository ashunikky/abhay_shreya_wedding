import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "events.json"


def get_events():

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)