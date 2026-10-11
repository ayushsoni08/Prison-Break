import json
import random

def load_quotes(filename = "quotes.json"):
    #loads quotes from the json file with error handling
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"\n⚠️ Warning: '{filename}' not found. Loading fallback quotes")
        return [
            {"text": "Imagination is more important than knowledge", "author": "Albert Einstein"},
            {"text": "The only way to do great work is to love what you do", "author": "Steve Jobs"}
        ]
    except json.JSONDecodeError:
        print(f"\n⚠️ Warning: '{filename}' has invalid JSON formatting")
        return[]

def get_random_quote(quotes):
    #Select and return a random quote dictionary
    return random.choice(quotes) if quotes else None

def get_quotes_by_author(quotes, author_query):
    #Filter quotes by Author name (case-insensitive partial match)
    matches = [
        q for q in quotes
        if  author_query.lower() in q["author"].lower()
    ]

    return matches