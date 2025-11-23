from models import Vinyl
from datetime import datetime
from storage_json import save_collection
from utils import clear_screen, get_valid_year, get_valid_trackcount, get_valid_string

def add_vinyl(collection, username):
    # Add a new vinyl record
    print("\n=== Add New Vinyl ===")
    artist = get_valid_string("Artist: ", "Artist")
    album = get_valid_string("Album: ", "Album")
    year = get_valid_year("Year: ")
    genre = get_valid_string("Genre: ", "Genre")
    barcode = input("Barcode: ").strip()  # Optional, no validation for now
    trackcount = get_valid_trackcount("Number of tracks: ")
    dateadded = datetime.today().strftime("%Y-%m-%d")  # ISO format

    vinyl = Vinyl(
        artist=artist,
        album=album,
        year=year,
        genre=genre,
        barcode=barcode,
        trackcount=trackcount,  # Already an int from validation
        dateadded=dateadded,
        username=username
    )
    collection.append(vinyl)
    save_collection(collection, username)
    print(f"\nAdded: {vinyl.summary()}")


def list_vinyls(collection, username):
    # List all vinyl records for the current user in summary format
    user_records = [v for v in collection if v.username == username]
    if not user_records:
        print("No vinyl records found.")
        return

    # Ask if user wants to sort
    print("Do you want to sort the collection?")
    print("1. No sorting")
    print("2. Artist")
    print("3. Album")
    print("4. Year")
    print("5. Genre")
    print("6. Date Added")
    sort_choice = input("Choose option (1-6): ").strip()

    field_map = {
        "2": "artist",
        "3": "album",
        "4": "year",
        "5": "genre",
        "6": "dateadded"
    }

    if sort_choice in field_map:
        field = field_map[sort_choice]
        order = input("Order: [A]scending or [D]escending? ").strip().lower()
        reverse = order == "d"
        user_records.sort(
            key=lambda v: getattr(v, field).lower() if isinstance(getattr(v, field), str) else getattr(v, field),
            reverse=reverse
        )

    print(f"\n=== Vinyl Collection ({username.title()}) ===")
    for idx, vinyl in enumerate(user_records, 1):
        print(f"{idx}. {vinyl.summary()}")

    # Allow user to select one for full view
    try:
        choice = int(input("\nSelect a record to view details (0 to cancel): "))
        if choice == 0:
            return
        clear_screen()
        vinyl = user_records[choice - 1]
        display_vinyl(vinyl)

        # Offer actions on the selected record
        from search import single_record_actions
        single_record_actions(vinyl, collection, username)
    except (ValueError, IndexError):
        print("Invalid choice.")


def display_vinyl(vinyl):
    # Display full details of a single vinyl record
    print("=== Vinyl Details ===")
    print(vinyl.display())


def edit_vinyl(vinyl):
    # Edit a vinyl record
    print("\n=== Edit Vinyl ===")
    print("Leave blank to keep current value.\n")

    vinyl.artist = get_valid_string("Artist ", "Artist", current_value=vinyl.artist)
    vinyl.album = get_valid_string("Album ", "Album", current_value=vinyl.album)
    vinyl.year = get_valid_year("Year ", current_value=vinyl.year)
    vinyl.genre = get_valid_string("Genre ", "Genre", current_value=vinyl.genre)
    vinyl.barcode = input(f"Barcode [{vinyl.barcode}]: ").strip() or vinyl.barcode
    vinyl.trackcount = get_valid_trackcount("Tracks ", current_value=vinyl.trackcount)

    print("\nRecord updated.")


def remove_vinyl(collection, username):
    # Remove a vinyl record, using index from list_vinyls
    user_records = [v for v in collection if v.username == username]
    if not user_records:
        print("No vinyl records to remove.")
        return

    list_vinyls(collection, username)
    try:
        idx = int(input("Enter index of vinyl to remove: ")) - 1
        vinyl = user_records[idx]
        collection.remove(vinyl)
        save_collection(collection, username)
        print(f"Removed: {vinyl.summary()}")
    except (IndexError, ValueError):
        print("Invalid index.")