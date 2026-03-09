import json
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "meal_updates.json"


def get_updates():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_current_meal():
    data = get_updates()
    now = datetime.now()

    current_date = now.date()
    current_time = now.time()

    for meal in data["meal_updates"]:

        start_date = datetime.strptime(meal["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(meal["end_date"], "%Y-%m-%d").date()

        if not (start_date <= current_date <= end_date):
            continue

        start_time_str, end_time_str = meal["time"].replace(" ", "").split("-")

        start_time = datetime.strptime(start_time_str, "%H:%M").time()
        end_time = datetime.strptime(end_time_str, "%H:%M").time()

        if start_time <= current_time <= end_time:
            return meal

    return None