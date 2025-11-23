from storage_json import load_users, save_users

def get_all_users():
    # Load users from JSON
    return load_users()


def find_user(username):
    # Find a user by username
    username = username.lower()
    users = get_all_users()
    for user in users:
        if user["username"] == username:
            return user
    return None


def create_user(username, password):
    # Create a new user
    users = get_all_users()
    user_dict = {"username": username.lower(), "password": password}
    users.append(user_dict)
    save_users(users)
    return user_dict


def authenticate(username, password):
    # Authenticate a user
    user = find_user(username)
    if user and user["password"] == password:
        return user
    return None


def login_screen():
   # Login screen, retuns username
    print("=== Login ===")
    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()

    user = authenticate(username, password)
    if user:
        print(f"Welcome back, {username.title()}!")
        return username

    # Check if user exists
    existing_user = find_user(username)
    if existing_user:
        # User exists but wrong password
        print("Incorrect password.")
        return None

    # User doesn't exist → create new
    create_user(username, password)
    print(f"New user {username.title()} created.")
    return username