from collection import display_vinyl, edit_vinyl
from utils import clear_screen


def search_menu(collection, username):
    # Main search menu
    print("=== Search Vinyl Collection ===")
    print("1. Search by Artist")
    print("2. Search by Album")
    print("3. Search by Genre")
    print("4. Search by Year")
    print("5. Search by Barcode")
    print("0. Back")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        term = input("Enter artist: ").strip().lower()
        results = search(collection, username, field="artist", term=term)
    elif choice == "2":
        term = input("Enter album: ").strip().lower()
        results = search(collection, username, field="album", term=term)
    elif choice == "3":
        term = input("Enter genre: ").strip().lower()
        results = search(collection, username, field="genre", term=term)
    elif choice == "4":
        term = input("Enter year: ").strip().lower()
        results = search(collection, username, field="year", term=term)
    elif choice == "5":
        term = input("Enter barcode: ").strip().lower()
        results = search(collection, username, field="barcode", term=term)
    else:
        return

    handle_results(results, collection, username)


def search(collection, username, field, term):
   # Search for records matching term in field
    results = []

    for vinyl in collection:
        if vinyl.username != username:
            continue  # only search current user's records

        value = getattr(vinyl, field).lower()
        if term in value:
            results.append(vinyl)

    return results


def handle_results(results, collection, username):
    # Handle search results matching view, if 1 show full details, if a list show summary list allowing user to chose one to view unredacted
    if len(results) == 0:
        print("\nNo matching records found.")
        return

    elif len(results) == 1:
        # Single match → Single Record View
        clear_screen()
        vinyl = results[0]
        display_vinyl(vinyl)
        single_record_actions(vinyl, collection, username)

    else:
        # Multiple matches → Summary View
        clear_screen()
        print(f"Found {len(results)} record(s):")
        for i, vinyl in enumerate(results, 1):
            print(f"{i}. {vinyl.summary()}")

        # Allow user to select one for full view
        try:
            choice = int(input("\nSelect one to view (0 to cancel): "))
            if choice == 0:
                return
            clear_screen()
            vinyl = results[choice - 1]
            display_vinyl(vinyl)
            single_record_actions(vinyl, collection, username)
        except (ValueError, IndexError):
            print("Invalid choice.")


def single_record_actions(vinyl, collection, username):
   # Actions available from single record view
    print("\n1. Edit Record")
    print("2. Delete Record")
    print("0. Back")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        edit_vinyl(vinyl)
    elif choice == "2":
        confirm = input(f"Delete '{vinyl.summary()}'? (y/n): ").strip().lower()
        if confirm == 'y':
            collection.remove(vinyl)
            from storage_json import save_collection
            save_collection(collection, username)
            print(f"Removed: {vinyl.summary()}")