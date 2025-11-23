import csv
from models import Vinyl
from storage_json import load_users, save_users, load_collection, save_collection
from utils import validate_year, validate_trackcount, validate_non_empty_string, validate_date

def import_csv_for_user(username, collection):
    filename = input("Enter CSV filename to import: ").strip()
    imported_count = 0
    skipped_count = 0

    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
                if row["username"].strip().lower() == username:
                    errors = []

                    # Validate artist
                    artist_valid, artist_value, artist_error = validate_non_empty_string(row["artist"], "Artist")
                    if not artist_valid:
                        errors.append(artist_error)

                    # Validate album
                    album_valid, album_value, album_error = validate_non_empty_string(row["album"], "Album")
                    if not album_valid:
                        errors.append(album_error)

                    # Validate year
                    year_valid, year_value, year_error = validate_year(row["year"])
                    if not year_valid:
                        errors.append(year_error)

                    # Validate genre
                    genre_valid, genre_value, genre_error = validate_non_empty_string(row["genre"], "Genre")
                    if not genre_valid:
                        errors.append(genre_error)

                    # Validate trackcount
                    trackcount_valid, trackcount_value, trackcount_error = validate_trackcount(row["trackcount"])
                    if not trackcount_valid:
                        errors.append(trackcount_error)

                    # Validate date added
                    date_valid, date_value, date_error = validate_date(row["dateadded"])
                    if not date_valid:
                        errors.append(date_error)

                    # If any validation failed, skip this row
                    if errors:
                        print(f"Row {row_num}: Skipping record - {'; '.join(errors)}")
                        print(f"  Album: {row.get('album', 'N/A')} by {row.get('artist', 'N/A')}")
                        skipped_count += 1
                        continue

                    # All validations passed, create vinyl object
                    assert artist_value is not None
                    assert album_value is not None
                    assert year_value is not None
                    assert genre_value is not None
                    assert trackcount_value is not None
                    assert date_value is not None

                    vinyl = Vinyl(
                        artist=artist_value,
                        album=album_value,
                        year=year_value,
                        genre=genre_value,
                        barcode=row["barcode"],  # No validation for barcode
                        trackcount=trackcount_value,
                        dateadded=date_value,
                        username=username
                    )
                    collection.append(vinyl)
                    imported_count += 1
            save_collection(collection, username)
        print(f"CSV import completed: {imported_count} imported, {skipped_count} skipped.")
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