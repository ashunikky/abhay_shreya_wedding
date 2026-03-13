AI Wedding Event Assistant

An AI-powered conversational assistant designed to help wedding guests easily access event details, venue information, and meal updates during a multi-day wedding celebration.

Instead of sharing schedules and updates through multiple messages, guests can simply ask questions and receive real-time responses about the ongoing or upcoming ceremonies.

Project Overview

This project demonstrates how Generative AI and tool-based architecture can be used to build a practical assistant for real-world events such as weddings, conferences, or large gatherings.

The assistant dynamically retrieves structured event information and generates natural responses to user queries.

Example questions guests can ask:

What event is happening now?

Where is the Barat meetup?

Is breakfast available?

Where is the wedding venue?

What is the next ceremony?

The assistant responds using real-time logic based on the current date and time.

Key Features

Conversational AI Interface
Guests can interact with the assistant using natural language questions.

Real-time Event Detection
The assistant detects whether an event is currently happening, starting soon, or already completed.

Dynamic Meal Announcements
Automatically informs guests when breakfast, lunch, tea, or dinner is available.

Venue Navigation
Provides location details along with map links for easy navigation.

Fallback Ritual Information
If no major ceremony is happening, the assistant informs guests about ongoing traditional rituals such as Haldi Lepan or family celebrations.

Live Deployment
The application is deployed as an interactive web app accessible to guests.

Tech Stack

Python

LLM-based conversational AI

Prompt Engineering

Tool-based AI architecture

JSON-based structured event data

Streamlit for web interface

GitHub for version control

Built using:

Streamlit

GitHub

Project Architecture

The assistant uses a modular tool-based architecture.

User Query
↓
Agent Router
↓
Specialized Tools

Tools include:

Event Information Tool

Meal Update Tool

Venue Map Tool

Couple Information Tool

Each tool retrieves structured data from JSON files and provides context to the AI model.

Example Assistant Responses

Event Query

User:
"What is happening now?"

Assistant:
"Sangeet ceremony is currently happening at the residence. Guests are welcome to join the celebration."

Meal Query

User:
"Is breakfast available?"

Assistant:
"Breakfast is ready at the terrace of the house. Chairs and tables are arranged for guests."

Upcoming Event Query

User:
"When is the Barat?"

Assistant:
"The Barat will first gather at the nearby temple at 5:00 PM and then proceed to the meetup point at Golmuri Circle at 6:00 PM."

Real-world Usage

This assistant was built for a family wedding and used by guests from both the groom's and bride's sides.

It helped guests quickly access ceremony schedules, venue directions, and meal updates without needing to search through messages or ask organizers.

Future Improvements

Possible enhancements include:

WhatsApp integration for guest queries

Voice-based interaction

Admin dashboard for live updates

Push notifications for major events

Multi-language support

Author

Ashutosh Pandit

AI enthusiast exploring practical applications of Generative AI in real-world scenarios.

License

This project is open for learning and experimentation.