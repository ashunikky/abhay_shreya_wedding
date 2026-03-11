import json
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "meal_updates.json"

IST = ZoneInfo("Asia/Kolkata")


def get_updates():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_current_meal():

    data = get_updates()
    now = datetime.now(IST)
    current_date = now.date()

    upcoming_meal = None
    upcoming_time = None

    for meal in data["meal_updates"]:

        start_date = datetime.strptime(meal["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(meal["end_date"], "%Y-%m-%d").date()

        if not (start_date <= current_date <= end_date):
            continue

        meal_time = datetime.strptime(meal["time"], "%H:%M").time()

        meal_datetime = datetime.combine(current_date, meal_time, tzinfo=IST)

        diff = (meal_datetime - now).total_seconds()

        # 🍳 Meal preparation window (2 hours before serving)
        if 0 < diff <= 10800:
            return f"{meal['name']} is currently being prepared and will be served shortly at the terrace."

        # 🍽 Meal currently being served (2 hours window)
        if -10800 <= diff <= 10800:
            return f"{meal['message']} {meal['note']}"

        # Track upcoming meal
        if diff > 0:
            if upcoming_time is None or meal_datetime < upcoming_time:
                upcoming_time = meal_datetime
                upcoming_meal = meal

    # If nothing active, inform next meal
    if upcoming_meal:
        return f"The next meal will be {upcoming_meal['name']} which will be served later at the terrace."

    return ""