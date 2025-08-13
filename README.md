# Automated Customer Support Assistant
Project Overview

This project implements a Customer Support Chatbot using Python, ChatterBot, and Flask.
The bot is trained to handle basic customer support queries like order tracking, damaged product complaints, and replacement requests.
Additionally, the repository includes chatbot variations for Mathematical Calculations and Unit Conversions, powered by ChatterBot’s built-in logic adapters.

Features 

Custom & Pre-trained Training Options:
Train the chatbot using a custom list of conversations (ListTrainer).

Or train it on large datasets from ChatterBot’s CorpusTrainer (e.g., English greetings, conversations, customer service data).

⭐ Customer Service Bot:

    Handles greetings and customer queries.

    Tracks orders based on user input.

    Guides customers through complaint and replacement processes.

    Returns default responses when no match is found.

⭐ Math Bot:

    Solves basic mathematical equations entered by the user.

⭐ Unit Conversion Bot:

    Converts between different units (length, weight, etc.).

⭐ NLP Integration:

    Uses spaCy for natural language processing.

⭐ Web Integration:

    Flask-based web application for an interactive chatbot experience.
    
🛠 Tech Stack

Python 3.8 (ChatterBot compatibility)

Flask – Web framework for serving the chatbot UI

ChatterBot – Chatbot engine

spaCy – NLP processing

HTML/CSS/JavaScript – For the frontend (via templates/index.html)


⚙️ Installation & Setup

1️⃣ Clone the Repository

    git clone <repo-url>
    cd <project-folder>
    
2️⃣ Install Dependencies

    pip install flask chatterbot chatterbot-corpus spacy
    python -m spacy download en_core_web_sm
    
3️⃣ Run the Application

    python index.py
    
Visit http://127.0.0.1:5000/ in your browser.

