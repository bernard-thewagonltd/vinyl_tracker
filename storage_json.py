import json
import os
from models import Vinyl

# Folder to store user and collection JSON files
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)


# User Storage
USERS_FILE = os.path.join(DATA_DIR, "users.json")

def load_users():
    # Load users from JSON, if file exists - create it if not
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return data  # list of dicts
        except json.JSONDecodeError:
            return []

def save_users(users):
    # Save users to JSON
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)


# Collection Storage
def get_collection_file(username):
    """Return path to the user's vinyl collection JSON file."""
    return os.path.join(DATA_DIR, f"{username}_collection.json")


def load_collection(username):
    # Load vinyl collection from JSON, if file exists - create it if not
    filename = get_collection_file(username)
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            # Convert dicts to Vinyl objects
            return [Vinyl(**vinyl_dict) for vinyl_dict in data]
        except json.JSONDecodeError:
            return []


def save_collection(collection, username):
   # Save vinyl collection to JSON, collection an array of vinyl objects
    filename = get_collection_file(username)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([vinyl.__dict__ for vinyl in collection], f, indent=4)