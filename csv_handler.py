import csv
from models import Vinyl
from storage_json import load_users, save_users, load_collection, save_collection

def import_csv_for_user(username, collection):
    filename = input("Enter CSV filename to import: ").strip()
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"].strip().lower() == username:
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
            save_collection(collection, username)
        print("CSV import completed.")
    except FileNotFoundError:
        print("File not found.")
    except KeyError as e:
        print(f"Missing CSV column: {e}")


def export_csv_for_user(username, collection):
    filename = input("Enter filename to export to: ").strip()
    fieldnames = ["username","artist","album","year","genre","barcode","trackcount","dateadded"]

    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for vinyl in collection:
                if vinyl.username == username:
                    writer.writerow({
                        "username": username,
                        "artist": vinyl.artist,
                        "album": vinyl.album,
                        "year": vinyl.year,
                        "genre": vinyl.genre,
                        "barcode": vinyl.barcode,
                        "trackcount": vinyl.trackcount,
                        "dateadded": vinyl.dateadded
                    })
        print("CSV export completed.")
    except Exception as e:
        print(f"Error exporting CSV: {e}")