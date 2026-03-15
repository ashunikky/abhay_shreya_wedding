import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from tools.couple_tool import get_couple_info
from tools.wedding_tool import get_events, get_live_event
from tools.maps_tool import get_locations
from tools.meal_update_tool import get_current_meal
from tools.ladkiwale_tool import get_ladkiwale_info

load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini")


prompt = ChatPromptTemplate.from_template("""
You are a professional wedding assistant for Abhay & Shreya's wedding.

Answer the guest question using ONLY the information provided.

Guest Question:
{question}

Couple Information:
{couple}

Events:
{events}
                                          
Live Ceremony Status:
{live_event}

Locations:
{locations}

current_meals_information:
{meals}
                                          
Ladkiwale:
{ladkiwale}

Important Rules:

1. Never invent information that is not provided, ask to contact Mr. Ashutosh on mobile number +91 9122972521. 
2. If the information is unavailable, respond playfully without making things up.
3. You a professional wedding assistant, try to answer in a respectful manner.
4. in doubtful question, alsways ask for clarification.
5. While answer in hindli/hinglish, change english words to hindi/hinglish e.g 'residence' to 'nivaas sthaan'. 
6. If ask about location, give the location map.
7. Always respond in the same language and style used by the guest.
8. Never show raw JSON or technical data and answer in natural human language.
9. as per the time and date, inform about the meals without telling the time and dates.
10. If a ceremony is live or starting soon, inform the guest and invite them to join.
11. If event is not live or started, inform the starting time and date for that event and ask to join.
12. If a guest asks about an event whose date or time has already passed, politely inform them that the event has already been celebrated joyfully. Then guide them to the next upcoming event, if available.
13. If there is no current event in progress and no upcoming events scheduled, politely respond that the wedding ceremony has already been happily celebrated and all planned events have been completed.


Tone:
Respectfully, festive, conversational.
""")

# ---------- Ladkiwale JSON to Text ----------
def ladkiwale_to_text(ladkiwale):
    hotel = ladkiwale.get("hotel", {})
    transport = ladkiwale.get("transport", {})
    transfer = ladkiwale.get("wedding_transfer", {})

    text = "🎉 Ladkiwale Information:\n\n"

    # ---------- Hotel Info ----------
    text += f"🏨 Hotel: {hotel.get('name', 'N/A')}, {hotel.get('area', '')}, {hotel.get('city', '')}\n"
    text += f"🕚 Check-in: {hotel.get('check_in', 'N/A')}, Check-out: {hotel.get('check_out', 'N/A')}\n"
    text += f"🛏 Total Rooms: {hotel.get('rooms', 'N/A')}\n"
    text += f"📍 Hotel Map: {hotel.get('hotel-stay_map', 'Not available')}\n"
    text += f"🗺 Route to Hotel: {hotel.get('route_to_stay', 'Not available')}\n"
    text += f"🍽 Meals: Welcome Snacks: {'Yes' if hotel.get('welcome_snacks') else 'No'}, "
    text += f"Veg Lunch Buffet: {'Yes' if hotel.get('veg_lunch_buffet') else 'No'}, "
    text += f"Morning Breakfast: {hotel.get('morning_breakfast', 'N/A')}\n\n"

    # ---------- Room Details ----------
    rooms = hotel.get("rooms_detail", [])
    if rooms:
        text += "🛌 Room Details:\n"
        for room in rooms:
            notes = f" ({room['notes']})" if room.get('notes') else ""
            text += f"- Room {room.get('room_no', 'N/A')} - PAX: {room.get('pax', 'N/A')}{notes}\n"
        text += "\n"

    # ---------- Transport Info ----------
    cars = transport.get("cars", [])
    if cars:
        car_info = ", ".join([f"{car.get('type', '')} ({car.get('purpose', '')})" for car in cars])
    else:
        car_info = "N/A"
    text += f"🚗 Transport: {car_info}\n\n"

    # ---------- Wedding Transfer Info ----------
    text += f"🎊 Wedding Transfer:\n"
    text += f"- Venue: {transfer.get('venue', 'N/A')}\n"
    text += f"- Departure Time: {transfer.get('departure_time', 'N/A')}\n"
    text += f"- Route from Hotel to Wedding: {transfer.get('route_from_stay_to_wedding-location', 'Not available')}\n"
    text += f"- Wedding Location Map: {transfer.get('wedding_location', 'Not available')}\n"

    return text


# ---------- Route Question ----------
def route_question(state):
    question = state["question"]

    events = get_events()
    live_event = get_live_event()
    locations = get_locations()
    meals = get_current_meal()
    couple = get_couple_info()
    ladkiwale = ladkiwale_to_text(get_ladkiwale_info())

    chain = prompt | llm

    response = chain.invoke({
        "question": question,
        "events": events,
        "live_event": live_event,
        "locations": locations,
        "meals": meals,
        "couple": couple,
        "ladkiwale": ladkiwale
    })

    return {"answer": response.content}

meal_data = get_current_meal()

if meal_data:
    meals = f"""
{meal_data}
"""
else:
    meals = "Meals are arranged at the terrace of the house with chairs and tables for Ladkewale."

