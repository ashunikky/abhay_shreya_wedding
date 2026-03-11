import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "events.json"

IST = ZoneInfo("Asia/Kolkata")


def get_events():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_live_event():

    data = get_events()
    now = datetime.now(IST)

    closest_event = None
    closest_diff = None

    for event in data["events"]:

        try:
            if isinstance(event.get("time"), dict):
                event_time = event["time"]["start"]
            else:
                event_time = event["time"]

            event_datetime = datetime.strptime(
                f"{event['date']} {event_time}", "%d %B %Y %I:%M %p"
            ).replace(tzinfo=IST)

        except Exception:
            continue

        diff = (event_datetime - now).total_seconds()

        # event happening
        if -7200 <= diff <= 7200:
            venue = event['venue'] if isinstance(event['venue'], str) else event['venue']['place']
            return f"{event['name']} is currently happening at {venue}. Guests are welcome to join the celebration."

        # find closest upcoming event
        if diff > 0:
            if closest_diff is None or diff < closest_diff:
                closest_diff = diff
                closest_event = event

    if closest_event:
        venue = closest_event['venue'] if isinstance(closest_event['venue'], str) else closest_event['venue']['place']
        return f"The next celebration is {closest_event['name']} at {venue}. Guests are welcome to join."

    return ""