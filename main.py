import sys
from user_manager import login_screen
from storage_json import load_collection, save_collection
from collection import add_vinyl, list_vinyls, remove_vinyl, edit_vinyl, display_vinyl
from csv_handler import import_csv_for_user, export_csv_for_user
from search import search_menu
from utils import clear_screen

def main():
    # Login
    current_user = login_screen()

    # Check if login was successful
    if current_user is None:
        print("Login failed. Exiting.")
        sys.exit()

    # Load user collection
    collection = load_collection(current_user)

    while True:
        # Main menu
        clear_screen()
        print("=== Main Menu ===")
        print("1. Add Vinyl")
        print("2. List Vinyls")
        print("3. Remove Vinyl")
        print("4. Edit Vinyl (via Search)")
        print("5. Search Vinyl")
        print("6. Import CSV")
        print("7. Export CSV")
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            clear_screen()
            add_vinyl(collection, current_user)
            input("\nPress Enter to continue...")

        elif choice == "2":
            clear_screen()
            list_vinyls(collection, current_user)
            input("\nPress Enter to continue...")

        elif choice == "3":
            clear_screen()
            # Remove vinyl by index
            user_records = [v for v in collection if v.username == current_user]
            if not user_records:
                print("No vinyl records to remove.")
                input("\nPress Enter to continue...")
                continue
            list_vinyls(collection, current_user)
            try:
                idx = int(input("Enter index of vinyl to remove: ")) - 1
                vinyl = user_records[idx]
                collection.remove(vinyl)
                save_collection(collection, current_user)
                print(f"Removed: {vinyl.summary()}")
            except (IndexError, ValueError):
                print("Invalid index.")
            input("\nPress Enter to continue...")

        elif choice == "4" or choice == "5":
            clear_screen()
            # Edit via Search or just Search
            search_menu(collection, current_user)
            input("\nPress Enter to continue...")

        elif choice == "6":
            clear_screen()
            import_csv_for_user(current_user, collection)
            input("\nPress Enter to continue...")

        elif choice == "7":
            clear_screen()
            export_csv_for_user(current_user, collection)
            input("\nPress Enter to continue...")

        elif choice == "0":
            save_collection(collection, current_user)
            clear_screen()
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid option.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()