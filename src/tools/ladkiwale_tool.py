import json
from pathlib import Path

# ---------- Data Path ----------
DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "ladkiwale.json"

# ---------- Tool Function ----------
def get_ladkiwale_info():
    """Return all Ladkiwale info as loaded from JSON."""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)