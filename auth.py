import json
from models import User
from storage_csv import import_csv

USERS_FILE = "users.json"


def load_users():
    # Load users from JSON, if file exists - create it if not
    try:
        with open(USERS_FILE, "r") as f:
            data = json.load(f)
        users = [User(u["username"], u["password"]) for u in data]
        return users
    except FileNotFoundError:
        print("No users found. Creating new user list.")
        return []  # no users yet


def save_users(users):
    # Save users to JSON
    data = [{"username": u.username, "password": u.password} for u in users]
    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def find_user(users, username):
    # Find a user by username - returns User object or None
    username = username.lower()
    for u in users:
        if u.username == username:
            return u
    return None


def login():
    # Main login function
    users = load_users()

    print("=== Vinyl Tracker Login ===")
    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()

    user = find_user(users, username)

    if user:
        # Existing user: verify password
        if user.password == password:
            print(f"Welcome back, {user.username.title()}!")
        else:
            print("Incorrect password. Try again.")
            return login()  # restart login
    else:
        # New user: create and save
        user = User(username, password)
        users.append(user)
        save_users(users)
        print(f"New user created: {user.username.title()}")

    # Optional: import records from CSV for this user
    choice = input("Do you want to import a CSV file? (y/n): ").strip().lower()
    if choice == "y":
        import_csv(users)  # function in storage_csv.py
        # import_csv will handle adding new users if needed

    return user