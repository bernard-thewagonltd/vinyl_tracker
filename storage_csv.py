import csv
from models import User, Vinyl
from storage_json import save_collection
from auth import save_users, find_user

CSV_FIELDS = [
    "username", "password", "artist", "album", "year",
    "genre", "barcode", "trackcount", "dateadded"
]


def import_csv(users, collection=None, filename=None):
    # Import CSV file and return updated users and collection, collection is optional, filename is none as this needs to be given by user.
    # Filename is expecected to be my_records.csv, place in the project root directory.
    if collection is None:
        collection = []

    if filename is None:
        filename = input("Enter CSV filename to import: ").strip()

    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                username = row["username"].lower()
                password = row["password"]
                user = find_user(users, username)
                if not user:
                    # Create new user dynamically.
                    user = User(username, password)
                    users.append(user)
                    save_users(users)
                    print(f"New user created from CSV: {username.title()}")

                # Create Vinyl object.
                vinyl = Vinyl(
                    artist=row["artist"],
                    album=row["album"],
                    year=row["year"],
                    genre=row["genre"],
                    barcode=row["barcode"],
                    trackcount=int(row["trackcount"]),
                    dateadded=row["dateadded"],
                    username=username
                )
                collection.append(vinyl)

        print(f"Imported {len(collection)} vinyl record(s) from {filename}.")
        return users, collection

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return users, collection


def export_csv(collection, filename=None):
    # Export collection to CSV, filename is none as this needs to be given by user.
    if filename is None:
        filename = input("Enter CSV filename to export: ").strip()

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            writer.writeheader()
            for vinyl in collection:
                writer.writerow({
                    "username": vinyl.username,
                    "password": find_user_password(vinyl.username),
                    "artist": vinyl.artist,
                    "album": vinyl.album,
                    "year": vinyl.year,
                    "genre": vinyl.genre,
                    "barcode": vinyl.barcode,
                    "trackcount": vinyl.trackcount,
                    "dateadded": vinyl.dateadded
                })
        print(f"Exported {len(collection)} vinyl record(s) to {filename}.")
    except Exception as e:
        print(f"Error exporting CSV: {e}")


def find_user_password(username):
    # Helper function to get user password for export.
    from auth import load_users
    user = find_user(load_users(), username)
    if user:
        return user.password
    return ""