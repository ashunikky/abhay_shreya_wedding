import json
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "events.json"


def get_events():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_live_event():

    data = get_events()
    now = datetime.now()

    for event in data["events"]:

        try:
            event_datetime = datetime.strptime(
                f"{event['date']} {event['time']}", "%d %B %Y %I:%M %p"
            )
        except:
            # skip events with complex time format
            continue

        diff = (event_datetime - now).total_seconds()

        # Event happening (within 2 hours)
        if -7200 <= diff <= 7200:
            return f"""
{event['name']} is currently happening at {event['venue']}.
Guests are welcome to join the celebration.
"""

        # Event starting soon (within 1 hour)
        if 0 < diff <= 3600:
            return f"""
{event['name']} will begin shortly at {event['venue']}.
Guests may start gathering there.
"""

    return "No ceremony is currently live."