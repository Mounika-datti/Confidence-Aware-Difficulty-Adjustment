# ==========================================
# DATABASE LAYER
# ==========================================

from collections import deque

# In-memory database
# Replace with PostgreSQL in production

database = {}

def initialize_user(user_id):

    if user_id not in database:

        database[user_id] = {

            "difficulty": "medium",

            "history": deque(maxlen=5),

            "increase_streak": 0,

            "decrease_streak": 0
        }

def get_user(user_id):

    return database.get(user_id)

def update_user(user_id, data):

    database[user_id] = data